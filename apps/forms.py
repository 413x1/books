from django import forms
from .models import Category, Book


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'category', 'keywords', 'price', 'author']

# class BookFilterForm(forms.Form):
#     title = forms.CharField(max_length=200, required=False, label='Title')
#     description = forms.CharField(required=False, label='Description')
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select Category', required=False, label='Category')
#     keywords = forms.CharField(max_length=200, required=False, label='Keywords')
#     price_min = forms.DecimalField(required=False, label='Minimum Price')
#     price_max = forms.DecimalField(required=False, label='Maximum Price')
#     author = forms.CharField(max_length=100, required=False, label='Author')

class BookFilterForm(forms.Form):
    field_names = ['title', 'description', 'category', 'keywords', 'price', 'author']

    for field_name in field_names:
        attrs = {'class': 'input'}
        if field_name == 'category':
            widget = forms.Select(attrs=attrs)
            queryset = Category.objects.all()
            locals()[field_name] = forms.ModelChoiceField(queryset=queryset, empty_label='Select Category', required=False, label='Category', widget=widget)
        else:
            if field_name == 'price':
                widget = forms.NumberInput(attrs=attrs)
            else:
                widget = forms.TextInput(attrs=attrs)
            placeholder = field_name.capitalize()
            widget.attrs['placeholder'] = f'{placeholder}'  # Set the placeholder attribute
            locals()[field_name] = forms.CharField(widget=widget, required=False, label=field_name.capitalize())
