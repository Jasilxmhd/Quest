from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = [
            'name',
            'description'
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter category name'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 4
                }
            ),
        }

    def clean_name(self):

        name = self.cleaned_data['name'].strip()

        if len(name) < 3:

            raise forms.ValidationError(
                'Category name must contain at least 3 characters.'
            )

        return name