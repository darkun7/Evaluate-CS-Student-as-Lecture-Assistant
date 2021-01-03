from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Lab)
admin.site.register(Training)
admin.site.register(Attribute)
admin.site.register(TrainingValue)
