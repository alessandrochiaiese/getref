import logging
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..services.stats_services import StatsService
from ..serializers import StatsSerializer

logger = logging.getLogger(__name__)

class StatsAPIView(APIView):
    permission_classes = [IsAuthenticated, HasActiveSubscription]
    renderer_classes = [JSONRenderer]

    def __init__(self, *args, **kwargs):
        self.service = StatsService()

    @swagger_auto_schema(
        operation_summary="List all Stats",
        operation_description="Returns a list of all Stats entries.",
        responses={
            200: openapi.Response('Successful Response', StatsSerializer(many=True)),
            500: 'Internal Server Error'
        },
        tags=['Stats']
    )
    def get(self, request, pk=None):
        try:
            if pk:
                obj = self.service.get_by_id(pk)
                serializer = StatsSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                objs = self.service.get_all()
                serializer = StatsSerializer(objs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching Stats: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Create new Stats",
        operation_description="Creates a new Stats entry.",
        request_body=StatsSerializer,
        responses={
            201: openapi.Response('Created', StatsSerializer),
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        tags=['Stats']
    )
    def post(self, request):
        try:
            serializer = StatsSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.create(serializer.validated_data)
                return Response(StatsSerializer(obj).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating Stats: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Update a Stats entry",
        operation_description="Updates a specific Stats entry by ID.",
        request_body=StatsSerializer,
        responses={
            200: openapi.Response('Successful Response', StatsSerializer),
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['Stats']
    )
    def put(self, request, pk=None):
        try:
            serializer = StatsSerializer(data=request.data)
            if serializer.is_valid():
                obj = self.service.update(pk, serializer.validated_data)
                return Response(StatsSerializer(obj).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating Stats: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Delete a Stats entry",
        operation_description="Deletes a specific Stats entry by ID.",
        responses={
            204: 'No Content',
            404: 'Not Found',
            500: 'Internal Server Error'
        },
        tags=['Stats']
    )
    def delete(self, request, pk=None):
        try:
            self.service.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting Stats: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
