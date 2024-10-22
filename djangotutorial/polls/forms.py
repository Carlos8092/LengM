from django import forms

from .models import Question, Choice  # El punto es importante si está en la misma carpeta

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes']  # No incluyas 'question', la asignamos en la vista
