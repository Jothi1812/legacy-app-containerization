# # # # app.py

# # # def read_names():
# # #     with open('names.txt', 'r') as f:
# # #         return [line.strip() for line in f.readlines()]

# # # def greet():
# # #     names = read_names()
# # #     for name in names:
# # #         print(f"Hello, {name}!")

# # # if __name__ == "__main__":
# # #     greet()



# # # from flask import Flask

# # # app = Flask(__name__)

# # # @app.route('/')
# # # def hello_world():
# # #     return "Hello, World!"



# # from flask import Flask, request, redirect, render_template_string

# # app = Flask(__name__)

# # # In-memory task list (acts like local storage)
# # todo_list = []

# # # HTML Template with card-style UI
# # HTML_TEMPLATE = '''
# # <!DOCTYPE html>
# # <html lang="en">
# # <head>
# #     <meta charset="UTF-8">
# #     <title>Todo List - Card View</title>
# #     <style>
# #         body {
# #             font-family: 'Segoe UI', sans-serif;
# #             background: #f2f4f8;
# #             margin: 0;
# #             padding: 2rem;
# #         }

# #         h1 {
# #             text-align: center;
# #             color: #333;
# #         }

# #         .container {
# #             max-width: 900px;
# #             margin: 0 auto;
# #         }

# #         .form {
# #             display: flex;
# #             justify-content: center;
# #             margin-bottom: 30px;
# #         }

# #         input[type="text"] {
# #             padding: 10px;
# #             width: 60%;
# #             border-radius: 8px;
# #             border: 1px solid #ccc;
# #             font-size: 16px;
# #         }

# #         button {
# #             padding: 10px 16px;
# #             background-color: #007bff;
# #             color: white;
# #             border: none;
# #             border-radius: 8px;
# #             margin-left: 10px;
# #             cursor: pointer;
# #             transition: 0.3s;
# #         }

# #         button:hover {
# #             background-color: #0056b3;
# #         }

# #         .cards {
# #             display: flex;
# #             flex-wrap: wrap;
# #             gap: 20px;
# #             justify-content: center;
# #         }

# #         .card {
# #             background-color: white;
# #             border-radius: 12px;
# #             box-shadow: 0 4px 6px rgba(0,0,0,0.1);
# #             padding: 20px;
# #             width: 250px;
# #             position: relative;
# #         }

# #         .card p {
# #             font-size: 16px;
# #             color: #333;
# #             word-wrap: break-word;
# #         }

# #         .actions {
# #             position: absolute;
# #             bottom: 15px;
# #             right: 15px;
# #         }

# #         .actions form,
# #         .actions a {
# #             display: inline-block;
# #             margin-left: 5px;
# #         }

# #         .edit-button {
# #             background-color: #ffc107;
# #         }

# #         .edit-button:hover {
# #             background-color: #e0a800;
# #         }

# #         .delete-button {
# #             background-color: #dc3545;
# #         }

# #         .delete-button:hover {
# #             background-color: #c82333;
# #         }
# #     </style>
# # </head>
# # <body>
# #     <div class="container">
# #         <h1>Todo List (Card Format)</h1>
# #         <form class="form" method="POST" action="/add">
# #             <input type="text" name="task" placeholder="Enter new task" required>
# #             <button type="submit">Add Task</button>
# #         </form>
# #         <div class="cards">
# #             {% for task in tasks %}
# #             <div class="card">
# #                 <p>{{ task }}</p>
# #                 <div class="actions">
# #                     <a href="/edit/{{ loop.index0 }}"><button class="edit-button">Edit</button></a>
# #                     <form method="POST" action="/delete/{{ loop.index0 }}">
# #                         <button class="delete-button" type="submit">Delete</button>
# #                     </form>
# #                 </div>
# #             </div>
# #             {% endfor %}
# #         </div>
# #     </div>
# # </body>
# # </html>
# # '''

# # @app.route('/')
# # def index():
# #     return render_template_string(HTML_TEMPLATE, tasks=todo_list)

# # @app.route('/add', methods=['POST'])
# # def add():
# #     task = request.form.get('task')
# #     if task:
# #         todo_list.append(task)
# #     return redirect('/')

# # @app.route('/delete/<int:task_id>', methods=['POST'])
# # def delete(task_id):
# #     if 0 <= task_id < len(todo_list):
# #         todo_list.pop(task_id)
# #     return redirect('/')

# # @app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
# # def edit(task_id):
# #     if request.method == 'POST':
# #         new_task = request.form.get('task')
# #         if new_task:
# #             todo_list[task_id] = new_task
# #         return redirect('/')
# #     return f'''
# #         <form method="POST">
# #             <input name="task" value="{todo_list[task_id]}" required>
# #             <button type="submit">Update</button>
# #         </form>
# #     '''


# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=5000, debug=True)


# from flask import Flask, request, redirect, render_template_string, flash
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  
# todo_list = []

# HTML_TEMPLATE = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Enhanced Todo List</title>
#     <style>
#         body {
#             font-family: 'Segoe UI', sans-serif;
#             background: #f2f4f8;
#             margin: 0;
#             padding: 2rem;
#         }

#         h1 {
#             text-align: center;
#             color: #333;
#         }

#         .container {
#             max-width: 900px;
#             margin: 0 auto;
#         }

#         .form {
#             display: flex;
#             justify-content: center;
#             margin-bottom: 30px;
#         }

#         input[type="text"], input[type="datetime-local"] {
#             padding: 10px;
#             width: 40%;
#             border-radius: 8px;
#             border: 1px solid #ccc;
#             font-size: 16px;
#             margin-right: 10px;
#         }

#         button {
#             padding: 10px 16px;
#             background-color: #007bff;
#             color: white;
#             border: none;
#             border-radius: 8px;
#             cursor: pointer;
#             transition: 0.3s;
#         }

#         button:hover {
#             background-color: #0056b3;
#         }

#         .cards {
#             display: flex;
#             flex-wrap: wrap;
#             gap: 20px;
#             justify-content: center;
#         }

#         .card {
#             background-color: white;
#             border-radius: 12px;
#             box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#             padding: 20px;
#             width: 300px;
#             position: relative;
#         }

#         .card p {
#             font-size: 16px;
#             color: #333;
#             word-wrap: break-word;
#         }

#         .card.completed p {
#             text-decoration: line-through;
#             color: #888;
#         }

#         .timestamp, .deadline {
#             font-size: 12px;
#             color: #666;
#             margin-top: 10px;
#         }

#         .deadline.alert {
#             color: red;
#             font-weight: bold;
#         }

#         .actions {
#             margin-top: 15px;
#             display: flex;
#             justify-content: space-between;
#         }

#         .actions form {
#             display: inline-block;
#         }

#         .edit-button {
#             background-color: #ffc107;
#         }

#         .edit-button:hover {
#             background-color: #e0a800;
#         }

#         .delete-button {
#             background-color: #dc3545;
#         }

#         .delete-button:hover {
#             background-color: #c82333;
#         }

#         .filter-buttons {
#             text-align: center;
#             margin-bottom: 20px;
#         }

#         .filter-buttons button {
#             margin: 0 5px;
#         }
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1>Enhanced Todo List</h1>
#         {% with messages = get_flashed_messages() %}
#         {% if messages %}
#         <div style="color: red; text-align: center; margin-bottom: 20px;">
#             {{ messages[0] }}
#         </div>
#         {% endif %}
#         {% endwith %}
#         <form class="form" method="POST" action="/add">
#             <input type="text" name="task" placeholder="Enter new task" required>
#             <input type="datetime-local" name="deadline" required>
#             <button type="submit">Add Task</button>
#         </form>
#         <div class="filter-buttons">
#             <a href="/"><button type="button">All</button></a>
#             <a href="/filter/completed"><button type="button">Completed</button></a>
#             <a href="/filter/pending"><button type="button">Pending</button></a>
#         </div>
#         <div class="cards">
#             {% for task in tasks %}
#             <div class="card {% if task.completed %}completed{% endif %}">
#                 <p>{{ task.text }}</p>
#                 <div class="timestamp">Added: {{ task.timestamp }}</div>
#                 <div class="deadline {% if task.alert %}alert{% endif %}">
#                     Deadline: {{ task.deadline }}
#                 </div>
#                 <div class="actions">
#                     <form method="POST" action="/toggle/{{ loop.index0 }}">
#                         <button class="edit-button" type="submit">
#                             {% if task.completed %}Unmark{% else %}Complete{% endif %}
#                         </button>
#                     </form>
#                     <form method="POST" action="/delete/{{ loop.index0 }}">
#                         <button class="delete-button" type="submit">Delete</button>
#                     </form>
#                 </div>
#             </div>
#             {% endfor %}
#         </div>
#     </div>
# </body>
# </html>
# '''

# @app.route('/')
# def index():

#     current_time = datetime.now()
#     for task in todo_list:
#         task_deadline = datetime.strptime(task['deadline'], '%Y-%m-%dT%H:%M')
#         if not task['completed'] and current_time > task_deadline:
#             task['alert'] = True
#             flash(f"Task '{task['text']}' has passed its deadline!")
#         else:
#             task['alert'] = False
#     return render_template_string(HTML_TEMPLATE, tasks=todo_list)

# @app.route('/filter/<status>')
# def filter_tasks(status):
#     if status == 'completed':
#         filtered_tasks = [task for task in todo_list if task['completed']]
#     elif status == 'pending':
#         filtered_tasks = [task for task in todo_list if not task['completed']]
#     else:
#         filtered_tasks = todo_list
#     return render_template_string(HTML_TEMPLATE, tasks=filtered_tasks)

# @app.route('/add', methods=['POST'])
# def add():
#     task_text = request.form.get('task')
#     deadline = request.form.get('deadline')
#     if task_text and deadline:
#         todo_list.append({
#             'text': task_text,
#             'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#             'deadline': deadline,
#             'completed': False,
#             'alert': False
#         })
#     return redirect('/')

# @app.route('/delete/<int:task_id>', methods=['POST'])
# def delete(task_id):
#     if 0 <= task_id < len(todo_list):
#         todo_list.pop(task_id)
#     return redirect('/')

# @app.route('/toggle/<int:task_id>', methods=['POST'])
# def toggle(task_id):
#     if 0 <= task_id < len(todo_list):
#         todo_list[task_id]['completed'] = not todo_list[task_id]['completed']
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)




from flask import Flask, request, redirect, url_for, session, flash, render_template_string
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import date
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
# app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
# app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'Jothisree@18')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'expense_db')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 3306))



mysql = MySQL(app)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Income & Expense Tracker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-4">

{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
      <div class="alert alert-{{category}} alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
      </div>
    {% endfor %}
  {% endif %}
{% endwith %}

{% if session.loggedin %}
    <h2>Welcome, {{ session.username }}!</h2>
    <a href="{{ url_for('logout') }}" class="btn btn-secondary mb-3">Logout</a>

    <h4>Add Transaction</h4>
    <form method="POST" action="{{ url_for('add') }}">
      <div class="mb-3">
        <label>Description</label>
        <input type="text" class="form-control" name="description" required>
      </div>
      <div class="mb-3">
        <label>Amount</label>
        <input type="number" step="0.01" class="form-control" name="amount" required>
      </div>
      <div class="mb-3">
        <label>Type</label>
        <select class="form-select" name="type" required>
          <option value="expense">Expense</option>
          <option value="income">Income</option>
        </select>
      </div>
      <div class="mb-3">
        <label>Date</label>
        <input type="date" class="form-control" name="date" value="{{ today }}" required>
      </div>
      <button type="submit" class="btn btn-primary">Add</button>
    </form>

    <hr>

    <h4>Transactions</h4>
    <form method="GET" class="row g-3 mb-3">
      <div class="col-auto">
        <input type="date" class="form-control" name="start_date" value="{{ filter.start_date }}">
      </div>
      <div class="col-auto">
        <input type="date" class="form-control" name="end_date" value="{{ filter.end_date }}">
      </div>
      <div class="col-auto">
        <button type="submit" class="btn btn-info">Filter</button>
      </div>
      <div class="col-auto">
        <a href="{{ url_for('index') }}" class="btn btn-secondary">Clear</a>
      </div>
    </form>

    <table class="table table-striped">
      <thead>
        <tr>
          <th>Description</th>
          <th>Amount</th>
          <th>Type</th>
          <th>Date</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
      {% for t in transactions %}
        <tr>
          <td>{{ t.description }}</td>
          <td>{{ '%.2f'|format(t.amount) }}</td>
          <td>{{ t.type.capitalize() }}</td>
          <td>{{ t.date.strftime('%Y-%m-%d') }}</td>
          <td><a href="{{ url_for('delete', id=t.id) }}" class="btn btn-danger btn-sm" onclick="return confirm('Delete this transaction?')">Delete</a></td>
        </tr>
      {% else %}
        <tr><td colspan="5" class="text-center">No transactions found.</td></tr>
      {% endfor %}
      </tbody>
    </table>

    <hr>
    <h4>Summary</h4>
    <p><strong>Total Income:</strong> {{ total_income }}</p>
    <p><strong>Total Expense:</strong> {{ total_expense }}</p>
    <p><strong>Net Profit:</strong> {{ net_profit }}</p>

{% else %}
    <h2>Login</h2>
    <form method="POST" action="{{ url_for('login') }}">
      <div class="mb-3">
        <label>Username</label>
        <input type="text" class="form-control" name="username" required>
      </div>
      <div class="mb-3">
        <label>Password</label>
        <input type="password" class="form-control" name="password" required>
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
    <p class="mt-3">Don't have an account? <a href="{{ url_for('register') }}">Register here</a></p>

{% endif %}
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

def user_exists(username):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    cursor.close()
    return user

@app.route('/')
def index():
    if not session.get('loggedin'):
        return redirect(url_for('login'))

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM transactions WHERE user_id=%s"
    params = [session['id']]

    if start_date and end_date:
        query += " AND date BETWEEN %s AND %s ORDER BY date DESC"
        params.extend([start_date, end_date])
    else:
        query += " ORDER BY date DESC"

    cursor.execute(query, tuple(params))
    transactions = cursor.fetchall()

    # Calculate totals
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    net_profit = total_income - total_expense

    cursor.close()

    return render_template_string(HTML_TEMPLATE,
                                  transactions=transactions,
                                  total_income=f"${total_income:.2f}",
                                  total_expense=f"${total_expense:.2f}",
                                  net_profit=f"${net_profit:.2f}",
                                  today=date.today(),
                                  filter={'start_date': start_date or '', 'end_date': end_date or ''})

@app.route('/add', methods=['POST'])
def add():
    if not session.get('loggedin'):
        flash("You need to log in first.", "warning")
        return redirect(url_for('login'))

    description = request.form.get('description')
    amount = request.form.get('amount')
    ttype = request.form.get('type')
    date_val = request.form.get('date')

    if not description or not amount or not ttype or not date_val:
        flash("All fields are required.", "danger")
        return redirect(url_for('index'))

    try:
        amount = float(amount)
    except ValueError:
        flash("Invalid amount.", "danger")
        return redirect(url_for('index'))

    if ttype not in ['income', 'expense']:
        flash("Invalid transaction type.", "danger")
        return redirect(url_for('index'))

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO transactions (user_id, description, amount, type, date) VALUES (%s, %s, %s, %s, %s)",
                   (session['id'], description, amount, ttype, date_val))
    mysql.connection.commit()
    cursor.close()

    flash("Transaction added successfully.", "success")
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    if not session.get('loggedin'):
        flash("You need to log in first.", "warning")
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM transactions WHERE id=%s AND user_id=%s", (id, session['id']))
    mysql.connection.commit()
    cursor.close()

    flash("Transaction deleted.", "info")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('loggedin'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        user = user_exists(username)
        if user and user['password'] == password:  # Use hashed passwords in production!
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            flash("Logged in successfully.", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password.", "danger")

    return render_template_string(HTML_TEMPLATE)

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('loggedin'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        confirm = request.form.get('confirm').strip()

        if not username or not password or not confirm:
            flash("All fields are required.", "danger")
            return redirect(url_for('register'))

        if password != confirm:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('register'))

        if user_exists(username):
            flash("Username already exists.", "danger")
            return redirect(url_for('register'))

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cursor.close()

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('login'))

    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Register</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-4">
  <h2>Register</h2>
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
      {% for category, message in messages %}
        <div class="alert alert-{{category}} alert-dismissible fade show" role="alert">
          {{ message }}
          <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
      {% endfor %}
    {% endif %}
  {% endwith %}
  <form method="POST">
    <div class="mb-3">
      <label>Username</label>
      <input type="text" class="form-control" name="username" required>
    </div>
    <div class="mb-3">
      <label>Password</label>
      <input type="password" class="form-control" name="password" required>
    </div>
    <div class="mb-3">
      <label>Confirm Password</label>
      <input type="password" class="form-control" name="confirm" required>
    </div>
    <button type="submit" class="btn btn-primary">Register</button>
  </form>
  <p class="mt-3">Already have an account? <a href="{{ url_for('login') }}">Login here</a></p>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
