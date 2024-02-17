import json
import os.path
import time

from flask import Flask, request, jsonify
from datetime import datetime

import csv

app = Flask(__name__)
launch_time = time.time_ns()

if not os.path.exists('tasks.csv'):
    open('tasks.csv', 'w')


# Listar todas las tareas
@app.route('/tasks')
def get_tasks():
    task_id = request.args.get("task", "")

    file = open('tasks.csv', newline='')
    csvreader = csv.reader(file)

    rows = []
    for row in csvreader:
        if row:
            if len(task_id) == 0 or row[0] == task_id:
                rows.append(row)

    file.close()

    return json.dumps(rows)


# Agregar una tarea
@app.route('/tasks', methods=['POST'])
def post_tasks():
    request_data = request.json
    task_description = request_data.get('Description', '')
    if not task_description:
        return jsonify({'msg': 'Task description is mandatory.'}), 400

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


# Editar una tarea en concreto TODO
@app.route('/tasks', methods=['PUT'])
def edit_task():
    updated_flag = False
    task_id = request.args.get("task", "")

    request_data = request.json
    task_description = request_data.get('Description', '')
    if not task_description:
        return jsonify({'msg': 'Task description is mandatory.'}), 400

    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

    file = open('tasks.csv', 'r+', newline='')
    csvreader = csv.reader(file)

    task_to_update = ""
    remaining_rows = []
    for row in csvreader:
        if row[0] == task_id:
            row[1] = task_description
            row[2] = 1
            row[3] = formatted_now
            task_to_update = row
            updated_flag = True
        remaining_rows.append(row)

    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    if updated_flag:
        return json.dumps(task_to_update)
    else:
        return jsonify({'msg': 'Task id not found.'}), 400


# Completar una tarea
@app.route('/check-task', methods=['PUT'])
def check_task():
    updated_flag = False
    task_id = request.args.get("task", "")

    file = open('tasks.csv', newline='')
    csvreader = csv.reader(file)

    task_to_update = ""
    remaining_rows = []
    for row in csvreader:
        if row[0] == task_id:
            row[2] = 1
            task_to_update = row
            updated_flag = True
        remaining_rows.append(row)

    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    if updated_flag:
        return json.dumps(task_to_update)
    else:
        return jsonify({'msg': 'Task id not found.'}), 400


# Cambiar una tarea de completa a incompleta
@app.route('/uncheck-task', methods=['PUT'])
def uncheck_task():
    updated_flag = False

    task_id = request.args.get("task", "")

    file = open('tasks.csv', newline='')
    csvreader = csv.reader(file)

    task_to_update = ""
    remaining_rows = []
    for row in csvreader:
        if row[0] == task_id:
            row[2] = 0
            task_to_update = row
            updated_flag = True
        remaining_rows.append(row)

    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    if updated_flag:
        return json.dumps(task_to_update)
    else:
        return jsonify({'msg': 'Task id not found.'}), 400


# Borrar una tarea
@app.route('/tasks', methods=['DELETE'])
def delete_tasks():
    deleted_flag = False
    row_to_delete = request.args.get("task", "")

    with open('tasks.csv', 'r', newline='') as file:
        rows = list(csv.reader(file))
        row_deleted = []
        remaining_rows = []
        for i, row in enumerate(rows):
            if row[0] != row_to_delete:
                remaining_rows.append(row)
            else:
                row_deleted = row
                deleted_flag = True

    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    if deleted_flag:
        return json.dumps(row_deleted)
    else:
        return jsonify({'msg': 'Task id not found.'}), 400


# Borrar todas las tareas finalizadas
@app.route('/completed-tasks', methods=['DELETE'])
def delete_completed_tasks():
    with open('tasks.csv', 'r', newline='') as file:
        rows = list(csv.reader(file))
        rows_deleted = []
        remaining_rows = []
        for i, row in enumerate(rows):
            if row[2] == "0":
                remaining_rows.append(row)
            else:
                rows_deleted.append(row)

    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    return json.dumps(rows_deleted)
