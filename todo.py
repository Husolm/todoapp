from flask import Flask,render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

#App Database and Framework
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Hüseyin Battal/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)

#CompleteTodo
@app.route("/complete/<string:ids>",methods=["GET","POST"])
def completeTodo(ids):
    todoComplete = Todo.query.filter_by(id=ids).first()
    todoComplete.complete = not todoComplete
    db.session.commit()
    return redirect(url_for("index"))

#DeleteTodo
@app.route("/delete/<string:ids>",methods=["GET","POST"])
def deleteTodo(ids):
    deletedValue = Todo.query.filter_by(id=ids).first()
    db.session.delete(deletedValue)
    db.session.commit()
    return redirect(url_for("index"))

#AddTodo
@app.route("/add",methods=["POST"])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

#UpdateTodoStatus


#Database Todo Table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

#Pages
@app.route("/")
def index():
    todo = Todo.query.all()
    return render_template("index.html",todos=todo)


#AppRun
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    