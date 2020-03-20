from django.shortcuts import render
from main import forms
from django.http import HttpResponseRedirect , HttpResponse
from google.cloud import texttospeech
from google.oauth2 import service_account
# Create your views here.
def index(request):
    form=forms.abc
    if request.method == "POST":
        form=forms.abc(request.POST)
        if form.is_valid():
            print(form)
            x=form.cleaned_data['STRING']
            print(x)
            credentials = service_account.Credentials.from_service_account_file(
                'C:/Users/acer/Downloads/MunishProject02111999-c479c6303f5e.json')
            scoped_credentials = credentials.with_scopes(
                ['https://www.googleapis.com/auth/cloud-platform'])
            client=texttospeech.TextToSpeechClient(credentials=credentials)
            synthesis_input = texttospeech.types.SynthesisInput(text=x)
            voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-IN',
                ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
            audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)
            response = client.synthesize_speech(synthesis_input, voice, audio_config)
            with open('static/output.mp3','wb') as file:
                file.write(response.audio_content)
                print('The Audio file is created in the current directory.')
            return HttpResponseRedirect('/audio')
        else:
            return HttpResponse("DATA ENTERED IS INVALID!!PLEASE TRY AGAIN!!!")
    context={
        "form":form
    }
    return render(request,'intro.html',context)


def audio(request):
    return render(request,'audio.html')