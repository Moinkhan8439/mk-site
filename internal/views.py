from pytube import YouTube
from pytube.exceptions import RegexMatchError

from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import IncidentForm , YoutubeForm
from django import forms

# Create your views here.
def home(request):
    return render(request,'index.html')


def report_incident(request):
    form=IncidentForm()
    if request.method == 'POST':
        print(request.POST)
        form=IncidentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(report_incident)
        else:
            return HttpResponse("incorrect data")
    else: 
        return render(request,'incident-form.html',{'form': form})


def youtube_downloader(request):
    form=YoutubeForm()
    if request.method == 'POST':
        form=YoutubeForm(data=request.POST)
        if form.is_valid():
            video_url=form.cleaned_data['url'] 
            yt = YouTube(video_url)
            my_vid=yt.streams
            stream_dict=list()
            for i in my_vid:
                size=f'{(i.filesize/(1024*1024)):.2f}MB'
                temp={
                    'itag':i.itag,
                    'resolution':i.resolution,
                    'type':i.type,
                    'size':size,
                    'subtype':i.subtype,
                    'url':video_url.split('.com/')[1]
                }
                stream_dict.append(temp)
                video={
                    'title':yt.title,
                    'thumbnail': yt.thumbnail_url,
                    'length':yt.length,
                    'streams':stream_dict
                    }
            return render(request,'youtube.html',{'form':form,'video':video})
    return render(request,'youtube.html',{'form':form })



def download_video(request,url,itag):
    video_url='https://www.youtube.com/'+url
    yt = YouTube(video_url)
    yt.streams.get_by_itag(itag).download()
    return redirect(youtube_downloader)
    