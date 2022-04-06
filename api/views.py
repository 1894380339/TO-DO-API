from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response
from .serializers import Singup_serializer,Task_serializer,UserSerializer
from .utils import generate_access_token,generate_refresh_token
from .models import User,Task
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import exceptions,status
# Create your views here.
# TO DO 1 SIGN-UP

@api_view(['POST',])
@permission_classes([AllowAny])
def SING_UP(request):
    if request.method == 'POST':
        serializer = Singup_serializer(data = request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save()
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)


# TO DO 2 SIGN-IN
# @ensure_csrf_cookie
@api_view(['POST',])
@permission_classes([AllowAny])
def SING_IN(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
    serialized_user = UserSerializer(user).data
    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)
    response = Response()
    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }
    return response

# TO DO 3 ADD-TO-DO
@api_view(['POST',])
def ADD_TO_DO(request):
    if request.method == 'POST':
        serializer = Task_serializer(data = request.data)
        data={}
        if serializer.is_valid():
            task = serializer.save()
            data['response'] = "Success"
        else:
            data = serializer.errors
        return Response(data)
# TO DO 6
@api_view(['GET'])
def GET_ALL_TO_DO(request):
    """
    List all  to do
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = Task_serializer(tasks, many=True)
        return Response(serializer.data)
# TO DO 4 + 5 UPDATE-TO-DO & REMOVE-TO-DO:
@api_view(['PUT','GET','DELETE'])
def Revise(request,task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response("Not found task")
    if request.method == 'GET':
        serializer = Task_serializer(task)
        return Response(serializer.data)
    if request.method == 'PUT':
        if task.Status is True:
                return Response("Task status is COMPLETE, Unable to edit")
        serializer = Task_serializer(task,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        if task.Status is True:
            return Response("Task status is COMPLETE, Unable to delete",status = status.HTTP_406_NOT_ACCEPTABLE)
        task.delete()
        return Response("Delete Task Successfully",status = status.HTTP_200_OK)

# TO DO 7 GET-TO-DO-BY-ID
@api_view(['POST'])
def GET_TO_DO_BY_ID(request):
    task_id = request.data["id"]
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response("Not found task")
    if request.method == 'POST':
        serializer = Task_serializer(task)
        return Response(serializer.data)

# TO DO 8 GET ALL USER
@api_view(['GET'])
def GET_ALL_USER(request):
    if request.method == 'GET':
        list_user = User.objects.all() 
        serializer = UserSerializer(list_user, many = True)
        return Response(serializer.data)

# TO DO 9 ASSIGN-TO-DO
@api_view(['POST'])
def ASSIGN_TO_DO(request):
    if request.method == 'POST':
        user_login = request.user
        id = request.data["user"]
        user = User.objects.get(id=id)
        if (user_login.id == user.id) is False:
            serializer = Task_serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Success")
            else:
                serializer.errors
            return Response(serializer.data)
        else:
            return Response("Unable to assign task for yourself", status = status.HTTP_406_NOT_ACCEPTABLE)

# TO DO 10 GET-ALL-TASK-BY-USER
@api_view(['POST'])
def GET_ALL_TASK_USER(request):
    if request.method == 'POST':
        id = request.data["id"]
        task = Task.objects.filter(user=id)
        serializer = Task_serializer(task, many=True)
        return Response(serializer.data)


