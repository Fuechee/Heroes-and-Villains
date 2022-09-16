from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from supers import serializers

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':

        supers_name = request.query_params.get('supers')

        queryset = Super.objects.all()

        if supers_name:
            queryset = queryset.filter(supers__name=supers_name)

        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    car = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)