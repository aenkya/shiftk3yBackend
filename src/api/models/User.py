""" User model. Contains properties for the user """

from flask.ext.bcrypt import Bcrypt

from BaseModel import Base, db


bcrypt = Bcrypt()

class User(Base):
    """ User Model """
    __tablename__ = 'users'
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)

    @password
    def password(self):
        return 'Password: Write Only'

    @password.setter
    def password(self, password):
        """ Generate password hash """
        self._password_hash = bcrypt.generate_password_hash(
            password, 4
        ).decode('utf-8')

    def verify_password(self, password):
        """ Check if the provided password matches the user password """
        return bcrypt.check_password_hash(self._password_hash, password)
