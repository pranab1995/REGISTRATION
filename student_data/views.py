from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Student
from rest_framework.decorators import api_view


@api_view(['POST'])
def add_student(request):
    if request.method == "POST":
        instance = Student(title=request.data['title'],first_name=request.data['first_name'],last_name=request.data['last_name'], email=request.data['email'], country=request.data['country'], message=request.data['message'], password=request.data['password'])
        instance.save()

    return JsonResponse({'message': 'Student added successfully'}, status=200)

@api_view(['GET'])
def get_student(request):
    students = Student.objects.values()
    return JsonResponse(list(students), safe=False)

@api_view(['PUT'])
def edit_student(request, id):
    instance = Student.objects.get(id=request.data['id']) 
    instance.title = request.data['title']
    instance.first_name = request.data['first_name']
    instance.last_name = request.data['last_name']
    instance.email = request.data['email']
    instance.country = request.data['country']
    instance.message = request.data['message']
    instance.password = request.data['password']
    instance.save()
    return JsonResponse({'message': 'Student updated successfully'}, status=200)


@api_view(['DELETE'])
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponse(student, HttpResponse.status_code)
    