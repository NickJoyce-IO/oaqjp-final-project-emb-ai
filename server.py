from flask import Flask, request
from EmotionPackage import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get('textToAnalyse')
    res = emotion_detector(text)
 
    return (
        f"For the given statement, the system response is 'anger': {res['anger']} "
        f"'disgust': {res['disgust']}, 'fear': {res['fear']}, "
        f"'joy': {res['joy']} and 'sadness': {res['sadness']}. "
        f"The dominant emotion is {res['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)