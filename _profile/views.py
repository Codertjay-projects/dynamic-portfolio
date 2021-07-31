from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from _profile.forms import UserUpdateForm, LayoutForm, ProfileForm
from _profile.models import Profile, Layout
from membership.models import UserMembershipSubscription
from portfolio_app.models import PortfolioTemplate
from users.models import User


def get_user_subscription(request):
    user_membsership = UserMembershipSubscription.objects.filter(user=request.user).first()
    if user_membsership:
        return user_membsership
    else:
        return None

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
            return redirect('dashboard:profileUpdate')

        messages.warning(self.request, f'{p_form.errors}')
        return redirect('dashboard:profileUpdate')


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
            if u_form.is_valid():
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
        return redirect('dashboard:userUpdate')


class UserLayoutUpdate(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        instance = get_object_or_404(Layout, user=self.request.user)
        layout_form = LayoutForm(self.request.FILES or None, instance=instance)
        portfolio_template = PortfolioTemplate.objects.all()
        context = {
            'layout': instance,
            'layout_form': layout_form,
            'portfolio_template': portfolio_template,
        }
        return render(self.request, 'dashboard/layout.html', context)

    def post(self, *args, **kwargs):
        l_form = LayoutForm(self.request.POST,
                            self.request.FILES,
                            instance=self.request.user.layout)
        if l_form.is_valid():
            print('the portfolio version', l_form.cleaned_data['portfolio_version'].paid)
            porfolio_type = l_form.cleaned_data['portfolio_version']
            user_subscription = get_user_subscription(self.request)
            if user_subscription:
                if user_subscription.membership.membership_type != 'Free' and user_subscription.expiration_date > datetime.now():
                    l_form.save()
                elif porfolio_type.paid == 'False':
                    l_form.save()
                else:
                    l_form.save(commit=False)
                    l_form.portfolio_version = self.request.user.layout.portfolio_version
                    l_form.save()
                    messages.info(self.request,
                                  'You dont have access to this template you have to become a premium member ')
                    return redirect('home_page:price')
                # this is used only when updating layout from the user portfolio
                if self.request.user.username == self.request.POST.get('the_user'):
                    return HttpResponseRedirect(self.request.user.profile.get_portfolio_absolute_url())
                messages.success(self.request, f'Layout has been updated')
                return redirect('dashboard:layoutUpdate')
        messages.warning(self.request, f'{l_form.errors}')
        return redirect('dashboard:layoutUpdate')

