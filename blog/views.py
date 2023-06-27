from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': "Kamil",
        'title': "Blog post 1",
        'content': "Post content 1",
        'post_date': "June 26, 2023"
    },
    {
        'author': "Laura",
        'title': "Blog post 2",
        'content': "Post content 2",
        'post_date': "June 27, 2023"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})