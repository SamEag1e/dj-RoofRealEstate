from django.shortcuts import render, HttpResponse

from .models import Post


def all_blogs(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(
        request, "blog/all_posts.html", context={"all_posts": all_posts}
    )


def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/each_post.html", context={"post": post})
