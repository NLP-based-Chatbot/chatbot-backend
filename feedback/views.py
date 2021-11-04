from feedback.serializer import FeedbackSerializer
from feedback.models import Feedback
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def feedback_view(request):
    if request.method == 'GET':
        snippets = Feedback.objects.all()
        serializer = FeedbackSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)