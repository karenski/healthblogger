from django import forms
from blog.models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title','url',  'tags', 'blurb', 'image' )
	tags = forms.CharField(max_length=100, required=False)

