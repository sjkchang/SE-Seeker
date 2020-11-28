from .. import db


class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), index=True, nullable=False)
    term = db.Column(db.String(100), index=True, nullable=False)
    year = db.Column(db.Integer, index=True, nullable=False)
    location = db.Column(db.String(100), index=True, nullable=False)
    additional_information = db.Column(db.String(800), index=True, nullable=True)
    link = db.Column(db.String(100), index=True, nullable=False)
    # user = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=True)

    def __repr__(self):
        return f'<Company: {self.company}, Date: {self.term} {self.year}, Location: {self.location}, Link: {self.link}'

    @classmethod
    def create(cls, company, term, year, location, additional_information, link):
        internship = Internship(company=company, term=term, year=year, location=location, additional_information=additional_information, link=link)
        db.session.add(internship)
        db.session.commit()

    @classmethod
    def delete(cls, id, currentUser):
        internship = db.session.query(Internship).filter_by(id=id)
        db.session.delete(internship)
        db.session.commit()

    @classmethod
    def alreadyExists(cls, link):
        internship = db.session.query(Internship).filter_by(link=link).first()
        if internship:
            return True
        else:
            return False
