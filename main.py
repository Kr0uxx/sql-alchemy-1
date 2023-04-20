from datetime import datetime
from data import db_session
from data.users import User
# from data.jobs import Jobs
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/data.db")
    app.run(port=8080, host='127.0.0.1')
