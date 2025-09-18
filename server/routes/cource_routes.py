from flask import Blueprint, request
from flask_restful import Resource, Api
from models import db, Course

course_bp = Blueprint('courses', __name__, url_prefix='/courses')
api = Api(course_bp)


class CourseListResource(Resource):
    def get(self):
        #GET
        courses = Course.query.all()
        return [course.to_dict() for course in courses], 200

    def post(self):
        #POST
        data = request.get_json()

        if not data or not data.get('name'):
            return {'error': 'Course name is required'}, 400

        if Course.query.filter_by(name=data['name']).first():
            return {'error': 'Course with this name already exists'}, 400

        credits = data.get('credits', 3)
        try:
            credits = int(credits)
            if credits <= 0:
                return {'error': 'Credits must be positive'}, 400
        except ValueError:
            return {'error': 'Credits must be an integer'}, 400

        course = Course(
            name=data['name'],
            description=data.get('description'),
            credits=credits
        )
        db.session.add(course)
        db.session.commit()

        return course.to_dict(), 201


class CourseResource(Resource):
    def get(self, course_id):
        #GET
        course = Course.query.get(course_id)
        if not course:
            return {'error': 'Course not found'}, 404
        return course.to_dict(), 200

    def put(self, course_id):
        #PUT
        course = Course.query.get(course_id)
        if not course:
            return {'error': 'Course not found'}, 404

        data = request.get_json()

        if 'name' in data:
            existing = Course.query.filter_by(name=data['name']).first()
            if existing and existing.id != course_id:
                return {'error': 'Course with this name already exists'}, 400
            course.name = data['name']

        if 'description' in data:
            course.description = data['description']

        if 'credits' in data:
            try:
                credits = int(data['credits'])
                if credits <= 0:
                    return {'error': 'Credits must be positive'}, 400
                course.credits = credits
            except ValueError:
                return {'error': 'Credits must be an integer'}, 400

        db.session.commit()
        return course.to_dict(), 200

    def delete(self, course_id):
        #DELETE
        course = Course.query.get(course_id)
        if not course:
            return {'error': 'Course not found'}, 404

        db.session.delete(course)
        db.session.commit()
        return {'message': 'Course deleted successfully'}, 200


api.add_resource(CourseListResource, '')
api.add_resource(CourseResource, '/<int:course_id>')
