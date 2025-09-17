from flask import jsonify, Blueprint, request
from flask_restful import Resource, Api
from models import db, Course

course_bp = Blueprint('courses', __name__, url_prefix='/courses')
api = Api(course_bp)

class CourseListResource(Resource):
    def get(self):
        courses = Course.query.all()
        return jsonify([course.to_dict() for course in courses])

    def post(self):
        data = request.get_json()
       
        if not data.get('name'):
            return {'error': 'Course name is required'}, 400
        
        
        if Course.query.filter_by(name=data['name']).first():
            return {'error': 'Course with this name already exists'}, 400

        course = Course(
            name=data['name'],
            description=data.get('description'),
            credits=data.get('credits', 3)
        )
        db.session.add(course)
        db.session.commit()
        return course.to_dict(), 201

class CourseResource(Resource):
    def get(self, course_id):
        course = Course.query.get_or_404(course_id)
        return course.to_dict()

    def put(self, course_id):
        course = Course.query.get_or_404(course_id)
        data = request.get_json()

        if 'name' in data:
            existing = Course.query.filter_by(name=data['name']).first()
            if existing and existing.id != course_id:
                return {'error': 'Course with this name already exists'}, 400
            course.name = data['name']

        if 'description' in data:
            course.description = data['description']

        if 'credits' in data:
            course.credits = data['credits']

        db.session.commit()
        return course.to_dict()

    def delete(self, course_id):
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        return '', 204

api.add_resource(CourseListResource, '')
api.add_resource(CourseResource, '/<int:course_id>')
