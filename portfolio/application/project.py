# /application/project.py
from portfolio.models import Project, needs_db
from portfolio.application import application

from flask import abort, jsonify, request

@application.route("/api/projects/count")
@needs_db
def project_count(db_session):
    """ Returns the number of projects in the portfolio. """
    count = db_session.query(Project).count()

    return jsonify(**{
        "count": count
    })

@application.route("/api/projects/<int:key>")
@needs_db
def project_read(db_session, key):
    """ Returns the information about a project from its ID. """
    data = db_session.query(
            Project
        ).filter(
            Project.key == key
        )
    if data.count() == 1:
        user = data.one()
        return jsonify(**user.to_json())
    else:
        return jsonify(**{"error": "project not found"})

@application.route("/admin/api/projects/new", methods=["POST"])
@needs_db
#@needs_login -- not yet implemented
def project_new(db_session):
    """ Creates a new project. """
    data = request.get_json()

    if data is None:
        abort(400)

    if "name" not in data:
        abort(400)
    if "url" not in data:
        abort(400)
    if "description" not in data:
        abort(400)

    project = Project(
            name=data["name"],
            url=data["url"],
            description=data["description"]
    )

    try:
        db_session.add(project)
        db_session.commit()
        return ("", 204)
    except IntegrityError:
        return jsonify(**{"error": "project could not be added"})

@application.route("/admin/api/projects/<int>", methods=["POST"])
@needs_db
#@needs_login -- not yet implemented
def project_write(db_session, key):
    abort(503)
