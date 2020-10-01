from api.utils.database import db


class InternshipModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Internship(Company = {self.company}, date = {self.date}, description = {self.description})"
