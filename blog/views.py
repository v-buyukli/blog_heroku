from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from blog.services import get_blogs


def index(request):
    blogs = get_blogs()
    context = {
        "blogs": blogs,
    }
    return render(request, "index.html", context)
