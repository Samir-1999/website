from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView

from  .models import Tovar, Category

class CategoryGet:
    """Категории товаров"""
    def get_category(self):
        return Category.objects.all()

class TovarView(CategoryGet, View):
    '''Список товаров'''
    def get(self, request):
        tovar = Tovar.objects.all()
        latest_products = Tovar.objects.order_by("-id")[: 4]
        return render(request, "products/products_list.html", {"products_list": tovar, 'latest_products': latest_products,"categories": self.get_category()})

class TovarDetailView(CategoryGet, View):
    """Полное описание товара"""
    def get(self, request, pk):
        tovar = Tovar.objects.get(id = pk)
        return render(request, "products/products_detail.html", {"products_detail": tovar})

class Search(ListView):
    """Поиск товаров"""
    paginate_by = 3

    def get_queryset(self):
        return Tovar.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context

class FilterTovarView(CategoryGet, ListView):
    """Фильтр товаров"""
    def get_queryset(self):
        queryset = Tovar.objects.filter(category__in=self.request.GET.getList("category"))
        return queryset