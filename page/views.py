from django.shortcuts import render
from django.http import HttpResponse
from page.models import Category, Good
from django.http import Http404

def index(request, cat_id):
	cats = Category.objects.all().order_by("name")
	if cat_id == None:
		cat = Category.objects.first()
	else:
		cat = Category.objects.get(cat_id)
	goods = Good.objects.filter(category = cat).order_by("name")
	return render(request, "page/index.html", {"category": cat, "cats": cats, "goods":goods})

def good(request, good_id):
	cats = Category.objects.all().order_by("name")
	try:
		good = Good.objects.get(pk = good_id)
	except Good.DoesNotExist:
		raise Http404("Страница не найдена ухахаха!")
	return render(request, "page/good.html", {"cats": cats, "good": good})
