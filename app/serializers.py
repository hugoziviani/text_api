from app.models import Text, Word

from rest_framework import serializers

class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = ['text_id', 'text', 'inserted_at']

class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ['word_id', 'word', 'inserted_at']