# -*- coding: utf-8 -*-
import base64
import requests
import json

from googletrans import Translator
class LocalLang:
    def encode_audio(self,audio):
      audio_content = audio.read()
      return base64.b64encode(audio_content)

    def getText(self,file,lang):
        text = self.encode_audio(open(file,'rb'))
        url = "https://speech.googleapis.com/v1/speech:recognize?key=AIzaSyBUkoTzrhNg3qq7q1s826nukmXuQv5YBIo" 
        r = requests.post(url, json={
          "audio": {
            "content":  text
          },
          "config": {
            "encoding": "FLAC",
            "sampleRateHertz": 16000,
            "languageCode": lang+"-IN"
          } 
        })
        jsonData = json.loads(r.text)
        data = jsonData["results"][0]["alternatives"][0]["transcript"]
        strs = [data]
        #print data
        translator = Translator()
        trans = translator.translate(data,src=lang)
        strs.append(trans.text)
        return strs
