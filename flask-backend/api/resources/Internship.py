from flask_restful import Resource, reqparse, fields, marshal_with
from api.models.internship_model import InternshipModel
from api.utils.database import db


internship_put_args = reqparse.RequestParser()
internship_put_args.add_argument("company", type=str, help="Name of the Company is required", required=True)
internship_put_args.add_argument("date", type=str, help="When the internship occurs, ex. Summer2021")
internship_put_args.add_argument("description", type=str, help="Description of the internship")

resource_fields = {
    'id': fields.Integer,
    'company': fields.String,
    'date': fields.String,
    'description': fields.String
}


class Internship(Resource):
    @marshal_with(resource_fields)
    def get(self, internship_id):
        result = InternshipModel.query.filter_by(id=internship_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, internship_id):
        args = internship_put_args.parse_args()
        internship = InternshipModel(id=internship_id, company=args['company'], date=args['date'], description=args['description'])
        db.session.add(internship)
        db.session.commit()
        return internship, 201
