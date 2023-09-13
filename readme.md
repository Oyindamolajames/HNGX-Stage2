# Flask API Documentation

## Author Name

Ogunsanya James

## Introduction

This documentation provides an overview of the Flask-based API, including its endpoints and functionality. The API allows you to create, retrieve, update, and delete user records in a SQLite database.

## API Endpoints

### Create a New User

- **Endpoint**: `/api` (POST)
- **Description**: This endpoint allows you to create a new user by providing a JSON payload with the user's name.
- **Request Body**:
  - `name` (string): The name of the user to be created.
- **Responses**:
  - `201 Created`: The user was successfully created.
    - JSON Response: `{'message': 'User name created successfully'}`

  - `400 Bad Request`: If the provided data is invalid (e.g., name is not a string).
    - JSON Response: `{'error': 'The name must be a string'}`

### Retrieve User Information

- **Endpoint**: `/api/<int:id>` (GET)
- **Description**: This endpoint allows you to retrieve information about a user by providing their unique identifier (`id`).
- **Responses**:
  - `200 OK`: The user was found, and their information is returned.
    - JSON Response: `{'name': 'User Name'}`

  - `404 Not Found`: If the user with the provided `id` does not exist.
    - JSON Response: `{'error': 'User not found'}`

### Update User Information

- **Endpoint**: `/api/<int:id>` (PUT)
- **Description**: This endpoint allows you to update the name of an existing user by providing their unique identifier (`id`) and a new name.
- **Request Body**:
  - `name` (string): The new name for the user.
- **Responses**:
  - `200 OK`: The user's name was successfully updated.
    - JSON Response: `{'message': 'User name updated successfully'}`

  - `404 Not Found`: If the user with the provided `id` does not exist.
    - JSON Response: `{'error': 'User not found'}`

### Delete a User

- **Endpoint**: `/api/<int:id>` (DELETE)
- **Description**: This endpoint allows you to delete an existing user by providing their unique identifier (`id`).
- **Responses**:
  - `200 OK`: The user was successfully deleted.
    - JSON Response: `{'message': 'User name deleted successfully'}`

  - `404 Not Found`: If the user with the provided `id` does not exist.
    - JSON Response: `{'error': 'User not found'}`

### Retrieve All Users

- **Endpoint**: `/api` (GET)
- **Description**: This endpoint allows you to retrieve a list of all users in the database.
- **Responses**:
  - `200 OK`: The list of users is returned.
    - JSON Response: `[{'id': 1, 'name': 'User 1'}, {'id': 2, 'name': 'User 2'}, ...]`

## Usage

To use the API, you can make HTTP requests to the specified endpoints using a tool like `curl` or by building a frontend application that interacts with the API.

### Example Usage

- **Create a New User**:
  ```shell
  curl -X POST -H "Content-Type: application/json" -d '{"name": "James"}' http://localhost:5000/api
  ```

- **Retrieve User Information**:
  ```shell
  curl http://localhost:5000/api/1
  ```

- **Update User Information**:
  ```shell
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' http://localhost:5000/api/1
  ```

- **Delete a User**:
  ```shell
  curl -X DELETE http://localhost:5000/api/1
  ```

- **Retrieve All Users**:
  ```shell
  curl http://localhost:5000/api
  ```

## Database

The application uses an SQLite database (`database.db`) to store user information. You can configure the database connection in the `SQLALCHEMY_DATABASE_URI` configuration option in the Flask app.

## Dependencies

This application uses the following Python libraries:

- Flask: A micro web framework for building web applications.
- Flask-SQLAlchemy: An extension for Flask that simplifies database integration.

## How to Run the Application

Follow these steps to run the application:

1. **Clone the GitHub Repository**: Begin by cloning the GitHub repository to your local machine using Git.

2. Activate the virtual environment if you're using one.

    ```
   python -m venv
   source venv/bin/activate
   ```

3. **Install Dependencies**: Install the required Python packages listed in `requirements.txt`. You can do this using `pip`:
   
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**: To start the application, execute the `app.run(debug=True)` line within the script. The API will be accessible at `http://localhost:5000/api`.

   Example:
   
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

4. **Access the API**: You can now access the API by opening a web browser or using an HTTP client like `curl`. The base URL for the API is `http://localhost:5000/api`.

