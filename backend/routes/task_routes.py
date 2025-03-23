from flask import Blueprint, jsonify, request
from models import db, Task

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks])

@task_bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    new_task = Task(title=data["title"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added successfully"}), 201
