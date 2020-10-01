from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from api.utils.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from api.models.internship_model import InternshipModel
    from api.utils.database import db
    db.init_app(app)
    with app.app_context():
        # from api.models import *
        db.create_all()

    return app
