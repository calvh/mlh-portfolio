import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/<person>')
def index(person):
    profile_picture = {'Josue': './static/img/miyabi.jpg',
                 'Carolina': './static/img/logo.jpg',
                 'Calvin': './static/img/logo.jpg'}
    description = {'Josue': 'Howdy I\'m Josue from Texas',
                 'Carolina': 'Hello I\'m Caro from Mexico',
                 'Calvin': 'Hellow I\'m Cal from Canada'}
    return render_template('index.html', title=person, profile_picture=profile_picture , description=description, url=os.getenv("URL"))
