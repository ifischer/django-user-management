from django.urls import path
from django.contrib import admin
from user_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-call/', views.api_call, name='api-call')
]
