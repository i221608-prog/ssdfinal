import pytest
import json
from app import app, db, Student


@pytest.fixture
def client():
    """Setup test client and database"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


class TestStudentApp:
    """Test suite for Flask Student Management App"""

    def test_app_creation(self):
        """Test that the Flask app is created properly"""
        assert app is not None
        assert app.config['TESTING'] is False

    def test_index_page_loads(self, client):
        """Test GET request to index page"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'<!DOCTYPE' in response.data or b'<!doctype' in response.data.lower()

    def test_add_student(self, client):
        """Test adding a new student"""
        response = client.post('/', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'course': 'Computer Science'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        
        # Verify student was added to database
        with app.app_context():
            student = Student.query.filter_by(name='John Doe').first()
            assert student is not None
            assert student.email == 'john@example.com'
            assert student.course == 'Computer Science'

    def test_get_all_students(self, client):
        """Test retrieving all students"""
        # Add test data
        with app.app_context():
            student1 = Student(name='Alice', email='alice@example.com', course='Physics')
            student2 = Student(name='Bob', email='bob@example.com', course='Math')
            db.session.add(student1)
            db.session.add(student2)
            db.session.commit()
        
        response = client.get('/')
        assert response.status_code == 200

    def test_delete_student(self, client):
        """Test deleting a student"""
        # Add a student first
        with app.app_context():
            student = Student(name='Charlie', email='charlie@example.com', course='English')
            db.session.add(student)
            db.session.commit()
            student_id = student.id
        
        # Delete the student
        response = client.get(f'/delete/{student_id}', follow_redirects=True)
        assert response.status_code == 200
        
        # Verify student was deleted
        with app.app_context():
            deleted_student = Student.query.get(student_id)
            assert deleted_student is None

    def test_update_student_get(self, client):
        """Test GET request to update student page"""
        # Add a student first
        with app.app_context():
            student = Student(name='David', email='david@example.com', course='History')
            db.session.add(student)
            db.session.commit()
            student_id = student.id
        
        response = client.get(f'/update/{student_id}')
        assert response.status_code == 200

    def test_update_student_post(self, client):
        """Test updating a student"""
        # Add a student first
        with app.app_context():
            student = Student(name='Emma', email='emma@example.com', course='Art')
            db.session.add(student)
            db.session.commit()
            student_id = student.id
        
        # Update the student
        response = client.post(f'/update/{student_id}', data={
            'name': 'Emma Updated',
            'email': 'emma.updated@example.com',
            'course': 'Music'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        
        # Verify student was updated
        with app.app_context():
            updated_student = Student.query.get(student_id)
            assert updated_student.name == 'Emma Updated'
            assert updated_student.email == 'emma.updated@example.com'
            assert updated_student.course == 'Music'

    def test_student_model_repr(self):
        """Test Student model __repr__ method"""
        with app.app_context():
            student = Student(id=1, name='Test', email='test@example.com', course='Test')
            assert str(student) == '1 - Test'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
