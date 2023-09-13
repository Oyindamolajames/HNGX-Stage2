# imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    def __init__(self, name):
        self.name = name

#db.create_all()

# Define the endpoints
@app.route('/api', methods=['POST'])
def create_person():
    data = request.json
    try:
        if not isinstance(data['name'], str):
            raise TypeError('The name must be a string.')
        new_person = User(name=data['name'])
        db.session.add(new_person)
        db.session.commit()
        message = f"{data['name']} created successfully"
        return jsonify({'message': message}), 201
    except TypeError:
        db.session.rollback()
        return jsonify({'error': "The name must be a string"}), 400


@app.route('/api/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_person(id):
    person = User.query.get(id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    if request.method == 'GET':
        return jsonify({'name': person.name}), 200

    elif request.method == 'PUT':
        data = request.json
        person.name = data['name']
        db.session.commit()
        message = f"{person.name} updated successfully"
        return jsonify({'message': message}), 200

    elif request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        message = f"{person.name} deleted successfully"
        return jsonify({'message': message}), 200


@app.route('/api', methods=['GET'])
def get_data():
    data = User.query.all()
    data_list = [{'id': item.id, 'name': item.name} for item in data]
    return jsonify(data_list), 200






if __name__ == '__main__':
    app.run(debug=True)