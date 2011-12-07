import math
import sys
from products.models import Product
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return product_list(request, '')

def product_list(request, category_string):
    NUM_PER_PAGE = 25
    PRODUCT_CATEGORIES = [x[0] for x in Product.CATEGORY_CHOICES]
    
    category_strings = [x.upper() for x in category_string.split(',')]

    if len(category_strings) == 1 and category_strings[0] == '':
        category_strings = PRODUCT_CATEGORIES

    # If there is more than one category, then we need to limit
    # the number of products from each category.
    if len(category_strings) > 1:
        limit = math.ceil(NUM_PER_PAGE / len(category_strings))
    else:
        limit = sys.maxint
        
    categories = {}
    for category in category_strings:
        categories[category] = Product.objects.select_related(
            'image').filter(category = category)[:limit]
    
    return render_to_response(
        'products/list.html',
        {'categories': categories,
         'category_strings': category_strings,
         'currentpage': 'products'})

def product(request, slug):
    product = get_object_or_404(Product.objects.select_related(
            'image'), slug = slug)
    return render_to_response(
        'products/product.html',
        {'product': product})
