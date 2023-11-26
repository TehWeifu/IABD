# save this as app.py
import json
import os.path
import time

from flask import Flask, request
from datetime import datetime

import csv

app = Flask(__name__)
launch_time = time.time_ns()


@app.route('/tasks')
def get_tasks():
    task_id = request.args.get("task", "")

    if not os.path.exists('./tasks.csv'):
        return ""

    file = open('./tasks.csv')
    csvreader = csv.reader(file)

    rows = []
    for row in csvreader:
        if len(task_id) == 0 or row[0] == task_id:
            rows.append(row)

    file.close()

    return json.dumps(rows)


@app.route('/tasks', methods=['POST'])
def post_tasks():
    request_data = request.json
    task_description = request_data.get('Description', '')

    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

    max_id = 1

    file = open('tasks.csv', 'r+')
    csvreader = csv.reader(file)

    for row in csvreader:
        if int(row[0]) > int(max_id):
            max_id = row[0]

    task_to_record = [max_id, task_description, 0, formatted_now]
    writer = csv.writer(file)
    writer.writerows([task_to_record])

    file.close()

    return json.dumps(task_to_record)


@app.route('/tasks', methods=['PUT'])
def put_tasks():
    task_id = request.args.get("task", "")

    file = open('tasks.csv')
    csvreader = csv.reader(file)

    remaining_rows = []
    for row in csvreader:
        if row[0] == task_id:
            row[2] = 1
            remaining_rows.append(row)

    # Write the remaining data back to the file
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)


@app.route('/tasks', methods=['DELETE'])
def delete_tasks():
    row_to_delete = request.args.get("task", "")

    # Read the data from the file and store all rows except the one to delete
    with open('tasks.csv', 'r', newline='') as file:
        rows = list(csv.reader(file))
        remaining_rows = [row for i, row in enumerate(rows) if row[0] != row_to_delete]

    # Write the remaining data back to the file
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)
