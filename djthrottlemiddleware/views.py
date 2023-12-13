from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.throttling import ScopedRateThrottle
from rest_framework import status

from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer
from .decorators import check_throttle
from middleware.throttle_middleware import CustomThrottle1, CustomThrottle2, RateThrottle

class ArticleView(APIView):
    throttle_scope = 'limited_scope1'
    throttle_classes = [CustomThrottle1]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})


class AuthorView(APIView):
    throttle_scope = 'premium_users'
    # throttle_classes = [ScopedRateThrottle] # 'rest_framework.throttling.ScopedRateThrottle'

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})


class ExampleView(APIView):
    """ This class is for throttling seperated apis with using decorators"""
    
    @check_throttle(CustomThrottle1)
    def get(self, request):
        return Response("Get Success", status=status.HTTP_200_OK)
    
    @check_throttle(CustomThrottle2)
    def post(self, request):
        return Response("Post Success", status=status.HTTP_200_OK)
    
    @check_throttle(RateThrottle)
    def put(self, request):
        return Response("Put Success", status=status.HTTP_200_OK)

    def patch(self, request):
        return Response("Patch Success", status=status.HTTP_200_OK)
    
    def delete(self, request):
        return Response("Delete Success", status=status.HTTP_200_OK)
