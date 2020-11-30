from django import forms
from upload_validator import FileTypeValidator

from .models import Post, blogCategory

from pagedown.widgets import PagedownWidget


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=200, label='Title',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control  ',
                                'label': 'Title',

                            }))
    slug = forms.SlugField(required=True,
                           max_length=50,
                           label='Slug')
    image = forms.ImageField(required=True, validators=[FileTypeValidator(
        allowed_types=['image/*']
    )],
                             widget=forms.FileInput(attrs={
                                 'class': '  waves-effect   bg-primary   ',

                             }))

    published_date = forms.DateTimeField(label='Published Date', widget=forms.SelectDateWidget(attrs={
        'class': 'form-control   datetimepicker ',
        'label': 'published_date',
    }))

    category = forms.ChoiceField(choices=blogCategory, required=False,
                                 widget=forms.Select(attrs={
                                     'class': 'form-control bg-primary text-info dropdown-toggle ',
                                     'type': "button",
                                     'data-toggle': "dropdown"
                                 }))
    description = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = ['title'
            , 'slug'
            , 'category'
            , 'description'
            , 'image'
            , 'published_date']
