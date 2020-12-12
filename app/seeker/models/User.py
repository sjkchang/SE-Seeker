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

    @classmethod
    def create(cls, username, email, password):
        """Function to create a new User, and add it to the db

        Args:
            username ([String]): New Users username
            email ([String]): New Users Email
            password ([String]): New Users Password
        """
        password_hash = bcrypt.generate_password_hash(password)
        user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def delete(cls, current_user):
        """Function to delete the current user from the DB

        Args:
            current_user ([User]): The user that is going to be deleted
        """
        db.session.delete(current_user)
        db.session.commit()

    @classmethod
    def edit(cls, id, username, email, new_password):
        """Function to edit a users data

        Args:
            id ([Integer]): The user being edited's id
            username ([String]): The new username for the user
            email ([String]): The new email for the user
            new_password ([String]): The new password for the user
        """
        user = db.session.query(User).filter_by(id=id).first()
        password_hash = bcrypt.generate_password_hash(new_password)
        user.username = username
        user.email = email
        user.password_hash = password_hash
        db.session.commit()

    @classmethod
    def usernameExists(cls, username):
        """Checks if a esername is already assigned to a user in database

        Args:
            username ([String]): Username that is being checked if it already exists

        Returns:
            [Boolean]: Returns true if the username is alreeady in use, false if email is new
        """
        user = db.session.query(User).filter_by(username=username).first()
        if user:
            return True
        else:
            return False

    @classmethod
    def emailExists(cls, email):
        """Checks if a email is already assigned to a user in database

        Args:
            email ([String]): Email that is being checked if it already exists

        Returns:
            [Boolean]: Returns true if the email is alreeady in use, false if email is new
        """
        user = db.session.query(User).filter_by(email=email).first()
        if user:
            return True
        else:
            return False

    @classmethod
    def passwordMatches(self, email, password):
        """Checks if a password matches a users email

        Args:
            id ([Interger]): email indicating user in database
            password ([String]): Password checked to match user

        Returns:
            [Booblean]: Returns true if password matches, false if password doesnt match
        """
        tempUser = db.session.query(User).filter_by(email=email).first()
        if tempUser and bcrypt.check_password_hash(tempUser.password_hash, password):
            return True
        else:
            return False

    @classmethod
    def passwordMatchesID(self, id, password):
        """Checks if a password matches a users id

        Args:
            id ([Interger]): Id indicating user in database
            password ([String]): Password checked to match user

        Returns:
            [Booblean]: Returns true if password matches, false if password doesnt match
        """
        tempUser = db.session.query(User).filter_by(id=id).first()
        if tempUser and bcrypt.check_password_hash(tempUser.password_hash, password):
            return True
        else:
            return False
