from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

# Load environment variables from .env file (if you have one)
load_dotenv()

app = Flask(__name__)
tasks = []

@app.route('/')
def task_list():
    return render_template('task_list.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('task_list'))

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('task_list'))

if __name__ == '__main__':
    # Use environment variables or provide a default value for the secret key
    secret_key = os.getenv("SECRET_KEY", "your_default_secret_key")

    # Set the secret key for your Flask application
    app.secret_key = secret_key
    app.run(debug=True)
