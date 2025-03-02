import logging
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..services.audit_services import AuditService
from ..serializers import AuditSerializer

logger = logging.getLogger(__name__)

class AuditAPIView(APIView):
    permission_classes = [IsAuthenticated, HasActiveSubscription]
    renderer_classes = [JSONRenderer]

    def __init__(self, *args, **kwargs):
        self.service = AuditService()

    @swagger_auto_schema(
        operation_summary="List all Audit",
        operation_description="Returns a list of all Audit entries.",
        responses={
            200: openapi.Response('Successful Response', AuditSerializer(many=True)),
            500: 'Internal Server Error'
        },
        tags=['Audit']
    )
    def get(self, request, pk=None):
        try:
            if pk:
                obj = self.service.get_by_id(pk)
                serializer = AuditSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                objs = self.service.get_all()
                serializer = AuditSerializer(objs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching Audit: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Create new Audit",
        operation_description="Creates a new Audit entry.",
        request_body=AuditSerializer,
        responses={
            201: openapi.Response('Created', AuditSerializer),
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        tags=['Audit']
    )
    def post(self, request):
        try:
            serializer = AuditSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.create(serializer.validated_data)
                return Response(AuditSerializer(obj).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating Audit: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Update a Audit entry",
        operation_description="Updates a specific Audit entry by ID.",
        request_body=AuditSerializer,
        responses={
            200: openapi.Response('Successful Response', AuditSerializer),
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['Audit']
    )
    def put(self, request, pk=None):
        try:
            serializer = AuditSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.update(pk, serializer.validated_data)
                return Response(AuditSerializer(obj).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating Audit: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Delete a Audit entry",
        operation_description="Deletes a specific Audit entry by ID.",
        responses={
            204: 'No Content',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['Audit']
    )
    def delete(self, request, pk=None):
        try:
            self.service.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting Audit: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
