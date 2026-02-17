from flask import Flask, request, render_template_string

app = Flask(__name__)
tasks = []

HTML_PAGE = """
<!doctype html>
<title>To-Do List</title>
<h1>To-Do List App</h1>
<form method="post" action="/add">
    <input type="text" name="task" placeholder="New task" required>
    <input type="submit" value="Add Task">
</form>
<ul>
{% for i, task in enumerate(tasks) %}
  <li>{{ task }} 
      <a href="/delete/{{ i }}">[Delete]</a>
  </li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PAGE, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return render_template_string(HTML_PAGE, tasks=tasks)

@app.route("/delete/<int:index>", methods=["GET"])
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return render_template_string(HTML_PAGE, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
