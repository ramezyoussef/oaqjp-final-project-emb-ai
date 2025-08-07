"""Flask app for detecting emotions from input text using Watson NLP service."""
from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Endpoint to detect emotion from text."""
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return jsonify({'error': 'Invalid text! Please try again!'}), 200

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 200

    return jsonify(response)

@app.route("/")
def render_index_page():
    """Render the homepage with the text input form."""
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
