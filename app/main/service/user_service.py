import uuid
import datetime


from app.main import db
from app.main.model.user import User
from app.main.util.database import save_changes



def save_new_user(data):
    try:
        user=User.query.filter_by(email=data['email']).first()
        if not user:
            new_user=User(
                public_id=str(uuid.uuid4()),
                email=data['email'],
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow()
            )
            save_changes(new_user,'user')
            return generate_token(new_user)
            # response_object={
            #     'status': 'success',
            #     'message': 'Successfully registered.'
            # }
            # return response_object,201
        else:
            response_object={
                'status':'fail',
                'message':'User already exists. Please Log in',
            }
            return response_object,409
    except Exception as e:
        return {
            "error": str(e)
        },500


def get_all_users():
    data=[]
    users=User.query.all()
    for user in users:
        object={
            'email': user.email,
            'username': user.username,
        }
        data.append(object)
    return {"data": data},200


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

def generate_token(user):
    try:
        # Generation of the auth_token
        auth_token=user.encode_auth_token(user.id)
        object={
            'status': 'success',
            'message': 'Successfully registered',
            'Authorization': auth_token.decode()
        }
        return object,201
    except Exception as e:
        object={
            'status':'fail',
            'message':'Some error occurred. Please try again.'
        }
        return object,401

# def save_changes(data):
#     db.session.add(data)
#     db.session.commit()

