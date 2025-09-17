from flask import Flask
from models import db, Course, Student
from routes.cource_routes import cource_bp

app = Flask(__name__)

app.register_blueprint(cource_bp)

@app.route('/')
def home():
	pass