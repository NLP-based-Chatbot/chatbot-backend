from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from newsfeed.models import News
from newsfeed.serializer import NewsSerializer

@api_view(['GET'])
def news_list(request, domain):
    if request.method == 'GET':
        snippets = News.objects.filter(domain=domain)
        serializer = NewsSerializer(snippets, many=True)

        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def news_detail(request, pk):
    try:
        snippet = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = NewsSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = NewsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def news_view(request):
    if request.method == 'GET':
        snippets = News.objects.all()
        serializer = NewsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)