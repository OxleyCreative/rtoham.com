from home.models import Article
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    sectionQuery = Article.objects.filter(
        slug__in=['homepage-section-' + str(x) for x in range(1,4)])
    sections = []
    for article in sectionQuery:
        sections.append(article)
    return render_to_response("home/index.html",
                              {"currentpage": "home",
                               "sections": sections})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('home/detail.html', {'article': article})
