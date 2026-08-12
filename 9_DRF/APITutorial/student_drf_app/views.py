from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from .serializers import StudentSerislizer
from .models import Student



@api_view(["GET"])
def get_student(request):
    stud = Student.objects.all()

    st = StudentSerislizer(stud, many = True)
    return Response(st.data)




@api_view(['POST'])
def student_create(request):

    serializer = StudentSerislizer(
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





@api_view(['PUT'])
def student_update(request, id):

    try:
        employee = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"},status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerislizer(employee,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['PATCH'])
def student_partial_update(request, id):

    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"},status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerislizer(student,data=request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)







@api_view(['DELETE'])
def student_delete(request, id):

    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"},status=status.HTTP_404_NOT_FOUND)

    student.delete()

    return Response({"message": "Student deleted successfully"},status=status.HTTP_200_OK)






