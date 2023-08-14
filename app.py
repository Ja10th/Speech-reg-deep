from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import numpy as np
import librosa
import librosa.display
from keras.models import load_model

# Initialize the Flask app
app = Flask(__name__)

# Directory where uploaded files will be stored
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file has an allowed extension
ALLOWED_EXTENSIONS = {'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load the emotion recognition model
model = load_model('/emotion_model.h5')

# Function to preprocess audio data
def extract_mfcc(audio_file_path):
    y, sr = librosa.load(audio_file_path, duration=3, offset=0.5)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc

# Flask route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Flask route for handling file upload
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return redirect(url_for('result', filename=filename))
        else:
            return render_template('index.html', error="Invalid file. Only WAV files are allowed.")

# Flask route for analyzing the uploaded audio
@app.route('/result/<filename>')
def result(filename):
    audio_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    input_mfcc = extract_mfcc(audio_file_path)
    input_mfcc = np.expand_dims(input_mfcc, axis=0)
    input_mfcc = np.expand_dims(input_mfcc, axis=-1)
    predicted_emotion_index = np.argmax(model.predict(input_mfcc))
    emotion_labels = ['fear', 'angry', 'disgust', 'neutral', 'sad', 'ps', 'happy']
    predicted_emotion = emotion_labels[predicted_emotion_index]
    return render_template('result.html', predicted_emotion=predicted_emotion, uploaded_file=filename)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
