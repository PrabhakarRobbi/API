
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/',views.student_list,name='student'),
    path('student/<int:pk>',views.student_detail,name='detail')
    ]