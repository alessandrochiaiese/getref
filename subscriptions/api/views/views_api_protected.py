from typing import Literal
from rest_framework.views import APIView
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from subscriptions.models import APIKey, APIUsageLog
from django_ratelimit.decorators import ratelimit

class ProtectedAPI(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]

    @ratelimit(key="user", rate="10/m", method="GET", block=True)
    def get(self, request):
        token = request.auth
        api_key = APIKey.objects.get(client_id=token.application.client_id)
        api_key.update_usage()
        APIUsageLog.objects.create(api_key=api_key, endpoint=request.path)
        return Response({"message": "Accesso autorizzato!"})
"""
class ProtectedAPI(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]

    def get(self, request):
        token = request.auth
        api_key = APIKey.objects.get(client_id=token.application.client_id)
        api_key.update_usage()

        APIUsageLog.objects.create(api_key=api_key, endpoint=request.path)

        return Response({"message": "Accesso autorizzato!"})


class ProtectedAPI(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]

    def get_rate_limit(self, request) -> Literal['100/m'] | Literal['10/m']:
        api_key = APIKey.objects.get(client_id=request.auth.application.client_id)
        return "100/m" if api_key.plan == "pro" else "10/m"

    def get(self, request):
        token = request.auth
        api_key = APIKey.objects.get(client_id=token.application.client_id)
        rate = self.get_rate_limit(request)
        with ratelimit(key="user", rate=rate, method="GET", block=True):
            api_key.update_usage()
            APIUsageLog.objects.create(api_key=api_key, endpoint=request.path)
            return Response({"message": "Accesso autorizzato!"})

"""