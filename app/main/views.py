from flask import render_template,url_for
from . import main
from ..requests import get_sources, get_articles


@main.route("/")
def index():
    title="Sources"
    all_news=get_sources()

    return render_template("index.html", title=title, news=all_news)

@main.route("/articles")
def articles():
    title="Articles"
    all_articles=get_articles()


    return render_template("articles.html", title=title, articles=all_articles)