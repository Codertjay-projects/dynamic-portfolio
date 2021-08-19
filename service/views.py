from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from service.forms import ServiceForm
from service.models import Service


class UserServiceCreate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        service_form = ServiceForm()
        service = Service.objects.filter(user=self.request.user)
        context = {
            'service': service,
            'service_form': service_form,
        }
        return render(self.request, 'dashboard/service.html', context)

    def post(self, *args, **kwargs):
        service_form = ServiceForm(self.request.POST, self.request.FILES)
        print('this is the post files', self.request.POST.get('the_user'))
        if service_form.is_valid():
            form = service_form.save(commit=False)
            form.user = self.request.user
            form.save()
            print('the form was valid')
            messages.success(self.request, f'your skill has being added ')
            if self.request.user.username == self.request.POST.get('the_user'):
                print('the data', self.request.POST.get('the_user'))
                return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
            return redirect('service:serviceCreate')
        messages.warning(self.request, f'{service_form.errors}')
        return redirect('service:serviceCreate')


@login_required()
def services_update_view(request):
    service_form = ServiceForm(request.POST, request.FILES)
    print('the post files', request.POST)
    print('the  files', request.FILES.get('image'))
    service = Service.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if service:
        service.name = service_form['name'].value()
        if service_form['image'].value() != None:
            service.image = service_form['image'].value()
        service.description = service_form['description'].value()
        service.save()
        messages.success(request, f'{service.name} has being updated ')
        return redirect('service:serviceUpdate')
    messages.warning(request, f'There was an error updating the service ')
    return redirect('service:serviceUpdate')


@login_required()
def service_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        service = Service.objects.filter(id=form, user=request.user).first()
        if service:
            service.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('dashboard:serviceCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('dashboard:serviceCreate')
