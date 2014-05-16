from django import forms
from blog.models import Article
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title','url',  'tags', 'blurb', 'image' )
	tags = forms.CharField(max_length=100, required=False)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')