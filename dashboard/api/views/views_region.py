import logging
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View 
from django.db.models import Sum 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from dashboard.api.services.region_service import RegionService
from dashboard.models.region import Region
from dashboard.api.serializers import RegionSerializer
from referral.models import *
from dashboard.api.permissions import HasActiveSubscription

# Set up a logger
logger = logging.getLogger(__name__)

class RegionAPIView(APIView):
    permission_classes = [AllowAny]  # [AllowAny]  or [IsAuthenticated]  or [HasActiveSubscription]
    renderer_classes = [JSONRenderer]
    authentication_classes = [OAuth2Authentication]

    def __init__(self, *args, **kwargs):
        self.region_service = RegionService()

    @swagger_auto_schema(
        operation_summary="List all region",
        operation_description="Returns a list of all region entries.",
        responses={
            200: openapi.Response('Successful Response', RegionSerializer(many=True)),
            500: 'Internal Server Error'
        },
        tags=['region']
    )
    def get(self, request, pk = None):
        try:
            if pk == None:
                region = Region.objects.all()
                serializer = RegionSerializer(region, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                region = self.region_service.get_region(pk)
                serializer = RegionSerializer(region)
                return Response(serializer.data, status=status.HTTP_200_OK)  
        except Region.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error fetching region: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Create new region",
        operation_description="Creates a new region entry.",
        request_body=RegionSerializer,
        responses={
            201: openapi.Response('Created', RegionSerializer),
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        tags=['region']
    )
    def post(self, request):
        try:
            serializer = RegionSerializer(data=request.data)
            if serializer.is_valid():
                region = self.region_service.create_region(serializer.validated_data)
                return Response(RegionSerializer(region).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating region: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    @swagger_auto_schema(
        operation_summary="Update a region entry",
        operation_description="Updates a specific region entry by ID.",
        request_body=RegionSerializer,
        responses={
            200: openapi.Response('Successful Response', RegionSerializer),
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['region']
    )
    def put(self, request, region_id=None):
        try: 
            region = Region.objects.get(id=region_id)
            serializer = RegionSerializer(instance=region, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Region.DoesNotExist:
            # Profilo non trovato
            error_message = f"Region with id {region_id} does not exist."
            logger.error(error_message)
            return Response({'error': error_message}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Qualsiasi altro errore generico
            logger.error(f"Error updating region: {str(e)}")
            return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Delete a region entry",
        operation_description="Deletes a specific region entry by ID.",
        responses={
            204: 'No Content',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['region']
    )
    def delete(self, request, pk=None):
        try:
            region = self.region_service.delete_region(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Region.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error deleting region: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(login_required, name='dispatch')
class UserRegionDataView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
 
        
        # Dati generali di referral
        referral_data = {
            # Totale delle commissioni: supponendo che siano in ReferralTransaction o ReferralReward
            'total_commission': ReferralTransaction.objects.filter(referral_codes__user=user).aggregate(Sum('conversion_value'))['conversion_value__sum'] or 0,
            
            # Totale delle ricompense (bonus e premi)
            #'total_rewards': (ReferralBonus.objects.filter(user=user).aggregate(Sum('bonus_value'))['bonus_value__sum'] or 0) + 
            #                (ReferralReward.objects.filter(referred_user=user).aggregate(Sum('reward_value'))['reward_value__sum'] or 0),
            
            'total_rewards': (ReferralReward.objects.filter(referred_user=user).aggregate(Sum('reward_value'))['reward_value__sum'] or 0),
            
            # Numero di referral attivi
            'active_referrals': Referral.objects.filter(referrer=user).count(),
            
            # Conversioni totali da ReferralConversion
            'total_conversions': ReferralConversion.objects.filter(referral_codes__user=user).count(),

            # Totale delle transazioni da ReferralTransaction
            'total_transactions': ReferralTransaction.objects.filter(referral_codes__user=user).aggregate(Sum('transaction_amount'))['transaction_amount__sum'] or 0,
        }


        # Dati per i codici referral
        referral_codes = ReferralCode.objects.filter(user=user).values('code', 'usage_count')

        # Dati per le campagne attive
        #active_campaigns = ReferralCampaign.objects.filter(is_active=True).values('id', 'campaign_name', 'start_date', 'end_date', 'goal', 'budget', 'spending_to_date', 'target_audience')

        # Statistiche dei referral
        referral_stats = list(ReferralStats.objects.filter(referral_codes__user=user).values('period', 'click_count', 'conversion_count', 'total_rewards', 'average_conversion_value', 'highest_referral_earning'))

        # Transazioni dei referral
        #referral_transactions = list(ReferralTransaction.objects.filter(referral_codes__in__referral_codes=referral_codes).values('referred_user', 'transaction_date', 'order_id', 'transaction_amount', 'currency', 'status', 'conversion_value', 'discount_value', 'coupon_code_used', 'channel'))

        # Audit dei referral
        recent_audits = list(ReferralAudit.objects.filter(user=user).values('referral_codes', 'action_taken', 'action_date', 'user', 'ip_address', 'device_info', 'location'))

        # Codice referral unico dell'utente
        referral_code = ReferralCode.objects.filter(user=user).first()

        data = {
            'referral_data': referral_data,
            'referral_codes': list(referral_codes),
            #'referral_campaigns': list(active_campaigns),
            'referral_stats': referral_stats,
            #'referral_transactions': referral_transactions, 
            'recent_audits': recent_audits,
            'referral_code': referral_code.code if referral_code else ''
        }

        return JsonResponse(data, status=200)
    