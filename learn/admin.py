from django.contrib import admin
from .models import Question, Answer_list ,Images ,stats ,profile
# Register your models here.



admin.site.register(Question)
admin.site.register(Answer_list)
admin.site.register(Images)
admin.site.register(stats)
admin.site.register(profile)

