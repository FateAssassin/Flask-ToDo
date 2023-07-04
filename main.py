from flask import Flask, render_template, redirect, request, url_for, flash
import sqlite3
import datetime

app = Flask(__name__)
table_name_list = ["todo"]
app.secret_key = 'the random string'

class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKCYAN = '\033[96m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

def checkdatabase(table_list):
    con = sqlite3.connect("todo.db")
    cursor = con.cursor()
    for table_name in table_list:
        query = cursor.execute(f"SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='todo'")

        result = query.fetchone()
        if str(result)=="(1,)":
            print(f"{bcolors.OKCYAN}{table_name} exists.{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}{table_name} does not exist.{bcolors.ENDC}")
            try:
                con.execute(f"CREATE TABLE `todo` (`todo` TEXT, `id` BIGINT) ;")
                con.commit()
                cursor = con.cursor()
                print(f"{bcolors.OKCYAN}Created the table to-do succesfully{bcolors.ENDC}")
            except Exception as e:
                print(f"{bcolors.FAIL}ERROR: {e}{bcolors.ENDC}")
                con.rollback()
    print('The databases are checked.')
    return

def get_todos():
   conn = sqlite3.connect('todo.db')
   c = conn.cursor()

   c.execute("SELECT * FROM todo")
   todos = c.fetchall()
   conn.close()
   return todos

@app.route("/")
def index():
   todos = get_todos()

   return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
   conn = sqlite3.connect('todo.db')
   c = conn.cursor()
   todo = request.form.get("todo")
   if todo == "":
      flash("Please enter a To-Do.")
      return redirect(url_for("index"))
   
   query = c.execute("select * FROM todo ORDER BY id DESC LIMIT 1")
   query = query.fetchall()

   if len(query) == 0:
      id = 1
   else:
      id = query[0][1] + 1
   print(query)

   c.execute("INSERT INTO todo VALUES (?, ?)", (request.form.get("todo"), id))
   conn.commit()
   conn.close()
   return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
   conn = sqlite3.connect('todo.db')
   c = conn.cursor()
   c.execute("DELETE FROM todo WHERE id=?", (id,))
   conn.commit()
   conn.close()
   return redirect(url_for("index"))
   

if __name__ == '__main__':
   checkdatabase(table_name_list)
   app.run(debug=True)

