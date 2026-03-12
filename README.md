# Random Matrix API

Backend service for generating and analyzing random matrices.

## Overview

Random Matrix API provides a REST API for generating random matrices and performing basic numerical operations.  
It is designed to support a web application that visualizes matrix properties and results from Random Matrix Theory.

## Backend Implementation

The backend is implemented in **Python** using the **FastAPI** framework. Key components:

- **Pydantic** – defines data schemas for input validation and JSON parsing.
- **Uvicorn ASGI server** – handles HTTP requests and communication between client and backend.
- Middleware allows cross-origin requests from any domain with any HTTP methods and headers.

## Features

- Generate random matrices
- Perform basic matrix operations
- Numerical analysis of matrix properties
- JSON-based REST API for frontend integration

## Installation and Running

Clone the repository and install dependencies (including the computation package from GitHub):

```bash
git clone https://github.com/Krzemon/random-matrix-api.git
cd random-matrix-api
pip install -r requirements.txt
```
Package repository: https://github.com/Krzemon/mp-package
In requirements.txt include a line like: git+https://github.com/Krzemon/mp-package.git@main#egg=mp-package

## Start the server (default host & port):
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

