from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Tag
from blog.forms import ArticleForm
import urllib

# home page / index page with the 20 most recent articles
def index(request):
	articles = Article.objects.all()[:20]
	topic_tags, other_tags = get_tag_lists()
	context = {
		'articles': articles,
		'topic_tags': topic_tags,
		'other_tags': other_tags,
	}

	return render(request, 'index.html', context)

# tag page with relevant tagged articles
def tag(request, tag_name):
	tag_clean = tag_name.replace("_"," ")
	tag = get_object_or_404(Tag, name=tag_name)
	articles = tag.articles.all()
	topic_tags, other_tags = get_tag_lists()

	context = {
		'tag' : tag,
		'articles': articles,
		'title': tag_clean,
		'topic_tags': topic_tags,
		'other_tags': other_tags,
	}
	return render(request, 'tag.html', context)

# list of tags for the sidebar
def get_tag_lists():
	topic_tags = Tag.objects.filter(topic_tag=True)
	other_tags = Tag.objects.filter(topic_tag=False)

	return topic_tags, other_tags

# add article page with form to add an article

def add_article(request):
	# context = RequestContext(request)

	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			new_article = form.save()
			raw_tags = form.cleaned_data['tags'].split(',')
			if raw_tags:
				for raw_tag in raw_tags:
					raw_tag = raw_tag.strip().replace(' ', '_').lower()
					tag_name = urllib.quote(raw_tag)
					tag, created = Tag.objects.get_or_create(name=tag_name)
					tag.save()
					tag.articles.add(new_article)
			return redirect(index)
		else:
			print form.errors
	else:
		form = ArticleForm()

	context = {
		'form': form
	}

	return render(request, 'add_article.html', context)	
