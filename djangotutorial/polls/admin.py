from django.contrib import admin
from .models import Question
from .models import Choices 

admin.site.register(Question)
admin.site.register(Choices)  