from django import forms
from Book.models import Book


class FormsModel(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name_Book',
            'author',
            'description',
            'ISBN',
            'price',
            'pages',
            'time',
            'Image',
            'active',
        ]
    widgets = {
        'name_Book': forms.TextInput(attrs={'class': 'c'}),
        'author': forms.TextInput(attrs={'class': ''}),
        'description': forms.TextInput(attrs={'class': 'textarea'}),
        'ISBN': forms.TextInput(attrs={'class': ''}),
        'price': forms.NumberInput(attrs={'class': ''}),
        'pages': forms.NumberInput(attrs={'class': ''}),
        'time': forms.TimeInput(attrs={'class': ''}),
        'Image': forms.FileInput(attrs={'class': ''}),
        'active': forms.Select(attrs={'class': ''}),
    }