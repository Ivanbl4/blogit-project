from django.shortcuts import render
from profiles.models import Profile
from blogs.models import Blog


# Create your views here.
def single_blog(request, author, slug):
    profile = Profile.objects.get(user__username=author)
    blog = Blog.objects.get(author=profile, slug=slug)

    context = {
        'blog': blog,
        'profile': profile,
    }

    return render(request, 'blogs/single_blog.html', context=context)
