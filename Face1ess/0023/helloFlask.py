from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_Flask():
    return 'hello flask!'

@app.route('/search_yunpan')
def search_yunpan():
    return 'search_yunpan page!'

@app.route('/run')
def run():
    return 'run page'

if __name__ == '__main__':
    app.run()
