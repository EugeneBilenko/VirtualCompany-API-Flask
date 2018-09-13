from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse, inputs, fields
import models


virtualco_fields = {
	'id': fields.Integer,
	'name': fields.String
}

class VirtualCoList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'name',
			required=True,
			help='VC not provided',
			location=['form', 'json']
		)
		super().__init__()
		
	def get(self):
		return jsonify({'VirtualCo': [{'name': 'Membranco CORP'}]})
		
	def post(self):
		args = self.reqparse.parse_args()
		models.VirtualCo.create(**args)
		return jsonify({'VirtualCo': [{'name': 'Shigaro LLC'}]})
		
class VirtualCo(Resource):
	def get(self, id):
		return jsonify({'name': [{'Membranco CORP'}]})
		
	def put(self, id):
		return jsonify({'name': [{'Membranco CORP'}]})
		
	def delete(self, id):
		return jsonify({'name': [{'Membranco CORP'}]})
		
virtualco_api = Blueprint('resources.courses', __name__)
api = Api(virtualco_api)
api.add_resource(
	VirtualCoList,
	'/api/v1/vcs',
	endpoint='vcs'
)
api.add_resource(
	VirtualCo,
	'/api/v1/vc/<int:id>',
	endpoint='vc'
)