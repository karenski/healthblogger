from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Tag
from blog.forms import ArticleForm

# home page / index page with the 20 most recent articles
def index(request):
	articles = Article.objects.all()[:20]
	topic_tags, other_tags = get_tag_lists()
	form = ArticleForm()
	context = {
		'articles': articles,
		'topic_tags': topic_tags,
		'other_tags': other_tags,
		'form': form,
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

