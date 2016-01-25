# /usr/local/bin/python
# encoding=utf8
# all the imports
import sqlite3 
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

from contextlib import closing

# configuration
DATABASE = '/tmp/messagesBook.db'
DEBUG = True
SECRET_KEY = 'development key'

# messageBook
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql',mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()
    g.db.close()

@app.route('/')
def show_messages():
    cur = g.db.execute('select name, text from messages order by id desc')
    messages = [dict(name=row[0],text=row[1]) for row in cur.fetchall()] 
    return render_template('show_messages.html',messages = messages)

@app.route('/add',methods=['POST'])
def add_message():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into messages (name,text) values(?,?)',[request.form['name'],request.form['text']])
    g.db.commit()
    flash('留言成功')
    return redirect(url_for('show_messages'))

if __name__ == '__main__':
    app.run()
