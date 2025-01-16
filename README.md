# Nava Organization Management API

A FastAPI-based service for managing organizations and their administrators.

## Features

- Organization creation and management
- Admin user management
- JWT-based authentication
- Async SQLite database support
- Docker support for development and deployment

## Prerequisites

- Python 3.12+
- Docker (optional)
- SQLite

## Project Structure

navaorg_management/
├── app/
│ ├── init.py
│ ├── models/
│ ├── routers/
│ └── schemas/
├── common/
│ └── db.py
├── config/
│ └── settings.py
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── local.env

## Environment Setup

1. Create a `local.env` file in the root directory:
```env
RUN_ENV=dev
DEBUG=True
PROJECT_NAME=navaorg_management
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
DATABASE_URL=sqlite+aiosqlite:///./master_db.sqlite3
```

## Running with Docker

1. Build and start the containers:
```bash
docker-compose up --build
```

2. For detached mode:
```bash
docker-compose up -d --build
```

3. View logs:
```bash
docker-compose logs -f
```

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI Schema: `http://localhost:8000/schema-pc/openapi.json`

## API Endpoints

### Organizations

- `POST /api/v1/org/create` - Create a new organization
  ```json
  {
    "organization_name": "string",
    "admin_email": "string",
    "password": "string"
  }
  ```

### Authentication

- `POST /api/v1/auth/login` - Login with admin credentials
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```

## Development

- Code changes will automatically reload when running with `--reload` flag or using Docker Compose
- Database migrations are handled automatically on startup
- Environment variables can be modified in `local.env`

## Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=app tests/
```