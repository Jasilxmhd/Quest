from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from .serializers import EmployeeSerislizer
from .models import Employee



@api_view(["GET"])
def get_employee(request):
    emp = Employee.objects.all()

    s = EmployeeSerislizer(emp, many = True)
    return Response(s.data)




@api_view(['POST'])
def employee_create(request):

    serializer = EmployeeSerislizer(
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





@api_view(['PUT'])
def employee_update(request, id):

    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"},status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerislizer(employee,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['PATCH'])
def employee_partialupdate(request, id):

    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"},status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerislizer(employee,data=request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)







@api_view(['DELETE'])
def employee_delete(request, id):

    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"},status=status.HTTP_404_NOT_FOUND)

    employee.delete()

    return Response({"message": "Employee deleted successfully"},status=status.HTTP_200_OK)












# @api_view(['GET'])
# def greet(request):
#     return Response({"message": "Hello welcome to DRF tutorials..."})


