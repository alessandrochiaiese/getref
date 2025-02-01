
from rest_framework.views import APIView
from rest_framework.response import Response
from subscriptions.models.api_usage_log import APIUsageLog


class MyLoggingView(APIView):
    def get(self, request):
        APIUsageLog.objects.create(
            api_key=request.headers.get("Authorization", "unknown"),
            endpoint=request.path
        )
        return Response({"message": "Logged successfully!"})
    