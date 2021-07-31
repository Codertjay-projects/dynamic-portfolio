from django import forms
from .models import Service
from upload_validator import FileTypeValidator


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
