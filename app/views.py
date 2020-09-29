from app.business.text_care import *
from app.models import Text, Word
from app.serializers import TextSerializer, WordSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView


class TextListAndInsert(APIView):
    def get(self, request):
        words = Text.objects.all()
        serializer = TextSerializer(words, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class WordsListAndInsert(APIView):
    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TextSerializer(data=request.data, many=False)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
