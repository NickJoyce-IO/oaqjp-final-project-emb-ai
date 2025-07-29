import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } } 
    response = requests.post(url, headers=headers, json=input_json)
    print(response.status_code, "STATUS CODE")
    
    if response.status_code == 200:
        res_dict = json.loads(response.text)
        emotions_dict = res_dict['emotionPredictions'][0]["emotion"]
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)
        return {
            'anger': emotions_dict['anger'],
            'disgust': emotions_dict['disgust'],
            'fear': emotions_dict['fear'],
            'joy': emotions_dict['joy'],
            'sadness': emotions_dict['sadness'],
            'dominant_emotion': dominant_emotion
        }
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
