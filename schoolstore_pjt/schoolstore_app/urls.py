from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('logout/', views.user_logout, name='logout'),
    path('api/courses/<str:department_id>/', views.get_courses_for_department, name='get_courses_for_department'),
    path('submit_order/', views.submit_order, name='submit_order'),



]
