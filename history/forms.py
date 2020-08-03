from django import forms
from .models import HistoryUrl


class HistoryUrlModelForm(forms.ModelForm):
    class Meta:
        model = HistoryUrl
        fields = ['url']

# do validation check to insure it's youtube video Url

    def clean_url(self, *args, **kwargs):
        url = self.cleaned_data.get('url')
        if url.startswith('https://www.youtube.com/watch?v=') != True:
            raise forms.ValidationError('Please Enter a Valid Youtube Url')
        return url
