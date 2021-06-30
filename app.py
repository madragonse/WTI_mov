import flask
from flask import render_template, request
from generator import generate_mp3
from zad import what_lang

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            print(what_lang(request.json['text'])[request.json['text']][-1][0:2])
            generate_mp3(request.json['text'], what_lang(request.json['text'])[request.json['text']][0][0:2])
        except Exception as e:
            print('Launguage not supported')

    return render_template('template.html')



app.run()