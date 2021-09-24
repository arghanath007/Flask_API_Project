from flask import request
from flask_restx import Resource

from  app.main.util.dto import  UserDto
from app.main.service.user_service import save_new_user,get_all_users,get_a_user

api=UserDto.api
_user=UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user,envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()


    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User"""
        data=request.json
        return save_new_user(data=data)

     
@api.route('/<public_id>')
class User(Resource):
    @api.param('public_id','Identification of the user')
    @api.response(404, 'User not found.')
    @api.doc('getting a single user')
    # @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user= get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
