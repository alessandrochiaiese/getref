import logging
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..services.referral_code_services import ReferralCodeService
from ..serializers import ReferralCodeSerializer

logger = logging.getLogger(__name__)

class ReferralCodeAPIView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]

    def __init__(self, *args, **kwargs):
        self.service = ReferralCodeService()

    @swagger_auto_schema(
        operation_summary="List all ReferralCode",
        operation_description="Returns a list of all ReferralCode entries.",
        responses={
            200: openapi.Response('Successful Response', ReferralCodeSerializer(many=True)),
            500: 'Internal Server Error'
        },
        tags=['ReferralCode']
    )
    def get(self, request, pk=None):
        try:
            if pk:
                obj = self.service.get_by_id(pk)
                serializer = ReferralCodeSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                objs = self.service.get_all()
                serializer = ReferralCodeSerializer(objs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching ReferralCode: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Create new ReferralCode",
        operation_description="Creates a new ReferralCode entry.",
        request_body=ReferralCodeSerializer,
        responses={
            201: openapi.Response('Created', ReferralCodeSerializer),
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        tags=['ReferralCode']
    )
    def post(self, request):
        try:
            serializer = ReferralCodeSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.create(serializer.validated_data)
                return Response(ReferralCodeSerializer(obj).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating ReferralCode: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Update a ReferralCode entry",
        operation_description="Updates a specific ReferralCode entry by ID.",
        request_body=ReferralCodeSerializer,
        responses={
            200: openapi.Response('Successful Response', ReferralCodeSerializer),
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['ReferralCode']
    )
    def put(self, request, pk=None):
        try:
            serializer = ReferralCodeSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.update(pk, serializer.validated_data)
                return Response(ReferralCodeSerializer(obj).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating ReferralCode: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Delete a ReferralCode entry",
        operation_description="Deletes a specific ReferralCode entry by ID.",
        responses={
            204: 'No Content',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['ReferralCode']
    )
    def delete(self, request, pk=None):
        try:
            self.service.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting ReferralCode: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
