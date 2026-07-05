# Module 03 – JWT Authentication

## Objective

Implement a secure authentication system for the Distributed Job Scheduler using JWT tokens.

---

## Features Implemented

- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Token Generation
- JWT Validation
- OAuth2 Authentication
- Swagger Authorization Support

---

## Folder Structure

backend/
└── app/
    └── auth/
        ├── hashing.py
        ├── jwt_handler.py
        ├── routes.py
        └── schemas.py

---

## Technologies Used

- FastAPI
- SQLAlchemy
- Passlib
- bcrypt
- python-jose
- OAuth2PasswordBearer

---

## API Endpoints

### Register User

POST /auth/register

Registers a new user.

Request

```json
{
    "username": "admin",
    "email": "admin@test.com",
    "password": "admin123"
}
```

---

### Login User

POST /auth/login

Authenticates the user and returns a JWT access token.

Response

```json
{
    "access_token": "<jwt_token>",
    "token_type": "bearer"
}
```

---

## Security

Passwords are never stored in plain text.

Each password is hashed using bcrypt before being stored.

JWT tokens contain

- user_id
- email
- expiration timestamp

---

## Testing

Successfully tested using Swagger UI.

Verified

- Registration
- Login
- JWT generation
- JWT authorization

---

## Status

✅ Completed