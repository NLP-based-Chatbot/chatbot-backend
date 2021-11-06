from rest_framework import serializers
from newsfeed.models import Instruction, News
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'domain', 'title', 'body', 'date', 'img_url']

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['id', 'domain', 'label', 'body']