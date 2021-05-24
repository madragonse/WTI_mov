import flask
from flask import render_template, request
from generator import generate_mp3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        generate_mp3(request.json['text'], request.json['lang'])
        return render_template('template.html')

    return render_template('template.html')



app.run()