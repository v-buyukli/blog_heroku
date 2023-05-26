from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from blog.forms import BlogForm
from blog.services import get_blogs


def index(request):
    context = "Blogs page"
    return render(request, "index.html", {"context": context})


def get_blog(request):
    blogs = get_blogs()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_id = int(form.cleaned_data["blog_id"])
            return HttpResponseRedirect(reverse("blog_view", args=[blog_id]))
    else:
        form = BlogForm()
    context = {
        "form": form,
        "blogs": blogs,
    }
    return render(request, "blog.html", context)


def blog_view(request, blog_id):
    try:
        blog = get_blogs()[str(blog_id)]
    except KeyError:
        return HttpResponseRedirect(reverse("blog"))
    return render(request, "blog_view.html", {"blog": blog})
