# pythonapp.py
from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["GET"])
def view_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json.get("task")
    tasks.append(task)
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<int:index>", methods=["DELETE"])
def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        return jsonify({"message": f"Removed task: {removed}"})
    return jsonify({"error": "Invalid index"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
