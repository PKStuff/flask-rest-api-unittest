from flask import Blueprint
from flask_restx import Api, Resource, Namespace

common_blueprint = Blueprint('Common Blueprint', __name__, url_prefix='/common')
app = Api(common_blueprint)
common_ns = Namespace("Common", 'Common api')

app.add_namespace(common_ns)

@common_ns.route('/')
class CommonInfo(Resource):
    def get(self):
        return {'message': 'Welcome Pradip Sambhaji Kothawale..'}, 200
