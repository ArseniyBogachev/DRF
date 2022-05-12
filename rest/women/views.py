from djoser.views import UserViewSet
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import exception_handler
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import *
from .permissions import IsAdminOrReadOnly, IsUserOrReadOnly
from .serializers import WomenSerializer, UserSerializer


class Home(ListView):
    template_name = 'index.html'
    model = Women

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class WomenAPIListPost(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsUserOrReadOnly, )

class WomenAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CustomRegistrationView(UserViewSet):
    queryset = WomenUser.objects.all()
    serializer_class = UserSerializer


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    print(response)
    return response
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
