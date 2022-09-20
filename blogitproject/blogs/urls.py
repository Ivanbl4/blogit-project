from django.urls import path
from blogs import views

urlpatterns = [
    path('<slug:author>/<slug:slug>/view', views.single_blog, name='single_blog'),
]

