# encoding=utf8
# imports
from flask import Flask,request, session,g, redirect, url_for, \
     abort, render_template, flash
from database import db_session

# todoList application

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_todoList():
    tasks = Task.query.all()
    return render_template('show_todoList.html',tasks=tasks)
     

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__=='__main__':
   app.run()
