from home.models import Article
from products.models import Product
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    sectionQuery = Article.objects.filter(
        slug__in=['homepage-section-' + str(x) for x in range(1,4)]
    ).order_by('slug')
    sections = [article for article in sectionQuery]

    equipmentQuery = Product.objects.select_related(
        "image"
    ).filter(
        category="USED_EQUIPMENT"
    ).order_by("-modified_at")[:5]
    units = [unit for unit in equipmentQuery]

    articlesQuery = Article.objects.filter(
        show_on_homepage = True
    ).order_by("-created_at")[:5]
    articles = [article for article in articlesQuery]
    return render_to_response("home/index.html",
                              {"currentpage": "home",
                               "sections": sections,
                               "units": units,
                               "articles": articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('home/detail.html', {'article': article})

def detail_with_slug(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    return render_to_response('home/detail.html', {'article': article})

def about_us(request):
    articles = Article.objects.filter(
        show_on_homepage = True,
        link = "").order_by("-created_at")[:3]
    article = articles[0] if len(articles) == 1 else None
    return render_to_response('home/about_us.html',
                              {'articles': articles,
                               'currentpage': 'about-us'})
