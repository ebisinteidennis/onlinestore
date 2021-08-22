from .models import Comment
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)     
    
class ImageForm(forms.ModelForm):
    '''Form for the image model'''
    class Meta:
        model = Image
        fields = ('title', 'image')