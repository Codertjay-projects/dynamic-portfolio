from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView
from django.views.generic.base import View

from portfolio_app.forms import ProjectForm, ProjectItemsForm
from portfolio_app.models import Project, ProjectItem
from users.models import User
from .models import (Layout,
                     Profile,
                     Testimonial,
                     Contact,
                     Skills, Service, Resume)

from .forms import (LayoutForm,
                    TestimonialForm,
                    SkillsForm,
                    ProfileForm, UserUpdateForm, ServiceForm, ResumeForm)


@login_required
def userDashboard(request, *args, **kwargs):
    layout = Layout.objects.filter(user=request.user)
    profile = Profile.objects.filter(user=request.user)
    testimonial = Testimonial.objects.filter(user=request.user)
    skills = Skills.objects.filter(user=request.user)
    context = {
        'layout': layout,
        'profile': profile,
        'testimonial': testimonial,
        'skills': skills,

        'layout_form': LayoutForm,
        'profile_form': ProfileForm,
        'testimonial_form': TestimonialForm,
        'skills_form': SkillsForm,
    }
    print('thue prifle pics', request.user.profile.profilePicsImageURL)
    return render(request, 'dashboard/dashboard.html', context)


class UserProfileUpdate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        profile_form = ProfileForm(self.request.FILES or None, instance=self.request.user.profile)
        profile = Profile.objects.filter(user=self.request.user).first()
        context = {
            'profile': profile,
            'profile_form': profile_form,
        }
        return render(self.request, 'dashboard/profile.html', context)

    def post(self, *args, **kwargs):
        p_form = ProfileForm(self.request.POST,
                             self.request.FILES,
                             instance=self.request.user.profile)
        if p_form.is_valid():
            p_form.save()
            print('the form was valid')
            messages.success(self.request, f'Your account has been updated')
            if self.request.user.username == self.request.POST.get('the_user'):
                print('the data', self.request.POST.get('the_user'))
                return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
            return redirect('profile:profileUpdate')

        messages.warning(self.request, f'{p_form.errors}')
        return redirect('profile:profileUpdate')


class UserNameUpdate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        _instance = get_object_or_404(User, username=self.request.user.username)
        instance_ = {
            'username': _instance.username,
            'first_name': _instance.first_name,
            'last_name': _instance.last_name,
            'email': _instance.email,
        }
        user_form = UserUpdateForm(self.request.FILES or None, initial=instance_)
        profile = Profile.objects.filter(user=self.request.user).first()
        context = {
            'profile': profile,
            'user_form': user_form,
        }
        return render(self.request, 'dashboard/userName.html', context)

    def post(self, *args, **kwargs):
        u_form = UserUpdateForm(self.request.POST)
        user = self.request.user
        _user = User.objects.filter(username=u_form['username'].value()).first()

        if _user == self.request.user:
            user.username = u_form['username'].value()
            user.first_name = u_form['first_name'].value()
            user.last_name = u_form['last_name'].value()
            user.email = u_form['email'].value()
            user.save()
            messages.success(self.request, "Your account has being updated")
            if self.request.user.username == self.request.POST.get('the_user'):
                print('the data', self.request.POST.get('the_user'))
                return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
        elif not _user:
            user.username = u_form['username'].value()
            user.first_name = u_form['first_name'].value()
            user.last_name = u_form['last_name'].value()
            user.email = u_form['email'].value()
            user.save()
            messages.success(self.request, "Your account has being updated")
            if self.request.user.username == self.request.POST.get('the_user'):
                print('the data', self.request.POST.get('the_user'))
                return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
        else:
            messages.warning(self.request, 'The username has already being taken')
        return redirect('profile:userUpdate')


class UserLayoutUpdate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        instance = get_object_or_404(Layout, user=self.request.user)
        layout_form = LayoutForm(self.request.FILES or None, instance=instance)
        context = {
            'layout': instance,
            'layout_form': layout_form,
        }
        return render(self.request, 'dashboard/layout.html', context)

    def post(self, *args, **kwargs):
        l_form = LayoutForm(self.request.POST,
                            self.request.FILES,
                            instance=self.request.user.layout)
        print('this is the post files', self.request.FILES)
        if l_form.is_valid():
            l_form.save()
            print('the form was valid')
            messages.success(self.request, f'Your account has been updated')
            if self.request.user.username == self.request.POST.get('the_user'):
                print('the data', self.request.POST.get('the_user'))
                return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
            return redirect('profile:layoutUpdate')
        messages.warning(self.request, f'{l_form.errors}')
        return redirect('profile:layoutUpdate')


class UserSkillCreate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        skill_form = SkillsForm()
        skills = Skills.objects.filter(user=self.request.user)
        context = {
            'skills': skills,
            'skill_form': skill_form,
        }
        return render(self.request, 'dashboard/skills.html', context)

    def post(self, *args, **kwargs):
        skill_form = SkillsForm(self.request.POST, self.request.FILES)
        print('this is the post files', self.request.POST.get('the_user'))
        if skill_form.is_valid():
            form = skill_form.save(commit=False)
            form.user = self.request.user
            form.save()
            print('the form was valid')
            messages.success(self.request, f'your skill has being added ')
            if self.request.user.username == self.request.POST.get('the_user'):
                print('the data', self.request.POST.get('the_user'))
                return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
            return redirect('profile:skillCreate')
        messages.warning(self.request, f'{skill_form.errors}')
        return redirect('profile:skillCreate')


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
            return redirect('profile:serviceCreate')
        messages.warning(self.request, f'{service_form.errors}')
        return redirect('profile:serviceCreate')


class UserTestimonialCreate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        testimonial_form = TestimonialForm()
        testimonial = Testimonial.objects.filter(user=self.request.user)
        context = {
            'testimonial': testimonial,
            'testimonial_form': testimonial_form,
        }
        return render(self.request, 'dashboard/testimonial.html', context)

    def post(self, *args, **kwargs):
        testimonial_form = TestimonialForm(self.request.POST, self.request.FILES)
        print('this is the post files', self.request.POST)
        if testimonial_form.is_valid():
            form = testimonial_form.save(commit=False)
            form.user = self.request.user
            # form.image = self.request.FILES.image
            print(self.request.POST.get('image'))
            form.save()
            print('the form was valid')
            messages.success(self.request, f'Your account has been updated')
            return redirect('profile:testimonialCreate')
        messages.warning(self.request, f'{testimonial_form.errors}')
        return redirect('profile:testimonialCreate')


class UserResumeCreate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        resume_form = ResumeForm()
        resume = Resume.objects.filter(user=self.request.user)
        context = {
            'resume': resume,
            'resume_form': resume_form,
        }
        return render(self.request, 'dashboard/resume.html', context)

    def post(self, *args, **kwargs):
        resume_form = ResumeForm(self.request.POST, self.request.FILES)
        print('this is the post files', self.request.POST)
        if resume_form.is_valid():
            form = resume_form.save(commit=False)
            form.user = self.request.user
            print(self.request.POST.get('image'))
            form.save()
            print('the form was valid')
            messages.success(self.request, f'Your account has been updated')
            return redirect('profile:resumeCreate')
        messages.warning(self.request, f'{resume_form.errors}')
        return redirect('profile:resumeCreate')


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
            return redirect('profile:profileUpdate')
        messages.warning(self.request, f'{project_form.errors}')
        return redirect('profile:projectCreate')


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
                    return redirect('profile:projectItemsCreate')
        messages.warning(self.request, f'{project_items_form.errors}')
        return redirect('profile:projectItemsCreate')


@login_required()
def testimonail_update_view(request):
    test_form = TestimonialForm(request.POST, request.FILES)
    print('the psot files', request.POST)
    test = Testimonial.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if test:
        test.client_name = test_form['client_name'].value()
        if request.FILES.get('image') != None:
            test.image = request.FILES.get('image')
        test.url = test_form['url'].value()
        test.detail = test_form['detail'].value()
        test.save()
        messages.success(request, f'{test.client_name} has being updated ')
        return redirect('profile:testimonialCreate')
    messages.warning(request, f'There was an error updating the reviews ')
    return redirect('profile:testimonialCreate')


@login_required()
def skill_update_view(request):
    skill_form = SkillsForm(request.POST, request.FILES)
    print('the psot files', request.POST)
    skill = Skills.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if skill:
        print('this is the skill name', skill_form['name'].value())
        print('this is the skill descrip', skill_form['description'].value())
        print('this is the skill percent', skill_form['percent'].value())
        skill.name = skill_form['name'].value()
        if  skill_form['icon'].value() != None:
            skill.icon = skill_form['icon'].value()
        skill.description = skill_form['description'].value()
        skill.percent = skill_form['percent'].value()
        skill.save()
        messages.success(request, f'{skill.name} has being updated ')
    else:
        messages.warning(request, f'There was an error updating the skill')
    return redirect('profile:skillCreate')


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
        return redirect('profile:serviceUpdate')
    messages.warning(request, f'There was an error updating the service ')
    return redirect('profile:serviceUpdate')


@login_required()
def resume_update_view(request):
    resume_form = ResumeForm(request.POST)
    print('the post files', request.POST)
    resume = Resume.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if resume:
        resume.name = resume_form['name'].value()
        resume.detail = resume_form['detail'].value()
        resume.start_date = resume_form['start_date'].value()
        resume.end_date = resume_form['end_date'].value()
        resume.save()
        messages.success(request, f'{resume.name} has being updated ')
        return redirect('profile:resumeCreate')
    messages.warning(request, f'There was an error updating the resume {resume_form.errors} ')
    return redirect('profile:resumeCreate')


@login_required()
def project_update_view(request):
    project_form = ProjectItemsForm(request.POST, request.FILES)
    print('the post files', request.POST)
    print('the  files', request.FILES.get('image'))
    project = Project.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if project:
        project.name = project_form['name'].value()
        if request.FILES.get('image') != None:
            project.image = request.FILES.get('image')
        project.description = project_form['description'].value()
        project.save()
        print('the image', project.image)
        messages.success(request, f'{project.name} has being updated ')
        return redirect('profile:projectCreate')
    messages.warning(request, f'There was an error updating the project ')
    return redirect('profile:projectCreate')


@login_required()
def project_items_update_view(request):
    project_item_form = ProjectItemsForm(request.POST, request.FILES)
    print('the post files', request.POST)
    project_item = ProjectItem.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if project_item:
        project_item.name = project_item_form['name'].value()
        if request.FILES.get('image') != None:
            project_item.image = project_item_form['image'].value()
        project_item.description = project_item_form['description'].value()
        project_item.tag = project_item_form['tag'].value()
        project_item.save()
        messages.success(request, f'{project_item.name} has being updated ')
        return redirect('profile:projectItemsCreate')
    messages.warning(request, f'There was an error updating the item   ')
    return redirect('profile:projectItemsCreate')


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
            return redirect('profile:projectCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('profile:projectCreate')


@login_required()
def project_item_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        project_item = ProjectItem.objects.filter(id=form, user=request.user).first()
        if project_item:
            project_item.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('profile:projectItemsCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('profile:projectItemsCreate')


@login_required()
def skill_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        skill = Skills.objects.filter(id=form, user=request.user).first()
        if skill:
            skill.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('profile:skillCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('profile:skillCreate')


@login_required()
def testimonial_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        skill = Testimonial.objects.filter(id=form, user=request.user).first()
        if skill:
            skill.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('profile:testimonialCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('profile:testimonialCreate')


@login_required()
def service_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        service = Service.objects.filter(id=form, user=request.user).first()
        if service:
            service.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('profile:serviceCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('profile:serviceCreate')


@login_required()
def resume_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        resume = Resume.objects.filter(id=form, user=request.user).first()
        if resume:
            resume.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('profile:resumeCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('profile:resumeCreate')
