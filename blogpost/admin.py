from django.contrib import admin

# Register your models here.
from .models import Blog, Category, Tag

admin.site.register([Blog, Category, Tag])