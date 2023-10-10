from django.shortcuts import render
from rest_framework.response import Response
from . models import student
from .serializers import SudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return render(request,'Rest_API/index.html')


@api_view(['GET','POST'])
def student_list(request):
    if request.method=="GET":
        students=student.objects.all()
        serializer=SudentSerializer(students,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=SudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        students=student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        students=student.objects.get(pk=pk)
        serializer=SudentSerializer(students)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer=SudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


