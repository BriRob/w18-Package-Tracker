from flask import Flask, render_template
from .config import Config
from .routes.new_package import np
from .models import db, Package
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
# print(app)
app.register_blueprint(np)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def root_endpoint():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)
