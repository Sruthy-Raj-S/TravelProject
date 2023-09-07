from django.contrib import admin
from . models import People

# Register your models here.
from . models import Place
admin.site.register(Place)


admin.site.register(People)