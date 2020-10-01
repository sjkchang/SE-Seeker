from flask import Blueprint
from flask_restful import Api
from api.resources.Internship import Internship


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Internship, "/internship/<int:internship_id>")
