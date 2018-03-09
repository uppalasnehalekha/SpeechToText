from django.shortcuts import render, render_to_response
from home.SpeechToText import SpeechToText
from home.ToneAnalyser import ToneAnalyser
from home.TextSummary import TextSummary
from home.LocalLang import LocalLang
import re

def index(request):
    return render(request,'index.html',{'transcripts':"Transcripts will be displayed here",'tone':"Tone will be displayed here",'summary':"Summary will be displayed here"})

def message(request):
    file = request.GET['file1']
    language = request.GET['language']
    language = str(language)
    print(file)
    print('starting watson s2t')
    if language == 'en':
        transcripts = SpeechToText().getText(file,'mp3')
        org_lang = ""
        with open(file.replace('mp3','txt'),'w') as f:
            f.write(transcripts)
    else:
        trans = LocalLang().getText(file,language)
        org_lang = trans[0]
        transcripts = trans[1]
        with open(file.replace('flac','txt'),'w') as f:
            f.write(transcripts)
    print('starting watson tone\n'+transcripts)
    tone = ToneAnalyser().getTone(transcripts)
    print('starting summary\n'+tone)
    try:
        summary = TextSummary().getSummary(transcripts, 0.5)
    except:
        summary = transcripts
    print('starting return\n'+summary)
    return render(request,'index.html',{'org_lang':org_lang,'transcripts':transcripts,'tone':tone,'summary':summary})

    
