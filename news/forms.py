from django import forms
from .models import Category, News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '200',
                'required': True
            })
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content',
                  'author', 'created_at',
                  'image', 'categories']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
