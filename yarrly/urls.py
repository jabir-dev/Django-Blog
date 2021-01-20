from django.contrib import admin
from django.urls import path, include
from django.conf import settings #!Media import
from django.conf.urls.static import static #!Media import

from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('articles/', include("article.urls")),
    path('user/', include("user.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#!MEdia ucun

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #!MEdia ucun
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#!MEdia ucun 
