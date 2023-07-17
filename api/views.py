from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action, permission_classes
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema


from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.http import JsonResponse

class Lion(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema()
    @action(detail=False, methods=["GET"])
    def test_lion(self, request):
        print(request.COOKIES)
        print(getattr(request._request, 'user', None))
        data = {"status": "ca marche, Lion!"}
        return JsonResponse(data, safe=False)


    @swagger_auto_schema()
    @action(detail=False, methods=["POST"])
    def test_lion_post(self, request):
        data = {"status": "ca marche Post POST!"}
        return JsonResponse(data, safe=False, status=200)