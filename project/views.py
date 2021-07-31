from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from project.forms import ProjectItemsForm, ProjectForm
from project.models import ProjectItem, Project


class ProjectView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        project_form = ProjectForm()
        project = Project.objects.filter(user=self.request.user)
        context = {
            'project_form': project_form,
            'project': project,
        }
        return render(self.request, 'dashboard/project.html', context)

    def post(self, *args, **kwargs):
        project_form = ProjectForm(self.request.POST, self.request.FILES)
        if project_form.is_valid():
            form = project_form.save(commit=False)
            form.user = self.request.user
            form.save()
            messages.success(self.request, f'Your account has been updated')
            if self.request.user.username == self.request.POST.get('the_user'):
                print('the data', self.request.POST.get('the_user'))
                messages.success(self.request, f'{form.name} added to {form.project}')
                return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
            return redirect('dashboard:projectCreate')
        messages.warning(self.request, f'{project_form.errors}')
        return redirect('dashboard:projectCreate')


class ProjectItemsView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        project_items_form = ProjectItemsForm()
        project_items = ProjectItem.objects.filter(user=self.request.user)
        project = Project.objects.filter(user=self.request.user)
        context = {
            'project_items_form': project_items_form,
            'project_items': project_items,
            'project': project,
        }
        return render(self.request, 'dashboard/projectItems.html', context)

    def post(self, *args, **kwargs):
        project_items_form = ProjectItemsForm(self.request.POST, self.request.FILES)
        print('the requested items', self.request.POST)
        print('the requested items', self.request.FILES)
        project_id = self.request.POST.get('project')
        if project_id:
            project = Project.objects.filter(id=project_id, user=self.request.user).first()
            if project:
                project_items_form.project = project
                if project_items_form.is_valid():
                    form = project_items_form.save(commit=False)
                    form.user = self.request.user
                    form.project = project
                    form.save()
                    print('the form was valid', form)
                    messages.success(self.request, f'Your account has been updated')
                    if self.request.user.username == self.request.POST.get('the_user'):
                        print('the data', self.request.POST.get('the_user'))
                        messages.success(self.request, f'{form.name} added to {form.project}')
                        return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
                    return redirect('dashboard:projectItemsCreate')
        messages.warning(self.request, f'{project_items_form.errors}')
        return redirect('dashboard:projectItemsCreate')


@login_required()
def project_update_view(request):
    project_form = ProjectItemsForm(request.POST, request.FILES)
    print('the post files', request.POST)
    print('the  files', request.FILES.get('image'))
    project = Project.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if project:
        project.name = project_form['name'].value()
        if request.POST.get('image') != None:
            project_form.image = request.POST.get('image')
            project.image = project_form.image
        project.description = project_form['description'].value()
        if project_form.is_valid():
            project.save()
            print('the image', project.image)
            messages.success(request, f'{project.name} has being updated ')
            return redirect('dashboard:projectCreate')
    messages.warning(request, f'{project_form.errors}')
    return redirect('dashboard:projectCreate')


@login_required()
def project_items_update_view(request):
    project_item_form = ProjectItemsForm(request.POST, request.FILES)
    print('the post files', request.POST)
    project_item = ProjectItem.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if project_item:
        project_item.name = project_item_form['name'].value()
        if request.POST.get('image') != None:
            project_item.image = project_item_form['image'].value()
        project_item.description = project_item_form['description'].value()
        project_item.tag = project_item_form['tag'].value()
        if project_item_form.is_valid():
            project_item.save()
            messages.success(request, f'{project_item.name} has being updated ')
            return redirect('dashboard:projectItemsCreate')
    messages.warning(request, f'{project_item_form.errors}')
    return redirect('dashboard:projectItemsCreate')


@login_required()
def project_delete_view(request):
    form = request.POST.get('id')
    print('form', form)
    if form:
        project = Project.objects.filter(id=form, user=request.user).first()
        if project:
            print('project', project)
            project.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('dashboard:projectCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('dashboard:projectCreate')


@login_required()
def project_item_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        project_item = ProjectItem.objects.filter(id=form, user=request.user).first()
        if project_item:
            project_item.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('dashboard:projectItemsCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('dashboard:projectItemsCreate')
