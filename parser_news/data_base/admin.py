from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Title, Url, News

admin.site.register(Title)
admin.site.register(Url)
admin.site.register(News)