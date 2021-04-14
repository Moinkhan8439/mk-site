from django import forms
from .models import Incident
from django.forms import Textarea,DateTimeInput


from pytube import YouTube
from pytube.exceptions import RegexMatchError



class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 2}),
            'incident_location': Textarea(attrs={'cols': 80, 'rows': 2}),
            'cause': Textarea(attrs={'cols': 80, 'rows': 2}),
            'action_taken': Textarea(attrs={'cols': 80, 'rows': 2}),
            'time' : DateTimeInput(attrs={})
        }


class YoutubeForm(forms.Form):
    url=forms.CharField( required=True,widget=forms.Textarea(attrs={'cols':80,'rows':1,'placeholder':'Enter Url here'}))

    def clean(self):
        video_url=self.cleaned_data.get('url')
        try:         
            yt = YouTube(video_url)
        except RegexMatchError:
            raise forms.ValidationError('The Url you entered is not correct')
        return self.cleaned_data