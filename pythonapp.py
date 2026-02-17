from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
tasks = []

# Simple HTML UI
HTML_PAGE = """
<!doctype html>
<title>To-Do List</title>
<h1>To-Do List App</h1>
<form action="/tasks" method="post">
  <input type="text" name="task" placeholder="New task" required>
  <input type="submit" value="Add Task">
</form>
<ul>
{% for i, task in enumerate(tasks) %}
  <li>{{ task }} 
      <a href="/tasks/delete/{{ i }}">[Delete]</a>
  </li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PAGE, tasks=tasks)

@app.route("/tasks", methods=["GET"])
def view_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    # Handle form submission from UI
    if request.form:
        task = request.form.get("task")
    else:
        data = request.json
        task = data.get("task")
    if task:
        tasks.append(task)
        return render_template_string(HTML_PAGE, tasks=tasks)
    return jsonify({"error": "Task not provided"}), 400

@app.route("/tasks/delete/<int:index>", methods=["GET"])
def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return render_template_string(HTML_PAGE, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
