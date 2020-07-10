from django.shortcuts import render
from django.views import generic
from .models import Article

def index(request):
	context = {}
	return render(request, 'index.html', context=context)


def articles_for_field(request, field):
	articles = Article.objects.filter(status=1, field=field).order_by('-created_on')

	templates = {'phys': 'physics.html',
				 'math': 'math.html',
				 'prog': 'programming.html'}
	context={'articles': articles}


	return render(request, templates[field], context=context)



class ArticleDetail(generic.DetailView):
	model = Article
	template_name = "article_detail.html"
