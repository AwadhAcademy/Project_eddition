from django.contrib import admin

# Register your models here.
from .models import Carousel_Data
from .models import loogin_data
from .models import project_details

admin.site.register(Carousel_Data)
admin.site.register(loogin_data)
admin.site.register(project_details)