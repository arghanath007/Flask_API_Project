from app.main import db
import datetime

class BlacklistToken(db.Model):
    """
    Modeling Token for storing the JWT tokens 
    """

    __tablename__='blacklist_tokens'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    token=db.Column(db.String, unique=True, nullable=False)
    blacklisted_on=db.Column(db.DateTime, nullable=False)


    def __init__(self,token):
        self.token=token
        self.blacklisted_on=datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # Checking to see if the 'auth_token' is blacklisted or not.
        res=BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False