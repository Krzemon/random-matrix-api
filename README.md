# Random Matrix API

Backend service for generating and analyzing random matrices.

Repository: https://github.com/Krzemon/random-matrix-api

## Overview

Random Matrix API is a backend application that provides an HTTP interface for generating and working with random matrices.  
It is designed to support a web application that visualizes matrix properties and results from Random Matrix Theory.

Random matrices are widely used in statistics, physics, and machine learning, where matrix elements are treated as random variables and their spectral properties are studied.

## Backend Implementation

The backend server of the application has been implemented in **Python** using the **FastAPI** framework, which is designed for building REST APIs.  

Key implementation details:

- **Pydantic** is used to define data schemas for input validation and parsing JSON data in HTTP request bodies.
- The application is run using the **Uvicorn ASGI server**, responsible for handling HTTP requests and managing communication between clients and the backend.
- Middleware configuration allows HTTP requests to the API from any domain, using any HTTP methods and headers, enabling cross-origin requests.

## Features

- Generation of random matrices
- Basic matrix operations
- Numerical analysis of matrix properties
- REST API for communication with the frontend
- JSON responses for easy integration with web applications
