from django.urls import path
from .views import HomePageView, ServiceView,FaqView,AboutView,TestimonialView,ContactView,PricingView

app_name = 'home_page'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('#/service/', ServiceView.as_view(), name='service'),
    path('#/faq/', FaqView.as_view(), name='faq'),
    path('#/about/', AboutView.as_view(), name='about'),
    path('#/testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('#/contact/', ContactView.as_view(), name='contact'),
    path('#/pricing/', PricingView.as_view(), name='price'),
]
