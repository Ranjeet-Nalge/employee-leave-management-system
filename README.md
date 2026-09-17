 # Employee Leave Management System

A backend REST API built using Django and Django REST Framework for managing employee leave requests.

## Features

* Create, retrieve, update and delete leave requests
* JWT authentication
* User-specific leave request access
* Leave type management
* Leave status management
* Leave date validation
* Filtering by status and leave type
* Search by leave reason
* Ordering by start date and creation date
* Pagination
* PostgreSQL database
* Docker support
* Docker Compose support

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Simple JWT
* django-filter
* Docker
* Docker Compose

## Project Structure

```
employee_leave_management_system/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── leave/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirement.txt
├── .env.example
├── .gitignore
└── README.md
```

## Leave Types

The system supports three types of leave:

* Sick
* Casual
* Annual

## Leave Status

Leave requests can have the following statuses:

* Pending
* Approved
* Rejected

New leave requests are created with `Pending` status by default.

## API Endpoints

### Authentication

#### Obtain JWT Token

```
POST /api/token/
```

Used to obtain an access token and refresh token using valid user credentials.

#### Refresh JWT Token

```
POST /api/token/refresh/
```

Used to obtain a new access token using a refresh token.

### Leave Requests

#### List Leave Requests

```
GET /api/leaves/
```

Returns leave requests belonging to the authenticated user.

#### Create Leave Request

```
POST /api/leaves/
```

Creates a new leave request for the authenticated user.

Example request body:

```
{
    "leave_type": "Sick",
    "start_date": "2026-09-20",
    "end_date": "2026-09-22",
    "reason": "Fever"
}
```

The `employee` and `status` fields are handled by the backend.

#### Retrieve Leave Request

```
GET /api/leaves/<id>/
```

Returns a specific leave request belonging to the authenticated user.

#### Update Leave Request

```
PUT /api/leaves/<id>/
```

Updates an existing leave request belonging to the authenticated user.

#### Delete Leave Request

```
DELETE /api/leaves/<id>/
```

Deletes an existing leave request belonging to the authenticated user.

## Filtering

Leave requests can be filtered by status and leave type.

### Filter by Status

```
GET /api/leaves/?status=Pending
```

### Filter by Leave Type

```
GET /api/leaves/?leave_type=Sick
```

## Search

Leave requests can be searched using the leave reason.

Example:

```
GET /api/leaves/?search=fever
```

## Ordering

Leave requests can be ordered by start date or creation date.

### Ascending Order

```
GET /api/leaves/?ordering=start_date
```

### Descending Order

```
GET /api/leaves/?ordering=-created_at
```

## Pagination

The API supports pagination for leave request results.

Example:

```
GET /api/leaves/?page=2
```

## Validation

The API validates the leave date range.

The end date cannot be earlier than the start date.

Example validation error:

```
End date cannot be before start date.
```

## Authentication

The API uses JWT authentication.

First obtain an access token:

```
POST /api/token/
```

Then include the access token in the request header:

```
Authorization: Bearer <access_token>
```

Protected leave request endpoints require authentication.

## User-Specific Access

Leave requests are associated with the authenticated employee.

When creating a leave request, the employee is automatically assigned from the authenticated user.

Users can only access their own leave requests through the API.

## Database

The project uses PostgreSQL for data storage.

Database configuration is provided through environment variables.

Example:

```
DB_NAME=leave_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

## Environment Variables

Create a `.env` file using `.env.example` as a reference.

Example:

```
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=leave_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

Do not commit the actual `.env` file or sensitive credentials to the repository.

## Installation

Clone the repository and navigate to the project directory.

Install the required dependencies:

```
pip install -r requirement.txt
```

## Database Migration

Run Django migrations:

```
python manage.py migrate
```

## Run the Development Server

Start the Django development server:

```
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/
```

## Docker

The project includes Docker and Docker Compose configuration for running the Django application with PostgreSQL.

Build and start the containers:

```
docker compose up --build
```

Stop the containers:

```
docker compose down
```

## API Testing

The API can be tested using Postman.

Typical testing flow:

1. Authenticate using `/api/token/`.
2. Copy the JWT access token.
3. Use the token as a Bearer token.
4. Create a leave request using `POST /api/leaves/`.
5. Retrieve leave requests using `GET /api/leaves/`.
6. Update or delete a leave request using its ID.
7. Test filtering, search and ordering.
8. Test date validation.
9. Verify user-specific access.

## Project Purpose

This project was built to practice backend REST API development using Django and Django REST Framework.

The project demonstrates:

* Django models and ORM
* Django REST Framework serializers
* Class-based API views
* CRUD operations
* JWT authentication
* Permissions
* PostgreSQL database integration
* Request validation
* Filtering
* Search
* Ordering
* Pagination
* Docker and Docker Compose
