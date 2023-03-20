import os
from flask import Flask, render_template
from flask_migrate import Migrate
from blog.views.auth import auth_app, login_manager
from blog.views.users import users_app
from blog.views.articles import articles_app

from blog.models.database import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.config.{cfg_name}")


db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(users_app, url_prefix='/users')
app.register_blueprint(articles_app, url_prefix='/articles')
app.register_blueprint(auth_app, url_prefix='/auth')
login_manager.init_app(app)

