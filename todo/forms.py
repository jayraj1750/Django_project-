from django import forms
from todo.models import Contact, Todo

class TodoForms(forms.ModelForm):
    class Meta:
        model=Todo
        fields={"title","description","name"}

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"name","email","mobileno","message"}