import requests
import subprocess
import os
import pyaudio


def text_to_speech(answer):
    key = "1a7933ab6deb4875ae7fe8da33cd9eff"
    key2 = "6304665b538349ec89e3a9cf57532202"
    jwt = requests.post("https://api.cognitive.microsoft.com/sts/v1.0/issueToken", headers={'Ocp-Apim-Subscription-Key': key}).text
    url = "https://speech.platform.bing.com/synthesize"
    headers = {'X-Search-AppId': key, 'X-Search-ClientID':key2, 'Authorization': jwt, 'X-Microsoft-OutputFormat': "audio-16khz-32kbitrate-mono-mp3"}
    data = {'text': "<speak>" + answer + "</speak>"}
    r = requests.post(url, data=data, headers=headers)
    if(r.status_code >= 200 and r.status_code < 300):
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(width=2), channels=1, rate=16000, output=True)
        for chunk in r.iter_content(chunk_size=128):
            print(chuck)
            stream.write(chuck)
        else:
            print("Failed to retrieve text conversion")
            
