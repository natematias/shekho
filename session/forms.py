from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import shekho.session.models

class SessionForm(ModelForm):
   #from http://www.chicagodjango.com/blog/django-form-snippets/
    def __init__(self, *args, **kwargs):
        super(SessionForm, self).__init__(*args, **kwargs)
        self.fields['rsvp_required'].required = False
        self.fields['has_cost'].required = False
        self.fields['preferred_date'].required = False

    class Meta:
        model = shekho.session.models.Session


class RegistrationForm(UserCreationForm):
	username = forms.CharField(max_length=30)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=75)
	
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email",)
	
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.username = self.cleaned_data["username"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user
