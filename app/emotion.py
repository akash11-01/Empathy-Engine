from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text: str) -> dict:
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.5:
        emotion = "positive"
    elif compound <= -0.5:
        emotion = "negative"
    else:
        emotion = "neutral"

    return {
        "emotion": emotion,
        "scores": scores,
        "intensity": abs(compound)
    }