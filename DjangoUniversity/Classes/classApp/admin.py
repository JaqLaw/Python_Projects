from django.contrib import admin
from .models import djangoClasses  #import the model you made

# register the model
admin.site.register(djangoClasses)
