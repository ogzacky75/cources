from flask import jsonify, Blueprint, request
from flask_restful import Resource, Api
from models import db, Course

cource_bp = Blueprint('courses', __name__, url_prefix='/courses')
api = Api(cource_bp)

class CourseListResource(Resource):
