import io
import pathlib
import time
from datetime import datetime

import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from flask_cors import CORS

IMG_VALID_EXTENSIONS = ('png', 'jpg', 'jpeg')
IMG_SIZE = (8, 8)

app = Flask(__name__)
CORS(app)

launch_time = time.time_ns()

model = None
try:
    path = pathlib.Path(__file__).parent.resolve()
    model = tf.keras.models.load_model(path / '../Model/digit_model.h5')
except Exception as e:
    print(f"Failed to load the model: {e}")
    exit(1)


@app.route('/')
def index():
    with open('tests/index.html', 'r') as file:
        html_content = file.read()

    return html_content


@app.route('/hc')
def health_check():
    now = datetime.now()
    formatted_now = now.strftime("%B %d, %Y %H:%M:%S")

    current_time = time.time_ns()
    elapsed_time = (current_time - launch_time) / 1_000_000_000

    return jsonify({
        'date': formatted_now,
        'uptime': f'{elapsed_time:.2f}'
    })


@app.route('/predict', methods=['POST'])
def predict():
    if 'digit' not in request.files:
        return jsonify({'msg': "The image (parameter 'digit') is missing."}), 400

    image_request = request.files['digit']

    file_extension = image_request.filename.rsplit('.', 1)[1]
    if file_extension not in IMG_VALID_EXTENSIONS:
        return jsonify({f'msg': f"The image must have a {', '.join(IMG_VALID_EXTENSIONS)} extension"}), 415

    image_raw = read_image(image_request)
    image_clean = prepare_image(image_raw)

    prediction = model.predict(image_clean)

    return build_prediction_response(prediction)


def read_image(image):
    in_memory_file = io.BytesIO()
    image.save(in_memory_file)
    data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8, sep='')
    return cv2.imdecode(data, 0)


def prepare_image(raw_image):
    image = cv2.resize(raw_image, IMG_SIZE, interpolation=cv2.INTER_AREA)
    image = image / 255.0
    image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)

    return image


def build_prediction_response(prediction):
    score = float(prediction[0].max())
    digit = int(prediction[0].argmax())

    return jsonify({
        'digit': digit,
        'score': score,
    })
