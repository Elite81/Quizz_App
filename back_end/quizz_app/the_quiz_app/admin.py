from django.contrib import admin
from . models import Quiz, Questions, Answer, User
# Register your models here.


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [ 'answer_text', 'is_right']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class QuestionsAdmin(admin.ModelAdmin):
    fields = ['title', 'quiz', 'created_at']
    list_display = ['title', 'quiz', 'created_at']
    readonly_fields = ['created_at']

    inlines = [AnswerInlineModel]

class AnswersAdmin(admin.ModelAdmin):
    fields = ['question', 'answer_text', 'is_right', 'created_at']
    list_display = ['question', 'answer_text', 'is_right', 'created_at']
    readonly_fields = ['created_at']
    
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answer, AnswersAdmin)
