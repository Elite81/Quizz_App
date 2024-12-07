from django.contrib import admin
from . models import Quiz, Questions, Answer, User
# Register your models here.



class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions)
admin.site.register(Answer)
