"""
Server file to run the flask server for the emotion detector.
"""

from flask import Flask, request
from EmotionPackage import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyze the emotional content of a given text and return a formatted summary.

    This function retrieves the 'textToAnalyse' query parameter from an HTTP GET request,
    analyzes the text using the `emotion_detector` function, and returns the scores for 
    several emotions along with the dominant emotion.

    Returns:
        str: A response string summarizing the emotion scores and dominant emotion,
             or an error message if the input text is invalid or no dominant emotion is found.
    """
    text = request.args.get('textToAnalyse')
    res = emotion_detector(text)
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!\n"
    return (
    f"For the given statement, the system response is 'anger': {res['anger']} "
    f"'disgust': {res['disgust']}, 'fear': {res['fear']}, "
    f"'joy': {res['joy']} and 'sadness': {res['sadness']}. "
    f"The dominant emotion is {res['dominant_emotion']}.\n"
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000,  debug=True)
