from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from cadastros.models import Cidade
from cadastros.serializers import CidadeSerializer


# class CidadeAPI(APIView):
#
#     def get(self, request, format=None):
#
#         cidades = Cidade.objects.all()
#         serializer = CidadeSerializer(cidades, many=True)
#
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

class CidadeAPIList(ListCreateAPIView):

    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

