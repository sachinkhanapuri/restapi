
from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_info,name='student_info'),
    path('student_detail/<int:pk>/',views.student_detail,name='student_detail'),
    path('show_detail/',views.show_detail,name='show_detail'),
]
