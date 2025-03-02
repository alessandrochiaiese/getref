import logging
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..services.payment_method_services import PaymentMethodService
from ..serializers import PaymentMethodSerializer

logger = logging.getLogger(__name__)

class PaymentMethodAPIView(APIView):
    permission_classes = [IsAuthenticated, HasActiveSubscription]
    renderer_classes = [JSONRenderer]

    def __init__(self, *args, **kwargs):
        self.service = PaymentMethodService()

    @swagger_auto_schema(
        operation_summary="List all PaymentMethod",
        operation_description="Returns a list of all PaymentMethod entries.",
        responses={
            200: openapi.Response('Successful Response', PaymentMethodSerializer(many=True)),
            500: 'Internal Server Error'
        },
        tags=['PaymentMethod']
    )
    def get(self, request, pk=None):
        try:
            if pk:
                obj = self.service.get_by_id(pk)
                serializer = PaymentMethodSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                objs = self.service.get_all()
                serializer = PaymentMethodSerializer(objs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching PaymentMethod: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Create new PaymentMethod",
        operation_description="Creates a new PaymentMethod entry.",
        request_body=PaymentMethodSerializer,
        responses={
            201: openapi.Response('Created', PaymentMethodSerializer),
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        tags=['PaymentMethod']
    )
    def post(self, request):
        try:
            serializer = PaymentMethodSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.create(serializer.validated_data)
                return Response(PaymentMethodSerializer(obj).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating PaymentMethod: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Update a PaymentMethod entry",
        operation_description="Updates a specific PaymentMethod entry by ID.",
        request_body=PaymentMethodSerializer,
        responses={
            200: openapi.Response('Successful Response', PaymentMethodSerializer),
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['PaymentMethod']
    )
    def put(self, request, pk=None):
        try:
            serializer = PaymentMethodSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.update(pk, serializer.validated_data)
                return Response(PaymentMethodSerializer(obj).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating PaymentMethod: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Delete a PaymentMethod entry",
        operation_description="Deletes a specific PaymentMethod entry by ID.",
        responses={
            204: 'No Content',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['PaymentMethod']
    )
    def delete(self, request, pk=None):
        try:
            self.service.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting PaymentMethod: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
