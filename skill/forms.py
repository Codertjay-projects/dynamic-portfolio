from django import forms

from .models import Skill


class SkillsForm(forms.ModelForm):
    name = forms.CharField(max_length=15, label='Skill Name', widget=forms.TextInput(attrs={
        'class': ' font-weight-bold mt-3'
    }))
    description = forms.CharField(max_length=200, label='Skill Description', widget=forms.TextInput(attrs={
        'class': ' font-weight-bold mt-3',
        'cols': ' 10',
        'rows': '4',
    }))
    percent = forms.IntegerField( max_value=100, min_value=1, widget=forms.NumberInput(attrs={
        'class': ' font-weight-bold mt-3',
        'placeholder': 'maximum number of 100 and minimum of 1',
        'maxlength': "100",
    }))

    class Meta:
        model = Skill
        fields = [
            'name',
            'percent',
            'description',
            'icon',
        ]
