from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .permissions import IsAdminOrReadOnly, IsUserOrReadOnly
from .serializers import WomenSerializer

class WomenAPIListPost(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsUserOrReadOnly, )

class WomenAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )





# class WomenViewSet(viewsets.ModelViewSet):
#       # queryset = Women.objects.all()
#       serializer_class = WomenSerializer
#
#       def get_queryset(self):
#           pk = self.kwargs.get('pk')
#
#           if not pk:
#               return Women.objects.all()[:3]
#
#           return Women.objects.filter(pk=pk)
#
#       @action(methods=['get'], detail=True)
#       def category(self, request, pk):
#           cats = Category.objects.get(pk=pk)
#           return Response({'cats': cats.name})


# class WomenView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenPost(APIView):
#     def get(self, request):
#         posts = Women.objects.all()
#         return Response({'post': WomenSerializer(posts, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({'Error': 'error'})
#
#         instance = Women.objects.get(pk=pk)
#
#         serializer = WomenSerializer(instance=instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({'Error': 'error'})
#         # print(request.data)
#         Women.objects.get(pk=pk).delete()
#
#         return Response({"post": 'Пост ' + str(pk) + ' удален'})

# serializer = WomenSerializer()

# Create your views here.
