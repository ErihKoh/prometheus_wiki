from django import forms


class NewPage(forms.Form):
    title = forms.CharField(initial='#')
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search'})) 