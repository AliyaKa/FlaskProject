from flask import Flask, render_template

from blog.views.auth import auth_app, login_manager
from blog.views.users import users_app
from blog.views.articles import articles_app

from blog.models.database import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


app.config["SECRET_KEY"] = 'abcdefg123456'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.register_blueprint(users_app, url_prefix='/users')
app.register_blueprint(articles_app, url_prefix='/articles')
app.register_blueprint(auth_app, url_prefix='/auth')
login_manager.init_app(app)


