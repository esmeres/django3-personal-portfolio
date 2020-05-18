from django.urls import path
from django.contrib import admin
from . import views
app_name = 'todo'



urlpatterns = [

    path("", views.todo_home, name="todo_home"),
    #authentication
    path('signup/', views.signupuser, name = 'signupuser'),
    path('logout/', views.logoutuser, name = 'logoutuser'),
    path('login/', views.loginuser, name = 'loginuser'),
        #todos
    path('current/', views.currenttodos, name = 'currenttodos'),
    path('create/', views.createtodo, name = 'createtodo'),
    path('todo/<int:todo_pk>', views.viewtodo, name = 'viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name = 'completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name = 'deletetodo'),
    path('completed/', views.completedtodos, name='completedtodos'),




]

