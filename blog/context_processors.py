from .models import Post


def add_variable_to_context(request):
    latest_posts = Post.objects.all()
    older_posts = Post.objects.all().order_by('-id')
    if Post.objects.count() > 3:
        latest_posts = Post.objects.all()[3]
    if Post.objects.count() > 3:
        older_posts = Post.objects.all()[3].order_by(-id)
    about_website = "Dynamic portfolio is all about crating portfolio " \
                    "website for individual with low or no cost We love the web and care deeply for how users interact with a digital product. We power " \
                    "" \
                    "businesses and individuals to create better looking web projects around the world"

    return {
        'testme': "hello world",
        'latest_posts': latest_posts,
        'older_posts': older_posts,
        'about_website': about_website,
    }
