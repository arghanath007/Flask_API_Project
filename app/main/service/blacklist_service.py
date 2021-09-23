from app.main import db
from app.main.model.blacklist import BlacklistToken
from app.main.util.database import save_changes


def save_token(token):
    blacklist_token=BlacklistToken(token=token)
    try:
        #Inserting the token
        object={
            'status':'success',
            'message': 'Successfully logged in',
            'token': blacklist_token
        }
        return save_changes(object,'blacklisted_token'), 200
    except Exception as e:
        object={
            'status':'fail',
            'message': str(e)
        }
        return object, 200
        