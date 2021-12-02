from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes , permission_classes
from rest_framework.response import Response
from books.models import Book

from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
def get_routes(request):
    routes = [

        {'GET','api/books'},
        {'GET','api/book/id'},
        
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    return Response(serializer.data)
  

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_book(request,pk):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated)
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
