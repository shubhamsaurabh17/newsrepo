from django import forms
from TestApp.models import Comment,Feedback
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=("name","email","body")


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
