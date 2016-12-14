# /admin/__init__.py
from portfolio.application import application
from portfolio.application.base import root_dir

from os.path import join, split
from functools import wraps
from flask import abort, jsonify, request, session
from bcrypt import hashpw

def needs_logged_in(function):
    """
    A function wrapper that ensures the user is logged in before their request
    is processed.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        if "admin" not in session:
            abort(403)
        return function(*args, **kwargs)
    return wrapper

@application.route("/admin/api/login", methods=["POST"])
def login():
    data = request.get_json()
    if data is None:
        abort(400)
    if "password" not in data:
        abort(400)
    # open the password file
    fname = join(split(root_dir)[0], "passwd")
    with open(fname, "rb") as f:
        password = f.readline()
        if hashpw(data["password"].encode("utf-8"), password) == password:
            session["admin"] = True
            return jsonify(**{
                "auth": True
            })
    return jsonify(**{
        "auth": False
    })

@application.route("/admin/api/logout")
def logout():
    if "admin" not in session:
        return jsonify(**{
            "error": "Not logged in"
        })

    session.pop("admin", None)
    return ("", 204)

@application.route("/admin/api/logged_in")
def logged_in():
    if "admin" in session:
        return jsonify(**{
            "auth": True
        })
    return jsonify(**{
        "auth": False
    })
