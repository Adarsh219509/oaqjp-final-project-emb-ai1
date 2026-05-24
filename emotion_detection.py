import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
       
    if "emotionPredictions" in result and len(result["emotionPredictions"]) > 0:
        dominant_emotion = result["emotionPredictions"][0]["emotion"]
        return dominant_emotion
    else:
        return None

    print(dominant_emotion)


if __name__ == "__main__":
    sample_text = input("Enter text to analyze: ")
    print("Detected emotion:", emotion_detector(sample_text))