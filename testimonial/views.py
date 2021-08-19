from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from testimonial.forms import TestimonialForm
from testimonial.models import Testimonial


@login_required()
def testimonial_delete_view(request):
    form = request.POST.get('id')
    if form:
        skill = Testimonial.objects.filter(id=form, user=request.user).first()
        if skill:
            skill.delete()
            messages.success(request, 'the item has being deleted')
            return redirect('testimonial:testimonialCreate')
    messages.warning(request, 'There was an error processing your request')
    return redirect('testimonial:testimonialCreate')


@login_required()
def testimonail_update_view(request):
    test_form = TestimonialForm(request.POST, request.FILES)
    print('the post files', request.POST)
    test = Testimonial.objects.filter(id=request.POST.get('id'), user=request.user).first()
    if test:
        test.client_name = test_form['client_name'].value()
        if request.FILES.get('image') != None:
            test.image = request.FILES.get('image')
        test.url = test_form['url'].value()
        test.detail = test_form['detail'].value()
        test.save()
        messages.success(request, f'{test.client_name} has being updated ')
        return redirect('testimonial:testimonialCreate')
    messages.warning(request, f'There was an error updating the reviews ')
    return redirect('testimonial:testimonialCreate')



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
            return redirect('testimonial:testimonialCreate')
        messages.warning(self.request, f'{testimonial_form.errors}')
        return redirect('testimonial:testimonialCreate')


