from home.models import Article
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    top_articles = Article.objects.all()[:5]
    return render_to_response("home/index.html",
                              {"top_articles": top_articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('home/detail.html', {'article': article})
