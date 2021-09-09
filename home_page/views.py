from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# Create your views here.
from django.template.loader import get_template
from django.views.generic.base import View

from Portfolio.settings import EMAIL_HOST_USER
from home_page.forms import SubscribeForm
from users.forms import ContactAdminForm
from users.models import ContactAdmin


class HomePageView(View):

    def get(self, request):
        return render(request, 'HomePage/index.html')


class ServiceView(View):

    def get(self, request):
        return render(request, 'HomePage/service_rendered/services.html')


class OfferView(View):
    def get(self, request):
        return render(request, 'HomePage/offer.html')


class FaqView(View):

    def get(self, request):
        return render(request, 'HomePage/faq.html')


class AboutView(View):

    def get(self, request):
        return render(request, 'HomePage/about-us.html')


class PricingView(View):

    def get(self, request):
        return render(request, 'HomePage/pricing.html')


class TestimonialView(View):

    def get(self, request):
        return render(request, 'HomePage/testimonials.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'HomePage/contact.html')

    def post(self, request):
        form = ContactAdminForm(request.POST)
        contact = ContactAdmin(
            contact_name=form['contact_name'].value(),
            contact_email=form['contact_email'].value(),
            contact_subject=form['contact_subject'].value(),
            contact_message=form['contact_message'].value()
        )
        if form.is_valid():
            contact.save()
            template = get_template('EmailTemplates/contact_admin.txt')
            context = {
                'contact_name': contact.contact_name,
                'contact_email': contact.contact_email,
                'contact_subject': contact.contact_subject,
                'contact_message': contact.contact_message
            }
            print('the for is valid')
            content = template.render(context)
            if context:
                send_mail(
                    contact.contact_subject,
                    content,
                    contact.contact_email,
                    [EMAIL_HOST_USER],
                    fail_silently=True,
                )
                print('sent the message', content)
                messages.success(request, 'Your message has being sent we would be in touch with you later ')
                return redirect('home_page:contact')
        print('there was an error sending your message')
        return redirect('home_page:contact')


def subscribe_user(request):
    form = SubscribeForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Subscribed to our mailing list ')
    else:
        messages.info(request, 'There was an error subscribing to our mailing list ')
    return redirect('home_page:home')
