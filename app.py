from flask import Flask
from models import db
from routes.cource_routes import course_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(course_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
