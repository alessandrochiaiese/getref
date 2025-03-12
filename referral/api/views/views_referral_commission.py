import logging
from django.http import JsonResponse
from referral.api.serializers import ReferralCommissionSerializer
from referral.models.referral_commission import ReferralCommission
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..services.referral_commission_service import ReferralCommissionService 
from dashboard.api.permissions import HasActiveSubscription

# Set up a logger
logger = logging.getLogger(__name__)

class ReferralCommissionAPIView(APIView):
    permission_classes = [IsAuthenticated, HasActiveSubscription]  # [AllowAny]  or [IsAuthenticated]  or [HasActiveSubscription]
    renderer_classes = [JSONRenderer]
    authentication_classes = [
        SessionAuthentication,  # Funziona per web app con sessione
        BasicAuthentication,    # Funziona per login base con username/password
        OAuth2Authentication,   # Funziona per autenticazione tramite OAuth2
        TokenAuthentication     # Funziona per Bearer token (es. JWT)
    ]

    def __init__(self, *args, **kwargs):
        self.referral_commission_service = ReferralCommissionService()

    @swagger_auto_schema(
        operation_summary="List all referral_commission",
        operation_description="Returns a list of all referral_commission entries.",
        responses={
            200: openapi.Response('Successful Response', ReferralCommissionSerializer(many=True)),
            500: 'Internal Server Error'
        },
        tags=['referral_commission']
    )
    def get(self, request, referral_commission_id = None):
        try:
            if referral_commission_id == None:
                referral_commission = ReferralCommission.objects.all()
                serializer = ReferralCommissionSerializer(referral_commission, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                referral_commission = self.referral_commission_service.get_referral_commission(referral_commission_id)
                serializer = ReferralCommissionSerializer(referral_commission)
                return Response(serializer.data, status=status.HTTP_200_OK)  
        except ReferralCommission.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error fetching referral_commission: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Create new referral_commission",
        operation_description="Creates a new referral_commission entry.",
        request_body=ReferralCommissionSerializer,
        responses={
            201: openapi.Response('Created', ReferralCommissionSerializer),
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        tags=['referral_commission']
    )
    def post(self, request):
        try:
            serializer = ReferralCommissionSerializer(data=request.data)
            if serializer.is_valid():
                referral_commission = self.referral_commission_service.create_referral_commission(serializer.validated_data)
                return Response(ReferralCommissionSerializer(referral_commission).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating referral_commission: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    @swagger_auto_schema(
        operation_summary="Update a referral_commission entry",
        operation_description="Updates a specific referral_commission entry by ID.",
        request_body=ReferralCommissionSerializer,
        responses={
            200: openapi.Response('Successful Response', ReferralCommissionSerializer),
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['referral_commission']
    )
    def put(self, request, referral_commission_id=None):
        try: 
            serializer = ReferralCommissionSerializer(data=request.data)
            if serializer.is_valid():
                referral_commission = self.referral_commission_service.update_referral_commission(referral_commission_id, serializer.validated_data)
                return Response(ReferralCommissionSerializer(referral_commission).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ReferralCommission.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating referral_commission: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Delete a referral_commission entry",
        operation_description="Deletes a specific referral_commission entry by ID.",
        responses={
            204: 'No Content',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['referral_commission']
    )
    def delete(self, request, referral_commission_id=None):
        try:
            referral_commission = self.referral_commission_service.delete_referral_commission(referral_commission_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ReferralCommission.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error deleting referral_commission: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
