from django.http import HttpResponse
from django.shortcuts import render
from match.models import Match
from blog.models import Post
from django.core.paginator import Paginator

def index(request):
    indexPage = True
    page_title = 'TITLE'
    page_description = 'page_description'
    allMatches = Match.objects.filter(is_active=True)
    allPosts = Post.objects.filter(is_active=True)
    paginator = Paginator(allMatches, 1)
    data = []
    for i in paginator.page_range:
        data.append(paginator.get_page(i))
    print(data)
    nearestMatch = allMatches.order_by('-date')[0]
    return render(request, 'pages/index.html', locals())


def offer(request):
    page_title = 'TITLE'
    page_description = 'page_description'
    return render(request, 'pages/offer.html', locals())

def stadium(request):
    page_title = 'TITLE'
    page_description = 'page_description'
    return render(request, 'pages/stadium.html', locals())

def contact(request):
    page_title = 'TITLE'
    page_description = 'page_description'
    return render(request, 'pages/contacts.html', locals())

def matches(request):
    page_title = 'TITLE'
    page_description = 'page_description'
    allMatches = Match.objects.filter(is_active=True).order_by('-date')
    return render(request, 'pages/matches.html', locals())


def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: localhost.ru/\nSitemap: localhost.ru/sitemap.xml"

    return HttpResponse(robotsTxt, content_type="text/plain")
