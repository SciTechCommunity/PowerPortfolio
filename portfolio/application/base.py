# /application/base.py
from flask import Flask
from os.path import abspath, join, split

application = Flask("PowerPortfolio")
application.secret_key = "SECRET_KEY" # TODO
application.config["DATABASE"] = "sqlite:///portfolio.db"
application.config.from_pyfile('settings.cfg')

root_dir = split(split(abspath(__file__))[0])[0]

@application.route("/")
@application.route("/index.html")
def main_page():
    """ Returns the main index.html page for the website """
    fname = join(root_dir, "static", "user", "index.html")
    with open(fname) as f:
        return f.read()

@application.route("/static/<path>")
def static_route(path):
    """ Route a static resource """
    path = path.split("/")
    fname = join(root_dir, "static", "user", *path)
    with open(fname) as f:
        return f.read()

@application.route("/admin/")
@application.route("/admin/index.html")
def main_page_admin():
    """ Returns the main index.html page for the admin """
    fname = join(root_dir, "static", "admin", "index.html")
    with open(fname) as f:
        return f.read()

@application.route("/admin/static/<path>")
def static_route_admin(path):
    """ Route a static response to part of the admin page """
    path = path.split("/")
    fname = join(root_dir, "static", "admin", *path)
    with open(fname) as f:
        return f.read()
