from django.urls import path

from testimonial.views import testimonail_update_view, testimonial_delete_view, UserTestimonialCreate

app_name = 'testimonial'
urlpatterns = [

    path('testimonialUpdate/', testimonail_update_view, name='testimonialUpdate'),
    path('testimonialDelete/', testimonial_delete_view, name='testimonialDelete'),
    path('testimonialCreate/', UserTestimonialCreate.as_view(), name='testimonialCreate'),

]
