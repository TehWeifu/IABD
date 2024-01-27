import random
import time
from datetime import datetime
import tensorflow as tf
import cv2
import numpy as np

from flask import Flask, request, jsonify

app = Flask(__name__)

launch_time = time.time_ns()

model = tf.keras.models.load_model('./../Model/digit_model.h5')

IMG_EXTENSIONS = ('png', 'jpg', 'jpeg')


@app.route('/hc')
def health_check():
    now = datetime.now()
    formatted_now = now.strftime("%B %d, %Y %H:%M:%S")

    current_time = time.time_ns()
    elapsed_time = (current_time - launch_time) / 1_000_000_000

    return jsonify({
        'date': formatted_now,
        'timestamp': f'{elapsed_time:.2f}'
    })


@app.route('/predict', methods=['POST'])
def predict():
    if 'digit' not in request.files:
        return jsonify({'msg': "The image (parameter 'digit') is missing."}), 400

    my_file = request.files['digit']

    file_extension = my_file.filename.rsplit('.', 1)[1]
    if file_extension not in IMG_EXTENSIONS:
        return jsonify({f'msg': f"The image must have a {', '.join(IMG_EXTENSIONS)} extension"}), 400

    img_dim = (8, 8)
    image = cv2.imread(my_file.filename, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, img_dim, interpolation=cv2.INTER_AREA)
    image = image / 255.0
    image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)

    value = int(prediction[0].max())
    index = int(prediction[0].argmax())

    return jsonify({
        'prediction': index,
        'score': value,
    })


def amazing_prediction_100_accurate_no_fake_4k():
    return {
        'prediction': random.randint(0, 9),
        'score': random.randint(0, 100) / 100,
    }
