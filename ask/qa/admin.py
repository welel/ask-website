from django.contrib import admin

from qa.models import Question, Answer


admin.site.register(Question, admin.ModelAdmin)
admin.site.register(Answer, admin.ModelAdmin)
