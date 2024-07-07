from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Article


def legacy_view(request):
    articles = Article.objects.all()
    return render(request, 'legacy.html', {'articles': articles})
