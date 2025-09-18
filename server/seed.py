
from app import create_app
from models import db, Course, Student

students = [
	{
		"id": "1",
		"first_name": "John",
		"last_name": "Doe",
		"email": "jd@gmail.com"
	},
	{
		"id": "2",
		"first_name": "Jane",
		"last_name": "Smith",
		"email": "jsmith@gmail.com"
	},
	{
		"id": "3",
		"first_name": "Alice",
		"last_name": "Johnson",
		"email": "alicej@gmail.com"
	},
	{
		"id": "4",
		"first_name": "Bob",
		"last_name": "Brown",
		"email": "bobb@gmail.com"
	},
	{
		"id": "5",
		"first_name": "Carol",
		"last_name": "White",
		"email": "carolw@gmail.com"
	},
	{
		"id": "6",
		"first_name": "David",
		"last_name": "Green",
		"email": "davidg@gmail.com"
	}
]

courses = [
	{
		"id": "1",
		"name": "Mathematics",
		"description": "Basic math course",
		"credits": "3"
	},
	{
		"id": "2",
		"name": "Physics",
		"description": "Introductory physics",
		"credits": "4"
	},
	{
		"id": "3",
		"name": "Chemistry",
		"description": "Fundamentals of chemistry",
		"credits": "3"
	}
]

def seed_data():
	app = create_app()
	with app.app_context():
		db.create_all()
		
		for student_data in students:
			student = Student(
				id=student_data["id"],
				first_name=student_data["first_name"],
				last_name=student_data["last_name"],
				email=student_data["email"]
			)
			db.session.add(student)
		
		for course_data in courses:
			course = Course(
				id=course_data["id"],
				name=course_data["name"],
				description=course_data["description"],
				credits=course_data["credits"]
			)
			db.session.add(course)
		
		db.session.commit()
		print("Database seeded successfully.")

seed_data()