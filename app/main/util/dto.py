from flask_restx import Namespace, fields


class UserDto:
    api=Namespace('user', description='user related operations')
    user=api.model('user',{
        'email': fields.String(required=True,description='Email Address of user'),
        'username': fields.String(required=True,description='Username of user'),
        'password': fields.String(required=True,description='Password of user'),
    })

class AuthDto:
    api=Namespace('auth', description='authentication related operations')
    user_auth=api.model('auth_details',{
        'email': fields.String(required=True,description='Email Address of the user'),
        'password': fields.String(required=True,description='Password of the user')
    })