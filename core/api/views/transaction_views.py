import logging
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..services.transaction_services import TransactionService
from ..serializers import TransactionSerializer

logger = logging.getLogger(__name__)

class TransactionAPIView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]

    def __init__(self, *args, **kwargs):
        self.service = TransactionService()

    @swagger_auto_schema(
        operation_summary="List all Transaction",
        operation_description="Returns a list of all Transaction entries.",
        responses={
            200: openapi.Response('Successful Response', TransactionSerializer(many=True)),
            500: 'Internal Server Error'
        },
        tags=['Transaction']
    )
    def get(self, request, pk=None):
        try:
            if pk:
                obj = self.service.get_by_id(pk)
                serializer = TransactionSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                objs = self.service.get_all()
                serializer = TransactionSerializer(objs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching Transaction: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Create new Transaction",
        operation_description="Creates a new Transaction entry.",
        request_body=TransactionSerializer,
        responses={
            201: openapi.Response('Created', TransactionSerializer),
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        tags=['Transaction']
    )
    def post(self, request):
        try:
            serializer = TransactionSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.create(serializer.validated_data)
                return Response(TransactionSerializer(obj).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating Transaction: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Update a Transaction entry",
        operation_description="Updates a specific Transaction entry by ID.",
        request_body=TransactionSerializer,
        responses={
            200: openapi.Response('Successful Response', TransactionSerializer),
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['Transaction']
    )
    def put(self, request, pk=None):
        try:
            serializer = TransactionSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.update(pk, serializer.validated_data)
                return Response(TransactionSerializer(obj).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating Transaction: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Delete a Transaction entry",
        operation_description="Deletes a specific Transaction entry by ID.",
        responses={
            204: 'No Content',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['Transaction']
    )
    def delete(self, request, pk=None):
        try:
            self.service.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting Transaction: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
