from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from skill.forms import SkillsForm
from skill.models import Skill


class UserSkillCreate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        skill_form = SkillsForm()
        skills = Skill.objects.filter(user=self.request.user)
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
            return redirect('dashboard:skillCreate')
        messages.warning(self.request, f'{skill_form.errors}')
        return redirect('dashboard:skillCreate')


@login_required()
def skill_update_view(request):
    skill_form = SkillsForm(request.POST, request.FILES)
    print('the psot files', request.POST)
    skill = Skill.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if skill:
        print('this is the skill name', skill_form['name'].value())
        print('this is the skill descrip', skill_form['description'].value())
        print('this is the skill percent', skill_form['percent'].value())
        skill.name = skill_form['name'].value()
        if skill_form['icon'].value() != None:
            skill.icon = skill_form['icon'].value()
        skill.description = skill_form['description'].value()
        skill.percent = skill_form['percent'].value()
        if skill_form.is_valid():
            skill.save()
        messages.success(request, f'{skill.name} has being updated ')
    else:
        messages.warning(request, f'There was an error updating the skill')
    return redirect('dashboard:skillCreate')


@login_required()
def skill_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        skill = Skill.objects.filter(id=form, user=request.user).first()
        if skill:
            skill.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('dashboard:skillCreate')
    messages.warning(request, 'There was an error proccessing your request')
    return redirect('dashboard:skillCreate')
