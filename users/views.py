from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from Portfolio.settings import EMAIL_HOST_USER
from .forms import ContactAdminForm, ContactUserForm
from .models import User, ContactUser, ContactAdmin
from django.core.mail import send_mail


class ContactUserView(APIView):

    def post(self, *args, **kwargs):
        form = ContactUserForm(self.request.data)
        to_email = User.objects.filter(email=form['to_email'].value()).first()
        host_url = self.request.data.get('url')
        print('these are the data', self.request.data)
        print('these are the data', host_url)
        print('the form error', form.errors)
        if not to_email:
            return Response(status=HTTP_400_BAD_REQUEST)
        if form.is_valid():
            print('the form was valid')
            template = get_template('main/contact.txt')
            contact = ContactUser(contact_name=form['contact_name'].value(),
                                  contact_email=form['contact_email'].value(),
                                  contact_subject=form['contact_subject'].value(),
                                  contact_message=form['contact_message'].value(),
                                  to_email=to_email)
            contact.save()
            context = {
                'contact_name': contact.contact_name,
                'contact_email': contact.contact_email,
                'contact_subject': contact.contact_subject,
                'contact_message': contact.contact_message,
                'to_email': contact.to_email
            }
            content = template.render(context)
            if context:
                send_mail(
                    contact.contact_subject,
                    content,
                    settings.EMAIL_HOST_USER,
                    [to_email],
                    fail_silently=False,
                )
                print('the message was sent')
                messages.success(self.request, 'Your messsage has  being sent')
                return Response(status=HTTP_201_CREATED)

        print('the message was not sent')
        messages.warning(self.request, 'There was an error sending your message')
        return Response(status=HTTP_400_BAD_REQUEST)


def contactAdminView(request):
    form = ContactAdminForm(request.POST)
    contact = ContactAdmin(
        contact_name=form['contact_name'].value(),
        contact_email=form['contact_name'].value(),
        contact_subject=form['contact_name'].value(),
        contact_message=form['contact_name'].value()
    )
    if form.is_valid():
        contact.save()
        template = get_template('main/contact_admin.txt')
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
                fail_silently=False,
            )
            print('sent the message',content)
            messages.success(request, 'Your message has being sent we would be in touch with you later ')
            return redirect('portfolio:home')
    print('there was an error sending your message')
    return redirect('portfolio:home')
