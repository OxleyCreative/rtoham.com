from home.models import Article
from django.shortcuts import render_to_response

def index(request):
    top_articles = Article.objects.all()[:5]
    return render_to_response("home/index.html",
                              {"top_articles": top_articles})

