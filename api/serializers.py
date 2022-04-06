from urllib import request
from django.forms import CharField
from rest_framework import serializers
from setuptools import Require
from .models import User,Task

# TO DO 1
class Singup_serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extract_kwargs = {
            'password':{'write_only':True}
            }
    #  TO DO 11
    def save(self):
        account = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'], 
                )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password!= password2:
            raise serializers.ValidationError({'password':'passwords must match.'})
        account.set_password(password)
        account.save()
        return account
# TO DO 2
class Task_serializer(serializers.ModelSerializer):
    # Description_of_task = serializers.CharField(required=False)
    # Date_of_completion = serializers.DateTimeField(required=False)
    # user = serializers.CharField(required=False)
    class Meta:
        model = Task
        fields =['name_task',
        'Description_of_task',
        'user',
        'Date_of_completion' ,
        'Status' ,
        'Date_of_creation' ,
        'Date_of_modification' ]
        # extract_kwargs = {
        #     'Description_of_task':{'required':False},
        #     'user':{'required':False},
        #     'Date_of_completion':{'required':False}
        #     }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']