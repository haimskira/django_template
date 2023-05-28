from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('img/<pk>', views.student_Views.as_view()),
    path('img/', views.student_Views.as_view()),
    path('students/<pk>', views.student_Views.as_view()),
    path('students/', views.student_Views.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.student_Views.reg ,name="register"),
    # product url here
    path('img/<pk>', views.product_Views.as_view()),
    path('img/', views.product_Views.as_view()),
    path('product/<pk>', views.product_Views.as_view()),
    path('product/', views.product_Views.as_view()),
]
