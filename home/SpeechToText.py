import requests
import json

class SpeechToText:
    
    def getText(self,filePath,extension):
        self.headers = {
            'Content-Type': 'audio/'+extension,
        }
        self.fileName = filePath
        
        data = open(self.fileName, 'rb').read()
        response = requests.post('https://stream.watsonplatform.net/speech-to-text/api/v1/recognize', headers=self.headers, data=data, auth=('bf132f5f-beaf-4b46-b9d3-63c8a09d85b6', 'rhUa8wA0f8kE'))
        jsonData = json.loads(response.text)
        result = ""
        for i in range(len(jsonData["results"])):
            result += jsonData["results"][i]['alternatives'][0]['transcript']+".\n"
        return result
