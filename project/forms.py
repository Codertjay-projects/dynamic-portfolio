from django import forms
from upload_validator import FileTypeValidator

from .models import ProjectItem, Project


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

    description = forms.CharField(required=True, max_length=100, label='Description', widget=forms.Textarea(attrs={
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
            'instagram',
            'twitter',
        ]

