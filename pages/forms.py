from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from learn.models import Profile


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Email'}))

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2", "first_name", "last_name")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
			p = Profile(user=user ,user_name=user.username)
			p.save()
		return user