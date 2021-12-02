from rest_framework import serializers
from books.models import Book,Tag
from django.contrib.auth.models import User

class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    

        fields = ['first_name', 'username' ,'email'] 

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']


class BookSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)
    tags = TagSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'
