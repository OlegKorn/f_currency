from collections import namedtuple as n

from flask import Flask, render_template, redirect, url_for, request

message = n('Message', 'text tag')
messages = []

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)
    

@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(message(text, tag))
    
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
    