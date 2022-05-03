from flask import render_template,url_for
from . import main
from ..requests import get_sources


@main.route("/")
def index():
    title="Sources"
    all_news=get_sources()

    return render_template("index.html", title=title, news=all_news)