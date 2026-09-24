# app.py
# Simple Flask server that connects the HTML/JS frontend with our LinkedList.

from flask import Flask, render_template, request, jsonify
from linked_list import LinkedList

app = Flask(__name__)

# One linked list is created when the server starts.
# It stores all the tasks while the app is running.
task_list = LinkedList()


@app.route("/")
def index():
    # Show the main page
    return render_template("index.html")


@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Send all tasks as JSON so JavaScript can show them
    return jsonify(task_list.show_tasks())


@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    task_name = data.get("task", "").strip()
    if task_name != "":
        task_list.add_task(task_name)
    return jsonify(task_list.show_tasks())


@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):
    task_list.delete_task(index)
    return jsonify(task_list.show_tasks())


@app.route("/complete/<int:index>", methods=["POST"])
def complete_task(index):
    task_list.complete_task(index)
    return jsonify(task_list.show_tasks())


if __name__ == "__main__":
    app.run(debug=True)
