from django import forms
from users.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Layout, Profile, Testimonial, Contact, Skills, skill_choices, portfolio_choices, Service, \
    background_colors, Resume
from colorful.fields import RGBColorField
from upload_validator import FileTypeValidator


class ProfileForm(forms.ModelForm):
    motto = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control   col-12',
    }))
    country = CountryField(blank_label='(select country)', blank=True).formfield(widget=CountrySelectWidget(attrs={
        'class': 'form-control  dropdown-toggle bg-primary  ',
        'type': "button",
        'data-toggle': "dropdown",
        "form_show_labels": False,
        'style': ' max-width: 70%;color:white;'
    }))
    phone_number = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control    ',
        'label': 'Phone Number'
    }))

    website = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control    ',
        'label': 'Phone Number'
    }))

    linkedin = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control   ',
        'label': 'linkedin'
    }))
    twitter = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control    ',
        'label': 'Twitter'
    }))
    instagram = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control   ',
        'label': 'Instagram'
    }))
    portfolio_version = forms.ChoiceField(choices=portfolio_choices, required=False,
                                          widget=forms.Select(attrs={
                                              'class': 'form-control  dropdown-toggle btn btn-primary  btn-block ',
                                              'type': "button",
                                              'data-toggle': "dropdown",
                                              'style': 'max-width: 50%;'

                                          }))
    facebook = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control    ',
        'label': 'facebook',
        "form_show_labels": False,
    }))
    address = forms.CharField(required=False, max_length=200, label='Address', widget=forms.TextInput(attrs={
        'class': 'form-control  ',
        'label': 'Address',

    }))

    about = forms.Textarea(attrs={
        'class': 'form-control   ',
        'cols': '40',
        'rows': '10'}
    )

    class Meta:
        model = Profile
        fields = [
            'motto',
            'country',
            'phone_number',
            'portfolio_version',
            'website',
            'linkedin',
            'twitter',
            'instagram',
            'facebook',
            'address',
            'about',
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['country'].required = False


class UserUpdateForm(forms.Form):
    username = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control   ',
        'label': 'Username'
    }))
    first_name = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control   ',
        'label': 'Username'
    }))
    last_name = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control   ',
        'label': 'Username'
    }))

    email = forms.EmailField(required=False, max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control   ',
        'label': 'Email',
        'value': 'dscfdsfdfdf'
    }))


class LayoutForm(forms.ModelForm):
    primary_color = RGBColorField()
    secondary_color = RGBColorField()
    background_color = forms.ChoiceField(choices=background_colors, required=False,
                                         widget=forms.Select(attrs={
                                             'class': 'form-control  dropdown-toggle btn btn-primary  btn-block ',
                                             'type': "button",
                                             'data-toggle': "dropdown",
                                             'style': 'max-width: 80%'
                                         }))
    profile_pics = forms.ImageField(required=False, validators=[FileTypeValidator(
        allowed_types=['image/*']
    )], widget=forms.FileInput(attrs={
        'class': ' waves-effect  text-light waves-light picture-src    col-4  mx-auto  _profile_pics',
        'label': 'Profile Picture',
        'style': 'background-color: #E0A0E4'
    }))
    logo = forms.ImageField(required=False, label='', validators=[FileTypeValidator(
        allowed_types=['image/*']
    )], widget=forms.FileInput(attrs={
        'class': ' waves-effect   text-light  waves-light col-4 mx-auto',
        'style': 'background-color: #E0A0E4'
    }))
    background_image = forms.ImageField(required=False, label='', validators=[FileTypeValidator(
        allowed_types=['image/*']
    )], widget=forms.FileInput(attrs={
        'class': '  waves-effect    text-light waves-light  mx-auto col-4 ',
        'style': 'background-color: #E0A0E4'

    }))

    class Meta:
        model = Layout
        fields = [
            'primary_color',
            'secondary_color',
            'background_color',
            'profile_pics',
            'logo',
            'background_image',
        ]


class TestimonialForm(forms.ModelForm):
    client_name = forms.CharField(max_length=50, label='Client Name', widget=forms.TextInput(attrs={
        'placeholder': ' The client name you worked with ',
        'class': ' form-control  ',
    }))
    image = forms.ImageField(required=False, label='Image', validators=[FileTypeValidator(
        allowed_types=['image/*']
    )], widget=forms.FileInput(attrs={
        'class': '  form-control  bg-primary  mx-auto  ',

    }))
    url = forms.URLField(label='Link', widget=forms.URLInput(attrs={
        'class': ' form-control  ',
        'placeholder': 'Any link to the client or project'
    }))
    detail = forms.CharField(max_length=500, label='Detail', widget=forms.TextInput(attrs={
        'class': ' font-weight-bold mt-3 form-control',
        'cols': ' 10',
        'rows': '4',
    }))

    class Meta:
        model = Testimonial
        fields = [
            'client_name',
            'image',
            'url',
            'detail',
        ]


class SkillsForm(forms.ModelForm):
    name = forms.CharField(max_length=15, label='Skill Name', widget=forms.TextInput(attrs={
        'class': ' font-weight-bold mt-3'
    }))
    description = forms.CharField(max_length=200, label='Skill Description', widget=forms.TextInput(attrs={
        'class': ' font-weight-bold mt-3',
        'cols': ' 10',
        'rows': '4',
    }))
    percent = forms.IntegerField(required=False, max_value=100, min_value=1, widget=forms.NumberInput(attrs={
        'class': ' font-weight-bold mt-3',
        'placeholder': 'maximum number of 100 and minimum of 1',
        'maxlength': "100",
    }))

    class Meta:
        model = Skills
        fields = [
            'name',
            'percent',
            'description',
            'icon',
        ]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': ' Your Name ',
        'class': ' form-control  ',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email ',
        'class': 'form-control  ',

    }))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Subject ',
        'class': 'form-control  ',
    }))
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        'placeholder': ' Content ',
        'class': 'md-textarea form-control  ',
        'rows': '5',
        'cols': '20'
    }))

    def clean_email(self):
        email_passed = self.cleaned_data.get('email')
        email_req = 'mmm'
        if email_passed != email_req:
            return forms.ValidationError("Not a valig email pls try again")
        return email_passed


class ServiceForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Subject ',
        'class': 'form-control  ',
    }))
    image = forms.ImageField(required=True, validators=[FileTypeValidator(
        allowed_types=['image/*']
    )], widget=forms.FileInput(attrs={
        'class': 'btn btn-purple ed btn-sm mt-3  bg-primary  waves-effect  waves-light  mx-auto col-7 ',
    }))
    description = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={
        'placeholder': ' Content of 200 characters',
        'class': 'md-textarea form-control  ',
        'rows': '5',
        'cols': '20'
    }))

    class Meta:
        model = Service
        fields = [
            'name',
            'image',
            'description',
        ]


class ResumeForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    start_date = forms.CharField()
    end_date = forms.CharField(required=False)
    detail = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={
        'placeholder': ' Content ',
        'class': 'md-textarea form-control  ',
        'rows': '5',
        'cols': '20'
    }))

    class Meta:
        model = Resume
        fields = ['name',
                  'start_date',
                  'end_date',
                  'detail']
