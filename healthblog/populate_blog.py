import os

def populate():


def add_article(title, url, blurb, image, views=0):
	p = Article.objects.get_or_create(title=title, url=url, blurb=blurb, image=image, views=views)
	return p

def add_tag(articles, name, topic_tag):
	t = Tag.objects.get_or_create(articles=articles, name=name, topic_tag=topic_tag)
	return t

if __name__ == '__main__':
	print "Starting blog population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthblog.settings')
	from blog.models import Article, Tag
	populate()