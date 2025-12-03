from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Post


def post_list(request):
    """Display all posts."""
    posts = Post.objects.all().order_by("id")
    return render(request, "books/post_list.html", {"posts": posts})


def post_create(request):
    """Show a form to add a new post and process form submissions."""
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")

        if title and author:
            Post.objects.create(
                title=title,
                author=author,
            )
            return redirect(reverse("post_list"))

    return render(request, "books/post_form.html")


def post_update(request, id):
    """Show a form to edit an existing post and save changes."""
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")

        if title and author:
            post.title = title
            post.author = author
            post.save()
            return redirect(reverse("post_list"))

    return render(request, "books/post_form.html", {"post": post})


def post_delete(request, id):
    """Show a confirmation page and delete a post when confirmed."""
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.delete()
        return redirect(reverse("post_list"))

    return render(request, "books/post_confirm_delete.html", {"post": post})

