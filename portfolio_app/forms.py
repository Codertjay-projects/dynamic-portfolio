from django import forms
from .models import ProjectItem, Project, Testimonial, Service, Resume,Skills
from upload_validator import FileTypeValidator


class ProjectForm(forms.ModelForm):
    name = forms.CharField(required=False, max_length=50, label='Name', widget=forms.TextInput(attrs={
        'class': 'form-control  ',

    }))
    image = forms.ImageField(required=False, label='', validators=[FileTypeValidator(
        allowed_types=['image/*']
    )], widget=forms.FileInput(attrs={
        'class': ' '
    }))
    description = forms.CharField(required=False, max_length=200, label='Description', widget=forms.Textarea(attrs={
        'class': 'form-control   ',
        'cols': '100',
        'placeholder': 'just a little description with maximum characters of 200',
        'rows': '4'}))

    class Meta:
        model = Project
        fields = [
            'name',
            'image',
            'description',
        ]


class ProjectItemsForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=50, label='Name', widget=forms.TextInput(attrs={
        'class': 'form-control  ',
        'placeholder': 'maximum length of 10',

    }))
    image = forms.ImageField(required=True, label='Image', validators=[FileTypeValidator(
        allowed_types=['image/*']
    )], widget=forms.FileInput(attrs={
        'class': ''
    }))

    description = forms.CharField(required=True, max_length=200, label='Description', widget=forms.Textarea(attrs={
        'class': 'form-control   ',
        'cols': '100',
        'placeholder': 'just a little description with maximum characters of 50',
        'rows': '4'}))

    class Meta:
        model = ProjectItem
        fields = [
            'name',
            'image',
            'description',
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
        'placeholder': ' Detail here  ',
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
