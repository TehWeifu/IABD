# save this as app.py
import os.path
import random
import time
from datetime import datetime
from werkzeug.utils import secure_filename

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)
launch_time = time.time_ns()


@app.route('/hc')
def health_check():
    now = datetime.now()
    formatted_now = now.strftime("%B %d, %Y %H:%M:%S")

    current_time = time.time_ns()
    elapsed_time = (current_time - launch_time) / 1_000_000_000

    return f'Server time: {formatted_now}. The server has been running for {elapsed_time:.2f} seconds'


@app.route('/hello_world')
def hello_world():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/animal_guesser')
def animal_guesser():
    animal = request.args.get("pet", "who.jpg")
    return f"The image {escape(animal)} has {random.randint(0, 100)}% chance a to be a dog."


@app.route('/upload_image', methods=['POST'])
def upload_image():
    my_file = request.files['file']
    filename = 'saved_' + secure_filename(my_file.filename)
    my_file.save(os.path.join('.', filename))
    return f"Image {filename} saved successfully"
