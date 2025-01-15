from django import forms

class SearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('label', 'label'),
        ('type', 'type'),
        ('color', 'color'),
    ]
    search_type = forms.ChoiceField(choices=SEARCH_CHOICES, required=True, label='Search Type')
    query = forms.CharField(max_length=100, required=True, label='Search Query')
