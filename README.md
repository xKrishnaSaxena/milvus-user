# FastAPI + Milvus User Management System

This project is a user management system built with FastAPI and Milvus. It supports CRUD operations and vector-based search functionality for user data stored in Milvus.

## Features

- Register a user with username, email, hashed password, and vector embeddings.
- Update user information.
- Search users by vector similarity.
- Retrieve a user by ID.
- Delete a user by ID.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Milvus](https://milvus.io/)
- [Pymilvus](https://pymilvus.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/) (optional if you extend with a relational database)
- [Uvicorn](https://www.uvicorn.org/) for ASGI server
- [Requests](https://docs.python-requests.org/) for testing
- Docker (optional for running Milvus)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **Milvus**: Follow the [Milvus installation guide](https://milvus.io/docs/install_standalone-docker.md) to set up Milvus using Docker.
- **Docker** (for Milvus setup)

## Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

```

### 2. Create and activate a Python virtual environment

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# For Linux/Mac
source venv/bin/activate

# For Windows
venv\Scripts\activate

```

### 3. Install required Python packages

```bash
pip install -r requirements.txt

```

### 4. Set up Milvus (Using Docker)

```bash
docker pull milvusdb/milvus:latest
docker run -d --name milvus-standalone -p 19530:19530 -p 8080:8080 milvusdb/milvus:latest

```

### 5. Run FastAPI App

```bash
# Run the FastAPI app using Uvicorn
uvicorn main:app --reload

```

### 6. Running Tests

```bash
python test.py

```
