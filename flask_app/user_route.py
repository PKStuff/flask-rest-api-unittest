from flask import Blueprint
from flask_restx import Api, Namespace, Resource
from flask_app.models import User

user_blueprint = Blueprint('User Blueprint', __name__, url_prefix='/user')

app = Api(user_blueprint)
user_namespace = Namespace('user', 'user apis')
user_common_namespace = Namespace('usercommon', 'user common namespace')
app.add_namespace(user_namespace)
app.add_namespace(user_common_namespace)

@user_namespace.route('/')
class UserInfo(Resource):
    def get(self):
        try:
            response = []
            users = User.query.all()
            for user in users:
                response.append(
                    {
                        'id': user.id,
                        'name': user.name
                    }
                )
            return response, 200
        except Exception as e:
            return {'message': 'Something went wrong: {}'.format(e)}, 400

@user_common_namespace.route('/')
class UserCommon(Resource):
    def get(self):
        return {'message': 'common user message..'},200
