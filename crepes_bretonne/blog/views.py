from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from datetime import datetime
from django.shortcuts import render
from blog.models import Article


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article': article})
