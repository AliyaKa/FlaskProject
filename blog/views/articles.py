from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint('articles_app', __name__)

ARTICLES = ['Flask', 'Django', 'JSON:API']


@articles_app.route('/', endpoint='list')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)


@articles_app.route('/<string:title>', endpoint='details')
def article_details(title: str):
    title_id = ARTICLES.index(title)
    try:
        article_name = ARTICLES[title_id]
    except KeyError:
        raise NotFound(f"Article #{title} doesn't exists!")
    return render_template('articles/details.html', title=title, article_name=article_name)
