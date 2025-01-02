from django.contrib import admin
from .models import Question

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','tematica','pregunta','respondida')
    list_filter = ('tematica','respondida')
    search_fields = ('pregunta','tematica')
    ordering = ('id',)