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

    file = open('./tasks.csv', newline='')
    csvreader = csv.reader(file)

    rows = []
    for row in csvreader:
        if row:
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

    max_id = 0

    file = open('tasks.csv', 'r+', newline='')
    csvreader = csv.reader(file)

    for row in csvreader:
        if row and int(row[0]) > int(max_id):
            max_id = row[0]

    task_to_record = [str(int(max_id) + 1), task_description, 0, formatted_now]
    writer = csv.writer(file)
    writer.writerows([task_to_record])

    file.close()

    return json.dumps(task_to_record)


@app.route('/tasks', methods=['PUT'])
def edit_task():
    request_data = request.json
    task_description = request_data.get('Description', '')

    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

    max_id = 0

    file = open('tasks.csv', 'r+', newline='')
    csvreader = csv.reader(file)

    for row in csvreader:
        if row and int(row[0]) > int(max_id):
            max_id = row[0]

    task_to_record = [str(int(max_id) + 1), task_description, 0, formatted_now]
    writer = csv.writer(file)
    writer.writerows([task_to_record])

    file.close()

    return json.dumps(task_to_record)


# Completar una tarea
@app.route('/check-task', methods=['PUT'])
def check_task():
    task_id = request.args.get("task", "")

    file = open('tasks.csv', newline='')
    csvreader = csv.reader(file)

    task_to_update = ""
    remaining_rows = []
    for row in csvreader:
        if row[0] == task_id:
            row[2] = 1
            task_to_update = row
        remaining_rows.append(row)

    # Write the remaining data back to the file
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    return json.dumps(task_to_update)


# Cambiar una tarea de completa a incompleta
@app.route('/uncheck-task', methods=['PUT'])
def uncheck_task():
    task_id = request.args.get("task", "")

    file = open('tasks.csv', newline='')
    csvreader = csv.reader(file)

    task_to_update = ""
    remaining_rows = []
    for row in csvreader:
        if row[0] == task_id:
            row[2] = 0
            task_to_update = row
        remaining_rows.append(row)

    # Write the remaining data back to the file
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    return json.dumps(task_to_update)


@app.route('/tasks', methods=['DELETE'])
def delete_tasks():
    row_to_delete = request.args.get("task", "")

    # Read the data from the file and store all rows except the one to delete
    with open('tasks.csv', 'r', newline='') as file:
        rows = list(csv.reader(file))
        row_deleted = []
        remaining_rows = []
        for i, row in enumerate(rows):
            if row[0] != row_to_delete:
                remaining_rows.append(row)
            else:
                row_deleted = row

    # Write the remaining data back to the file
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    return json.dumps(row_deleted)


# Borrar todas las tareas finalizadas
@app.route('/completed-tasks', methods=['DELETE'])
def delete_completed_tasks():
    # Read the data from the file and store all rows except the one to delete
    with open('tasks.csv', 'r', newline='') as file:
        rows = list(csv.reader(file))
        rows_deleted = []
        remaining_rows = []
        for i, row in enumerate(rows):
            if row[2] == "1":
                remaining_rows.append(row)
            else:
                rows_deleted.append(row)

    # Write the remaining data back to the file
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    return json.dumps(rows_deleted)
