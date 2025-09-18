from flask import Flask
from models import db
from routes.cource_routes import course_bp 

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    app.register_blueprint(course_bp, url_prefix='/courses')

    with app.app_context():
        db.create_all()
    @app.route('/')
    def home():
        return "Welcome to the Course API!"
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8080,debug=True)
