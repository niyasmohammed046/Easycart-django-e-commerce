# by using this we can call the category we want

from .models import Category  

def menu_links(request):   # menu_links is user defined ()
    links = Category.objects.all()
    return dict(links=links)