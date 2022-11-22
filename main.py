from flask import flask
from config import DevConfig

app = Flask(__watchtower__)
app.config.from_object (DevConfig)

@app.route('/')
def home():
    return '<h1>Im always watching you</h1>'
if _watchtower_ -- '__main__':
    app.run()_
