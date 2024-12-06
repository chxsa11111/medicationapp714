#from django.contrib import admin
from django.urls import path,include
from todo.views import TodoList,TodoDetail,TodoCreate,TodoDelete,TodoUpdate,ImageUploadView,VaccinationTodoList,VaccinationTodoDetail,VaccinationTodoCreate,VaccinationTodoDelete,VaccinationTodoUpdate

app_name = 'todo'

urlpatterns = [
    path('list/', TodoList.as_view(),name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(),name='detail'),
    path('create/', TodoCreate.as_view(),name='create'),
    path('delete/<int:pk>',TodoDelete.as_view(),name='delete'),
    path('update/<int:pk>',TodoUpdate.as_view(),name='update'),
    path('image_upload/', ImageUploadView.as_view(), name='image_upload'),
    path('vaccinationlist/', VaccinationTodoList.as_view(),name='vaccinationlist'),
    path('vaccinationdetail/<int:pk>', VaccinationTodoDetail.as_view(),name='vaccinationdetail'),
    path('vaccinationcreate/', VaccinationTodoCreate.as_view(),name='vaccinationcreate'),
    path('vaccinationdelete/<int:pk>',VaccinationTodoDelete.as_view(),name='vaccinationdelete'),
    path('vaccinationupdate/<int:pk>',VaccinationTodoUpdate.as_view(),name='vaccinationupdate'),
]