from django import forms
from upload_validator import FileTypeValidator

from .models import Testimonial


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
