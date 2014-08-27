from django.contrib import admin

# Register your models here.
from .models import Questions

class QuestionsDataAdmin(admin.ModelAdmin):
    class Meta:
        model = Questions

admin.site.register(Questions, QuestionsDataAdmin)
