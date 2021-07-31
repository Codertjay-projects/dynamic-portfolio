from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from _profile.forms import (LayoutForm,
                            ProfileForm)
from _profile.models import (Layout,
                             Profile, )
from skill.forms import SkillsForm
from skill.models import Skill
from testimonial.forms import TestimonialForm
from testimonial.models import Testimonial


@login_required
def userDashboard(request, *args, **kwargs):
    layout = Layout.objects.filter(user=request.user)
    profile = Profile.objects.filter(user=request.user)
    testimonial = Testimonial.objects.filter(user=request.user)
    skills = Skill.objects.filter(user=request.user)
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
    return render(request, 'dashboard/dashboard.html', context)

