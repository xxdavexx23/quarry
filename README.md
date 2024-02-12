# Basic Three-Tier Application Simulation

This project simulates a basic three-tier application consisting of a front-end built with Vue.js, a back-end developed using Flask, and a MariaDB database. It demonstrates a simple data flow from the database to the front-end through the API.

## Project Structure

The project is divided into three main parts:

### 1. Frontend (`/frontend`)

- **Technology:** Vue.js
- **Key Features:** Data display in table format, API integration, reactivity, and environment configuration.
- **Development Tools:** Vue DevTools, component structure, state management with Vuex, testing with Jest/Mocha/Cypress, and accessibility considerations.
- **Setup Instructions:** Includes steps for project setup, development, and deployment. See [frontend README](frontend/README.md) for more details.

### 2. Backend (`/backend/api.base`)

- **Technology:** Flask
- **Key Features:** Flask CLI, database migrations, testing, error handling, logging, API documentation, and security practices.
- **Security Measures:** VPN access, network segmentation, monitoring and logging, regular updates, and authentication (JWT, OAuth 2.0, API keys/tokens, RBAC, 2FA).
- **Setup Instructions:** Covers Python and pip installation, project setup, secret key generation, and application running instructions. See [backend README](backend/api.base/README.md) for more details.

### 3. Database (`/db/changelog`)

- **Technology:** MariaDB
- **Setup Overview:** Outlines the database schema, table creation, example data insertion, and AWS RDS setup for integration with the Flask API.
- **Security Best Practices:** Creation of a read-only user for the Flask API to ensure limited access.
- **Connection Details:** Instructions for connecting to the database using a MariaDB client and configuring the Flask API to connect to the database. See [DB Setup Overview](db/changelog/README.md) for more details.

## Additional Files

- **`.gitignore` Files:** Present in both the frontend and backend directories to exclude specific files and directories from Git tracking.
- **`requirements.txt`**: Lists the Python packages required for the backend.
- **`package.json`**: Defines the frontend project dependencies and scripts.
- **`vite.config.js`**: Configuration file for Vite, used in the frontend for tooling and optimization.

## Development and Deployment

- **Frontend Deployment:** Instructions for running the Vue.js development server and building the project for production deployment.
- **Backend Deployment:** Details on running the Flask application locally and in the cloud, including setting up an Elastic IP for persistent access.
- **Database Deployment:** Steps for creating and connecting to a MariaDB database instance on AWS RDS, including security configurations.

This project serves as a foundational example of a three-tier application, demonstrating the integration of a Vue.js frontend, Flask backend, and MariaDB database.
