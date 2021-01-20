from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone



# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name = "Admin")
    title = models.CharField(max_length=200, verbose_name="Baslik")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now = True, verbose_name="Olusturma Tarihi")
    article_image = models.FileField(blank = True, null = True, verbose_name="Makaleye Fotoqraf Ekle")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
    
