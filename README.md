# Flask MongoDB CRUD Application (with Docker)

This project is a simple and clean implementation of a **Flask-based REST API** for performing CRUD operations on a MongoDB database. It focuses on managing user information and is containerized using Docker for easy deployment.

---

## Why this project?

The aim was to build a small but scalable backend application using Python’s Flask framework and MongoDB as the database. Docker is used to ensure easy environment setup and portability.

---

## Features

- REST API built with Flask
- MongoDB integration using PyMongo
- Modular code organization (separated into config, models, services, and routes)
- Docker support for running the entire stack easily
- Postman support for testing

---

## Tech Stack

- **Backend**: Python (Flask)
- **Database**: MongoDB
- **Containerization**: Docker + Docker Compose

---

## Project Structure

```
flask_mongo_crud/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   └── user_model.py
│   ├── routes/
│   │   └── user_routes.py
│   └── services/
│       └── user_service.py
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## User Schema

Each user has the following fields:

- `id`: (automatically generated ObjectId)
- `name`: Name of the user
- `email`: Email address (must be unique)
- `password`: Password (plaintext in this example)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/akashdavidramisetti/flask-mongo-crud.git
cd flask-mongo-crud
```

### 2. Run using Docker

```bash
docker-compose up --build
```

- Flask app runs at: `http://localhost:5000`
- MongoDB is exposed internally and used by Flask via Docker network

---

## API Endpoints

| Method | Endpoint         | Action                 |
|--------|------------------|------------------------|
| GET    | `/users`         | List all users         |
| GET    | `/users/<id>`    | Get a single user      |
| POST   | `/users`         | Create a new user      |
| PUT    | `/users/<id>`    | Update existing user   |
| DELETE | `/users/<id>`    | Delete a user          |

---

## Testing with Postman

You can manually test each endpoint using Postman or any REST client.

Example `POST /users` body:

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "password": "mysecurepassword"
}
```
## Final Notes
This project is built with the intention of being **simple to understand, modular in design**, and **easy to test or scale**. While it’s basic, it provides a strong foundation for building out more complex Flask-Mongo apps in the future.
---
Built with by AkashDavid Ramisetti
