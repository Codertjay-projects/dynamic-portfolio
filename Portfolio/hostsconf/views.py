from PIL import ImageColor
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from Portfolio.settings import DEFAULT_REDIRECT_URL
from _profile.forms import LayoutForm, ProfileForm, TestimonialForm, SkillsForm
from _profile.models import Skills, Testimonial, Service, Layout, Resume, Profile
from blog.models import Post
from portfolio_app.forms import ProjectForm, ProjectItemsForm
from portfolio_app.models import ProjectItem, Project
from users.forms import ContactUserForm


# Todo: i would need to create a 404 page to redirect the user when he or she goes to a url or host
#  that does not exist
def my_portfolio(request, username):
    print('the requsest get_raw_uri', request.get_raw_uri())
    print('this is the username', username)
    if username:
        project = Project.objects.filter(user__username=username)
        project_items = ProjectItem.objects.filter(user__username=username)
        profile = Profile.objects.filter(user__username=username).first()
        skills = Skills.objects.filter(user__username=username)
        testimonial = Testimonial.objects.filter(user__username=username)
        layout = Layout.objects.filter(user__username=username).first()
        service = Service.objects.filter(user__username=username)
        resume = Resume.objects.filter(user__username=username)
        post = Post.objects.filter(user__username=username)
        try:
            primary_color_nums = ImageColor.getrgb(layout.primary_color)
            secondary_color_nums = ImageColor.getrgb(layout.secondary_color)
            primary_color_1 = primary_color_nums[0]
            primary_color_2 = primary_color_nums[1]
            primary_color_3 = primary_color_nums[2]
            secondary_color_1 = secondary_color_nums[0]
            secondary_color_2 = secondary_color_nums[1]
            secondary_color_3 = secondary_color_nums[2]
            print('this is the project items', project_items)
            host_url = f"{profile.user.username}{settings.PARENT_HOST}"
        except Exception:
            primary_color_nums = None
            secondary_color_nums = None
            primary_color_1 = None
            primary_color_2 = None
            primary_color_3 = None
            secondary_color_1 = None
            secondary_color_2 = None
            secondary_color_3 = None
            host_url = None
    else:
        try:
            messages.warning(request, "the site does not exist")
        except Exception as a:
            print(a)
        return HttpResponseRedirect(DEFAULT_REDIRECT_URL)
    context = {
        'project': project,
        'ProjectItem': project_items,
        'profile': profile,
        'skills': skills,
        'testimonial': testimonial,
        'layout': layout,
        'post': post,
        'service': service,
        'resume': resume,
        'media_url': DEFAULT_REDIRECT_URL,
        'host_url': host_url,
        'primary_color': {
            'primary_color_1': primary_color_1,
            'primary_color_2': primary_color_2,
            'primary_color_3': primary_color_3,
        },
        'secondary_color': {
            'secondary_color_1': secondary_color_1,
            'secondary_color_2': secondary_color_2,
            'secondary_color_3': secondary_color_3,
        },

        'contact_user_form': ContactUserForm(),
        'user': 'user',
        'layout_form': LayoutForm(),
        'profile_form': ProfileForm(),
        'testimonial_form': TestimonialForm(),
        'skills_form': SkillsForm(),
        'Project_form': ProjectForm(),
        'Project_items_form': ProjectItemsForm(),

    }
    if profile:
        if profile.portfolio_version == 'portfolio_v1':
            return render(request, 'portfolio_v1/base_v1.html', context)
        elif profile.portfolio_version == 'portfolio_v2':
            return render(request, 'portfolio_v2/base_v2.html', context)
        elif profile.portfolio_version == 'portfolio_v3':
            return render(request, 'portfolio_v3/base_v3.html', context)
        elif profile.portfolio_version == 'portfolio_v4':
            return render(request, 'portfolio_v4/base_v4.html', context)
        elif profile.portfolio_version == 'portfolio_v5':
            return render(request, 'portfolio_v5/base_v5.html', context)
        else:
            try:
                messages.warning(request, "the site does not exist")
            except Exception as a:
                print(a)
            return HttpResponseRedirect(DEFAULT_REDIRECT_URL)
    else:
        try:
            messages.warning(request, "the site does not exist")
        except Exception as a:
            print(a)
        return HttpResponseRedirect(DEFAULT_REDIRECT_URL)
