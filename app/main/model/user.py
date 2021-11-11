import datetime
import jwt

from app.main import db,flask_bcrypt
from app.main.model.blacklist import BlacklistToken
from app.main.config import key

class User(db.Model): #Declaring the User Class as a model for SQLALCHEMY
    # User Model for storing user details.
    __tablename__='user'

    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    email=db.Column(db.String, unique=True, nullable=False)
    registered_on=db.Column(db.DateTime, nullable=False)
    admin=db.Column(db.Boolean, nullable=False,default=False)
    public_id=db.Column(db.String,unique=True)
    username=db.Column(db.String)
    password_hash=db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash=flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self,password):
        return flask_bcrypt.check_password_hash(self.password_hash,password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)


# For Encoding of the auth_token

def encode_auth_token(self, user_id):

    """Generating the Auth Token, return: string
    """
    try:
        payload={
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            key,
            algorithm='HS256'
        )
    except Exception as e:
        return str(e)

# For Decoding of the auth_token

@staticmethod
def decode_auth_token(auth_token):
    """
    Decoding of the auth_token
    :parameters auth_token:
    :returns: integer|string
    """
    try:
        payload= jwt.decode(auth_token, key)
        is_blacklisted_token=BlacklistToken.check_blacklist(auth_token)
        if is_blacklisted_token:
            return 'Token blacklisted. Please log in again'
        else:
            return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again'

