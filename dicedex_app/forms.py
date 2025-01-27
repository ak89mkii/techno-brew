from django import forms

class SearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('last_name', 'last_name'),
        ('first_name', 'first_name'),
        ('owner_id', 'owner_id'),
        ('dog_name', 'dog_name'),
        ('dog_id', 'dog_id'),
    ]
    search_type = forms.ChoiceField(choices=SEARCH_CHOICES, required=True, label='Search Type')
    query = forms.CharField(max_length=100, required=True, label='Search Query')
