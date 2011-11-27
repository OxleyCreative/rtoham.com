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
    return render_to_response("home/index.html",
                              {"currentpage": "home",
                               "sections": sections,
                               "units": units})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('home/detail.html', {'article': article})
