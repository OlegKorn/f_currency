from collections import namedtuple as n 
from get_currency_data import *
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
text = "TEST"

@app.route('/', methods=['GET'])
def main():
    
    return render_template('index.html', tickers = data) #берем из файла переменную)
    



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    