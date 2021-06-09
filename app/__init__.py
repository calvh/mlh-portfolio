import os
from flask import Flask, render_template, send_from_directory
from flask_navigation import Navigation
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
nav = Navigation(app)

<<<<<<< HEAD
nav.Bar(
    "top",
    [
        nav.Item("About Me", "index"),
        nav.Item("Projects", "projects"),
        nav.Item("Contact Me", "contact"),
        nav.Item("Resume", "resume"),
    ],
)


@app.route("/")
def index():
    title = "Miyabi"
    profile_picture = "./static/img/miyabi.jpg"
    description = "about me"
    return render_template(
        "index.html",
        title=title,
        profile_picture=profile_picture,
        description=description,
        url=os.getenv("URL"),
    )


@app.route("/projects")
def projects():
    title = "Projects"
    profile_picture = "./static/img/miyabi.jpg"
    description = "Project"
    return render_template(
        "projects.html",
        title=title,
        profile_picture=profile_picture,
        description=description,
        url=os.getenv("URL"),
    )


@app.route("/contact")
def contact():
    title = "Contact"
    profile_picture = "./static/img/miyabi.jpg"
    description = "contact"
    return render_template(
        "contact.html",
        title=title,
        profile_picture=profile_picture,
        description=description,
        url=os.getenv("URL"),
    )


@app.route("/resume")
def resume():
    title = "Resume"
    profile_picture = "./static/img/miyabi.jpg"
    description = "Resume"
    return render_template(
        "resume.html",
        title=title,
        profile_picture=profile_picture,
        description=description,
        url=os.getenv("URL"),
    )
=======
nav.Bar('top', [
    nav.Item('Calvin', 'index', {'person': 'Calvin'}),
    nav.Item('Josue', 'index', {'person': 'Josue'}),
    nav.Item('Carolina', 'index', {'person': 'Carolina'})])


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', url=os.getenv("URL"))

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
>>>>>>> c2802f7 (Added 404 Page, with proper response)
