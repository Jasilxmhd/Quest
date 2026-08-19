
# python -m venv venv
# venv\Scripts\activate

# pip install Django

# django-admin startproject APITutorial
# cd APITutorial

# python manage.py startapp first_drf_app

# pip install djangorestframework





# INSTALLED_APPS = [
#     # ...
#     'rest_framework',
#     'api',
# ]




# Create a serializer: ( serializers.py )


# from rest_framework import serializers
# from .models import Student


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'