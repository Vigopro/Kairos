from django.shortcuts import render
from django.http import HttpResponse
from page.models import Category, Good
from django.http import Http404

def index(request, cat_id):
	if cat_id == None:
		cat = Category.objects.first()
	else:
		cat = Category.objects.get(cat_id)
	goods = Good.objects.filter(category = cat).order_by("name")
	s = "Категория: " + cat.name + "<br><br>"
	for good in goods:
		s = s + "(" + str(good.pk) + ") " + good.name + "<br>"
	return HttpResponse(s) 

def good(request, good_id):
	try:
		good = Good.objects.get(pk = good_id)
	except Good.DoesNotExist:
		raise Http404("Страница не найдена ухахаха!")
	s = good.name + "<br><br>" + good.category.name + "<br><br>" + good.description 
	if not good.in_stock:
		s = s + "<br><br>" + "Нет в наличии!"
	return HttpResponse(s)
