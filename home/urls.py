from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    
   
    path('login',views.loginUser,name='loginUser'),
    path('',views.dashboard,name='dashboard'),
    path('register',views.register,name='register'),
    path('validation',views.validation,name="validation"),
    path('addEmp',views.addEmp,name='addEmp'),
    path('load_subDept',views.load_subDept,name='load_subDept'),
    path('Update_info',views.Update_info,name='Update_info'),
    path('load_emp',views.load_emp,name='load_emp'),
    path('getInfo',views.getInfo,name='getInfo'),
    path('view_allEmp',views.view_allEmp,name='view_allEmp'),
    path('detail_view/<str:pk>/', views.detail_view, name='detail_view'),
    path('take_Attendance', views.take_Attendance, name='take_Attendance'),
    path('submibt_Attendance', views.submibt_Attendance, name='submibt_Attendance'),
    path('getDataForUpdate', views.getDataForUpdate, name='getDataForUpdate'),
    path('UpdateEmpStatus', views.UpdateEmpStatus, name='UpdateEmpStatus'),
    path('render_pdf_view/<str:pk>/', views.render_pdf_view, name='render_pdf_view'),
    path('historyOfAttendance', views.historyOfAttendance, name='historyOfAttendance'),
    path('logoutUser', views.logoutUser, name='logoutUser'),

]

