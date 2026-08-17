from django import forms
from django.utils import timezone

from .models import Category, Expense


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']

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


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = ['title','amount','expense_date','description','category',]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter expense title'
                }
            ),

            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter amount',
                    'step': '0.01'
                }
            ),

            'expense_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 4
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            self.initial['expense_date'] = timezone.localdate()