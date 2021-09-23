from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth
from app.main.util.dto import  AuthDto

api=AuthDto.api
user_auth=AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    """
    Login Resources of the user
    """
    @api.doc('User Login')
    @api.expect(user_auth,validate=True)
    def post(self):
        # Getting the data of the Post request
        post_data=request.json
        return Auth.login_user(data=post_data)

@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resources of the user
    """
    @api.doc('User Logout')
    def post(self):
        # Getting the auth_token
        auth_header=request.headers.get('Authorization')
        return Auth.login_user(data=auth_header)
