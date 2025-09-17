from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import text

db = SQLAlchemy()

class Course(db.Model, SerializerMixin):

	__tablename__ = 'courses'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(200), nullable=True)
	credits = db.Column(db.Integer, nullable=False, server_default=text('3'))


	

class Student(db.Model, SerializerMixin):

	__tablename__ = 'students'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)



	courses = db.relationship('Course', back_populates='students')
