from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from resume.forms import ResumeForm
from resume.models import Resume


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
            return redirect('resume:resumeCreate')
        messages.warning(self.request, f'{resume_form.errors}')
        return redirect('resume:resumeCreate')

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
        return redirect('resume:resumeCreate')
    messages.warning(request, f'There was an error updating the resume {resume_form.errors} ')
    return redirect('resume:resumeCreate')



@login_required()
def resume_delete_view(request):
    form = request.POST.get('id')
    print('fotm', form)
    if form:
        resume = Resume.objects.filter(id=form, user=request.user).first()
        if resume:
            resume.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('resume:resumeCreate')
    messages.warning(request, 'There was an error processing your request')
    return redirect('resume:resumeCreate')
