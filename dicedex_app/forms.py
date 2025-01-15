from django import forms

class SearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('title', 'Title'),
        ('author', 'Author'),
        ('content', 'Content'),
    ]
    search_type = forms.ChoiceField(choices=SEARCH_CHOICES, required=True, label='Search Type')
    query = forms.CharField(max_length=100, required=True, label='Search Query')
