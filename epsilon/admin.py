from django.contrib import admin
from .models import Question,Score,Display,Profile
# Register your models here.
admin.site.register(Question)
admin.site.register(Score)
admin.site.register(Display)
admin.site.register(Profile)