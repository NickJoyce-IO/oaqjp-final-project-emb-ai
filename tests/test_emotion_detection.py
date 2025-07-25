from EmotionPackage import emotion_detector

def test_emotion_detector_returns_expected_joy():
    res = emotion_detector("I am glad this happened")
    assert res["dominant_emotion"] == 'joy'

def test_emotion_detector_returns_expected_anger():
    res = emotion_detector("I am really mad about this")
    assert res["dominant_emotion"] == "anger"

def test_emotion_detector_returns_expected_disgust():
    res = emotion_detector("I feel disgusted just hearing about this")
    assert res["dominant_emotion"] == "disgust"

def test_emotion_detector_returns_expected_sadness():
    res = emotion_detector("I am so sad about this")
    assert res["dominant_emotion"] == "sadness"

def test_emotion_detector_returns_expected_fear():
    res = emotion_detector("I am really afraid that this will happen")
    assert res["dominant_emotion"] == "fear"