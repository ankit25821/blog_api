from rest_framework import generics
from django.http import HttpResponse
from api import serializers
from django.contrib.auth.models import User
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from api.models import Comment, Category, Post, Contact
from django.core import serializers as custom_serializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]



class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.AllowAny]

class ContactDetail(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.AllowAny]


class CategoryWisePost(generics.ListAPIView):
    serializer_class = serializers.CategoryWisePostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        cat_id = self.kwargs.get('pk')
        data = Post.objects.filter(categories__id=cat_id)
        return data


def api_root(request):
    return HttpResponse("Sorry, You are on wrong URL.")