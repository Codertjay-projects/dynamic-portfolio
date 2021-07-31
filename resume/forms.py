from django import forms

from .models import Resume


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
