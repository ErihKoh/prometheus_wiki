from django import forms


class NewPage(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))


class SearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'search',
                                                                     'type': 'text',
                                                                     'placeholder': 'Search Encyclopedia'}))
