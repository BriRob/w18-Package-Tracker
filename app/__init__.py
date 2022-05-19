from flask import Flask, render_template
from .config import Config
from .routes.new_package import new_package



app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(new_package, url_prefix='/new_package')

@app.route("/")
def index():
    return '<h1>Package Tracker</h1>'
