import requests
import json

class ToneAnalyser:
    
    def getTone(self,text):
        params = (
            ('version', '2018-03-08'),
            ('text', text),
        )

        response = requests.get('https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone', params=params, auth=('da5b8a9d-249b-4235-997c-451f02c48025', 'z6PGFSCZclav'))
        jsonData = json.loads(response.text)
        l = len(jsonData["document_tone"]["tones"])
        maxi = -1
        ind = -1
        for i in range(l):
            if jsonData["document_tone"]["tones"][i]["score"] > maxi:
                maxi = jsonData["document_tone"]["tones"][i]["score"]
                ind = i
        if ind < 0:
            return 'No Tone Detected'
        return jsonData["document_tone"]["tones"][ind]["tone_name"]
