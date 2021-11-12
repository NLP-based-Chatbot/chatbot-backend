from rest_framework import status
from feedback.serializer import FeedbackSerializer
from feedback.models import Feedback
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import Coalesce, Lower
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def feedback_view(request):
    if request.method == 'GET':
        snippets = Feedback.objects.all().order_by('timestamp').reverse()
        serializer = FeedbackSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def feedback_update_view(request, pk):
    try:
        feedback = Feedback.objects.get(pk=pk)
    except Feedback.DoesNotExist:
        return JsonResponse({'message': 'No such feedback object exists'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(feedback, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
