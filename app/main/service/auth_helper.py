from app.main.model.user import User
from app.main.service.blacklist_service import save_token

class Auth:

    @staticmethod
    def login_user(data):
        try:
            #Fetching the data of the user
            user=User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token=user.encode_auth_token(user.id)
                if auth_token:
                    object={
                        'status': 'success',
                        'message': 'Successfully logged in',
                        'Authorization': auth_token.decode()
                    }
                    return object,200
            else:
                object={
                        'status': 'fail',
                        'message': 'Email or password does not match',
                    }
                return object,401
        except Exception as e:
            print(e)
            object={
                'status':'fail',
                'message':'Try again'
            }
            return object,500
    
    @staticmethod
    def login_user(data):
        if data:
            auth_token=data.split(" ")[1]
        else:
            auth_token=''
        if auth_token:
            resp=User.decode_auth_token(auth_token)
            if not isinstance(resp,str):
                # Making the auth_token as blacklisted
                return save_token(token=auth_token)
            else:
                object={
                    'status': 'fail',
                    'message': resp
                }
                return object,401
        else:
            object={
                'status': 'fail',
                'message':'Please provide an Authorization Token'
            }
            return object,403

    @staticmethod
    def get_logged_in_user(new_request):
        # Getting the auth_token and decoding it to get the user details
        auth_token=new_request.headers.get('Authorization')
        if auth_token:
            resp=User.decode_auth_token(auth_token)
            if not isinstance(resp,str):
                user=User.query.filter_by(id=resp).first().first()
                object={
                    'status': 'success',
                    'data':{
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    }
                }
                return object,200
            object={
                'status': 'fail',
                'message': resp,
            }
            return object, 401
        else:
            object={
                'status': 'fail',
                'message': 'Provide a valid Authentication Token',
            }
            return object, 401
        
