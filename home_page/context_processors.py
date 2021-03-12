from blog.models import Post
from .models import HomePageService, HomePageTestimonial
from _profile.models import PortfolioTemplate, TagChoice
from membership.models import Membership
from django.conf import settings

paystack_public_key = settings.PAYSTACK_PUBLIC_KEY

def add_variable_to_context(request):
    latest_posts = Post.objects.all()


    Free = Membership.objects.get_membership_type(membership_type='Free')
    Standard = Membership.objects.get_membership_type(membership_type='Standard')
    Premium = Membership.objects.get_membership_type(membership_type='Premium')
    Professional = Membership.objects.get_membership_type(membership_type='Professional')
    service = HomePageService.objects.all()
    testimonial = HomePageTestimonial.objects.all()
    portfolio_template = PortfolioTemplate.objects.all()
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
        'instagram_url': 'https://instagram.com/',
        'twitter_url': 'https://twitter.com/',
        'facebook_url': 'https://instagram.com/',
        'email': 'portfolio@gmail.com',
        'phone_number': '1234567890',
        'service': service,
        'home_page_testimonial': testimonial,
        'portfolio_template': portfolio_template,
        'website_name': 'Pcreator',
        'tag_choice': TagChoice,
        'Free': Free,
        'Standard': Standard,
        'Premium': Premium,
        'Professional': Professional,
        'paystack_public_key': paystack_public_key,
    }
