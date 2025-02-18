import logging
from pet_manager.models import Animal
from pet_manager.serializers import AdoptionProfileSerializer, ListAdoptionSerializer

from rest_framework import permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class AdoptionAnimalsViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request):
        return Response(ListAdoptionSerializer(Animal.objects.all(), many=True),status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        return Response(AdoptionProfileSerializer(Animal.objects.filter(pk=pk).first()).data,status=status.HTTP_200_OK)
    
    def create(self, request):
        return Response(status=status.HTTP_200_OK)
    