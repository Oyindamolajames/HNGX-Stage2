import unittest
import json
from app import app, db, User

class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an SQLite in-memory database for testing
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_person(self):
        data = {'name': 'John Doe'}
        response = self.app.post('/api', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'John Doe created successfully')

    def test_create_person_invalid_name(self):
        data = {'name': 123}  # Invalid data (name must be a string)
        response = self.app.post('/api', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'The name must be a string')

    def test_manage_person_get(self):
        # Create a person first
        new_person = User(name='Alice')
        db.session.add(new_person)
        db.session.commit()

        response = self.app.get(f'/api/{new_person.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Alice')

    def test_manage_person_put(self):
        # Create a person first
        new_person = User(name='Alice')
        db.session.add(new_person)
        db.session.commit()

        data = {'name': 'Updated Name'}
        response = self.app.put(f'/api/{new_person.id}', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Updated Name updated successfully')

    def test_manage_person_delete(self):
        # Create a person first
        new_person = User(name='Alice')
        db.session.add(new_person)
        db.session.commit()

        response = self.app.delete(f'/api/{new_person.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Alice deleted successfully')

    def test_manage_person_not_found(self):
        response = self.app.get('/api/999')  # Assuming ID 999 does not exist
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Person not found')

    def test_get_data(self):
        # Create some test persons
        new_person1 = User(name='Alice')
        new_person2 = User(name='Bob')
        db.session.add_all([new_person1, new_person2])
        db.session.commit()

        response = self.app.get('/api')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)  # Check if two persons are returned

if __name__ == '__main__':
    unittest.main()
