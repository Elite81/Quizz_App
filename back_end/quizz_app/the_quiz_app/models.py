from django.db import models
from django.utils.translation import gettext_lazy as _
# from autoslug import AutoSlugField
from django.contrib.auth.models import User


# Create your models here.

class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=526, verbose_name=_("Quiz Title"), default= _("New Quiz"))
    created_at = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=64, unique=True, allow_unicode=True)

    @property
    def question_count(self):
        return self.questions.count()
    
    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    def __str__(self):
        return self.title

class Questions(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    title = models.CharField( max_length=526, verbose_name=_("Quiz Title"), default= _("New Quiz"))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('Questions')
        verbose_name_plural = _("Questions")
        ordering = ['id']
    
    def __str__(self):
        return self.title
    

class Answer(models.Model):
    question = models.ForeignKey(Questions, related_name="answers", on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, null=True, blank=True)
    is_right = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('Answers')
        verbose_name_plural = _("Answers")
        ordering = ['id']
    
    def __str__(self):
        return self.answer_text
