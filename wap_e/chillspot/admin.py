from django.contrib import admin

# Register your models here.
from .models import Top_spots, Popular, Content

admin.site.register(Top_spots)
admin.site.register(Popular)
admin.site.register(Content)
