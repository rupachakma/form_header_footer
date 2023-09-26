
from django.contrib import admin
from django.urls import path

from herapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('r/', views.r),
    path('', views.dex),
    path('p/', views.port),
    path('f/', views.form),
]