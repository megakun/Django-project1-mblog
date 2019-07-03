from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime
from django.http import HttpResponse
from .models import Post

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)