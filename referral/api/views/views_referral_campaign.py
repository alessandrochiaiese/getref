import logging
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..services.referral_campaign_service import ReferralCampaignService
from ...models.referral_campaign import ReferralCampaign
from ..serializers import ReferralCampaignSerializer
from dashboard.api.permissions import HasActiveSubscription

# Set up a logger
logger = logging.getLogger(__name__)

class ReferralCampaignAPIView(APIView):
    permission_classes = [IsAuthenticated, HasActiveSubscription]  # [AllowAny]  or [IsAuthenticated]  or [HasActiveSubscription]
    renderer_classes = [JSONRenderer]
    authentication_classes = [
        SessionAuthentication,  # Funziona per web app con sessione
        BasicAuthentication,    # Funziona per login base con username/password
        OAuth2Authentication,   # Funziona per autenticazione tramite OAuth2
        TokenAuthentication     # Funziona per Bearer token (es. JWT)
    ]

    def __init__(self, *args, **kwargs):
        self.referral_campaign_service = ReferralCampaignService()

    @swagger_auto_schema(
        operation_summary="List all referral_campaign",
        operation_description="Returns a list of all referral_campaign entries.",
        responses={
            200: openapi.Response('Successful Response', ReferralCampaignSerializer(many=True)),
            500: 'Internal Server Error'
        },
        tags=['referral_campaign']
    )
    def get(self, request, referral_campaign_id = None):
        try:
            if referral_campaign_id == None:
                referral_campaign = ReferralCampaign.objects.all()
                serializer = ReferralCampaignSerializer(referral_campaign, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                referral_campaign = self.referral_campaign_service.get_referral_campaign(referral_campaign_id)
                serializer = ReferralCampaignSerializer(referral_campaign)
                return Response(serializer.data, status=status.HTTP_200_OK)  
        except ReferralCampaign.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error fetching referral_campaign: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Create new referral_campaign",
        operation_description="Creates a new referral_campaign entry.",
        request_body=ReferralCampaignSerializer,
        responses={
            201: openapi.Response('Created', ReferralCampaignSerializer),
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        tags=['referral_campaign']
    )
    def post(self, request):
        try:
            data=request.data
            serializer = ReferralCampaignSerializer(data=data)
            if serializer.is_valid():
                referral_campaign = self.referral_campaign_service.create_referral_campaign(serializer.validated_data)
                return Response(ReferralCampaignSerializer(referral_campaign).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating referral_campaign: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    @swagger_auto_schema(
        operation_summary="Update a referral_campaign entry",
        operation_description="Updates a specific referral_campaign entry by ID.",
        request_body=ReferralCampaignSerializer,
        responses={
            200: openapi.Response('Successful Response', ReferralCampaignSerializer),
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['referral_campaign']
    )
    def put(self, request, referral_campaign_id=None):
        try: 
            serializer = ReferralCampaignSerializer(data=request.data)
            if serializer.is_valid():
                referral_campaign = self.referral_campaign_service.update_referral_campaign(referral_campaign_id, serializer.validated_data)
                return Response(ReferralCampaignSerializer(referral_campaign).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ReferralCampaign.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating referral_campaign: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Delete a referral_campaign entry",
        operation_description="Deletes a specific referral_campaign entry by ID.",
        responses={
            204: 'No Content',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['referral_campaign']
    )
    def delete(self, request, referral_campaign_id=None):
        try:
            referral_campaign = self.referral_campaign_service.delete_referral_campaign(referral_campaign_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ReferralCampaign.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error deleting referral_campaign: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
