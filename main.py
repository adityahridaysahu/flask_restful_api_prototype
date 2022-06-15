from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///complaints_database.db'
db = SQLAlchemy(app)

class ComplaintModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	subject = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(500), nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(Complaint_Title = {subject}, Description = {description}, Likes = {likes})"


complaint_put_args = reqparse.RequestParser()
complaint_put_args.add_argument("subject", type=str, help="A Complaint Title is Required!", required=True)
complaint_put_args.add_argument("description", type=str, help="A Complaint Description is Required!", required=True)
complaint_put_args.add_argument("likes", type=int, help="Likes on the complaint", required=True)

complaint_update_args = reqparse.RequestParser()
complaint_update_args.add_argument("subject", type=str, help="Complaint Title")
complaint_update_args.add_argument("description", type=str, help="Complaint Description")
complaint_update_args.add_argument("likes", type=int, help="Likes on the video")

resource_fields = {
	'id': fields.Integer,
	'subject': fields.String,
	'description': fields.String,
	'likes': fields.Integer
}

class Complaint(Resource):
	@marshal_with(resource_fields)
	def get(self, complaint_id):
		result = ComplaintModel.query.filter_by(id=complaint_id).first()
		if not result:
			abort(404, message="Could not find any complaint with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, complaint_id):
		args = complaint_put_args.parse_args()
		result = ComplaintModel.query.filter_by(id=complaint_id).first()
		if result:
			abort(409, message="That complaint ID is already taken...")

		complaint = ComplaintModel(id=complaint_id, subject=args['subject'], description=args['description'], likes=args['likes'])
		db.session.add(complaint)
		db.session.commit()
		return complaint, 201

	@marshal_with(resource_fields)
	def patch(self, complaint_id):
		args = complaint_update_args.parse_args()
		result = ComplaintModel.query.filter_by(id=complaint_id).first()
		if not result:
			abort(404, message="Complaint doesn't exist, cannot update!")

		if args['subject']:
			result.subject = args['subject']
		if args['description']:
			result.description = args['description']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()

		return result


	def delete(self, complaint_id):
		result = ComplaintModel.query.filter_by(id=complaint_id).first()
		if not result:
			abort(404, message="Complaint doesn't exist, cannot delete!")
		db.session.delete(result)
		return '', 204


api.add_resource(Complaint, "/complaint/<int:complaint_id>")

if __name__ == "__main__":
	app.run(debug=True)