from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Image
from .serializers import uploadImageSerializer


# Create your views here.
@api_view(['POST', 'GET'])
def uploadImage(request):
    if request.method == 'GET':
        guests =Image.objects.all()
        serializer =uploadImageSerializer(guests, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = uploadImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
