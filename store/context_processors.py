from .models import Category

def comman_data(request):
    categories = Category.objects.all()
    return {'categories' : categories}