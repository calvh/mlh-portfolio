import os
from flask import Flask, render_template, send_from_directory
from flask_navigation import Navigation
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Calvin', 'index', {'person': 'Calvin'}),
    nav.Item('Josue', 'index', {'person': 'Josue'}),
    nav.Item('Carolina', 'index', {'person': 'Carolina'})])

@app.route('/', defaults={'person':'Miyabi'})
@app.route('/<person>')
def index(person):
    profile_picture = {'Miyabi': './static/img/miyabi.jpg',
                'Josue': './static/img/miyabi.jpg',
                 'Carolina': './static/img/logo.jpg',
                 'Calvin': './static/img/logo.jpg'}
    description = {'Miyabi': 'Hi I\'m Miyabi Serizawa from the manga Domestic Girlfriend',
                'Josue': 'Howdy I\'m Josue from Texas',
                 'Carolina': 'Hello I\'m Caro from Mexico',
                 'Calvin': 'Hellow I\'m Cal from Canada'}
    return render_template('index.html', title=person, profile_picture=profile_picture , description=description, url=os.getenv("URL"))
