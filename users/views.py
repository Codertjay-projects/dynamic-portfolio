from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .forms import ContactAdminForm, ContactUserForm
from .models import User, ContactUser, ContactAdmin
from django.core.mail import send_mail


class ContactUserView(APIView):

    def post(self, *args, **kwargs):
        contact_name = self.request.data.get('contact_name')
        contact_email = self.request.data.get('contact_email')
        contact_subject = self.request.data.get('contact_subject')
        contact_message = self.request.data.get('contact_message')
        to_email_ = self.request.data.get('to_email')
        form = ContactUserForm(self.request.data)
        if form.is_valid():
            to_email = User.objects.filter(email=to_email_).first()
            if not to_email:
                return Response(status=HTTP_400_BAD_REQUEST)
            template = get_template('main/contact.txt')
            contact = ContactUser(contact_name=contact_name,
                                  contact_email=contact_email,
                                  contact_subject=contact_subject,
                                  contact_message=contact_message,
                                  to_email=to_email)
            contact.save()
            context = {
                'contact_name': self.request.data.get('name'),
                'contact_email': self.request.data.get('from_email'),
                'contact_subject': self.request.data.get('subject'),
                'contact_message': self.request.data.get('message'),
                'to_email': self.request.data.get('to_email')
            }
            content = template.render(context)
            if context:
                send_mail(
                    context.contact_subject,
                    content,
                    settings.EMAIL_HOST_USER,
                    [to_email],
                    fail_silently=True,
                )
                return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)


def contactAdminView(request):
    form = ContactAdminForm(request.POST)
    contact_name = form['contact_name'].value()
    contact_email = form['contact_email'].value()
    contact_subject = form['contact_subject'].value()
    contact_message = form['contact_message'].value()
    if form.is_valid():
        template = get_template('main/contact_admin.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'contact_subject': contact_subject,
            'contact_message': contact_message
        }
        print('the for is valid')
        content = template.render(context)
        if context:
            print('sent the message')
            send_mail(
                contact_subject,
                content,
                settings.EMAIL_HOST_USER,
                ['favourtjay@gmail.com'],
                fail_silently=True,
            )
        messages.success(request, 'Your message has being sent we would be in touch with you later ')
        print('the succes message,',
              messages.success(request, 'Your message has being sent we would be in touch with you later '))
        return redirect('portfolio:home')
    messages.warning(request,
                     'There was an error trying to send this message please fill the form an try again ')
    return redirect('portfolio:home')
