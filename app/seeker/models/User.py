from .. import db, login_manager, bcrypt
# from ..models.UserInternship import UserInternship
from flask_login import UserMixin


@login_manager.user_loader
def load_user(userId):
    """
    Loads user
    Parameters
    ----------
    userId
        the id of the user being loaded
    """
    return User.query.get(int(userId))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    #internships = db.relationship('Internship', backref='Poster', lazy=True)

    def __repr__(self):
        return f'<user: {self.username}, email: {self.email}>'

    @classmethod
    def create(cls, username, email, password):
        password_hash = bcrypt.generate_password_hash(password)
        user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def edit(cls, id, username, email, new_password):
        user = db.session.query(User).filter_by(id=id).first()
        password_hash = bcrypt.generate_password_hash(new_password)
        user.username = username
        user.email = email
        user.password_hash = password_hash
        db.session.commit()

    @classmethod
    def usernameExists(cls, username):
        user = db.session.query(User).filter_by(username=username).first()
        if user:
            return True
        else:
            return False

    @classmethod
    def emailExists(cls, email):
        user = db.session.query(User).filter_by(email=email).first()
        if user:
            return True
        else:
            return False

    @classmethod
    def passwordMatches(self, email, password):
        tempUser = db.session.query(User).filter_by(email=email).first()
        if tempUser and bcrypt.check_password_hash(tempUser.password_hash, password):
            return True
        else:
            return False

    @classmethod
    def passwordMatchesID(self, id, password):
        tempUser = db.session.query(User).filter_by(id=id).first()
        if tempUser and bcrypt.check_password_hash(tempUser.password_hash, password):
            return True
        else:
            return False
