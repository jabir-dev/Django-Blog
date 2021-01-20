from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('create/', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addArticle, name="addArticle"),
    path('article/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.updateArticle, name="update"),
    path('delete/<int:id>', views.deletArticle, name="delete"),
    path('', views.articles, name="articles"),
]
