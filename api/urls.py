from django.urls import path
from .views import *
app_name = 'api'
urlpatterns = [
    path('api1_singup',SING_UP, name="url_api1"),
    path('api2_login',SING_IN, name="url_api2"),
    path('api3_add-todo',ADD_TO_DO, name="url_api3"),
    path('api4+5_update-remove_task/<int:task_id>',Revise, name="url_apii"),
    path('api6_get-all-to-do',GET_ALL_TO_DO, name="url_api6"),
    path('api7_get-todo-by-id',GET_TO_DO_BY_ID, name="url_api7"),
    path('api8_get-all-user',GET_ALL_USER, name="url_api8"),
    path('api9_assign_todo',ASSIGN_TO_DO, name="url_api9"),
    path('api10_get-all-task-by-user',GET_ALL_TASK_USER, name="url_api10"),
]
