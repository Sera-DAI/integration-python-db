<img width="1700" height="460" alt="github-header-banner" src="https://github.com/user-attachments/assets/e541c44d-4fe4-41da-86af-77ea202ed070" />

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=git,vscode,docker,py,arch,postman,windows,mysql" />
  </a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/stats-Completed-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/python-3.14.6-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/github/repo-size/Sera-DAI/integration-python-db?style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/Sera-DAI/integration-python-db?style=for-the-badge" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Tests-Postman%20Verified-orange?style=flat-square&logo=postman" />
  <img src="https://img.shields.io/badge/Environment-Docker%20%2B%20MySQL-0275d8?style=flat-square&logo=docker" />
</p>

---
## 📝 About

This project demonstrates a backend integration between a **Python** application and a **MySQL** database, fully containerized using **Docker**. The main goal is to provide a reliable, scalable, and easy-to-reproduce environment for API development and data persistence.

## 🏛️ Architecture

* **Backend:** Python application handling the core business logic, API routing, and database communication.
* **Database:** MySQL relational database storing structured application data.
* **Infrastructure:** Docker and Docker Compose for seamless environment replication, networking, and dependency management.

## 📦 Modules & Dependencies

The Python application requires the following core modules to function properly. All of them are listed in the `requirements.txt` file:

* **Flask:** Core microframework for routing and handling HTTP API requests.
* **Flask-SQLAlchemy:** Database ORM (Object-Relational Mapper) to handle database queries and models efficiently.
* **Flask-Cors:** Handles Cross-Origin Resource Sharing (CORS) to allow frontend applications to communicate with the API safely.
* **Werkzeug:** A comprehensive WSGI web application library that underlies Flask.
* **Flask-Login:** Provides comprehensive user session management, handling logins, logouts, and remembering users' sessions.
* **mysql-connector-python:** The official database driver used by Python to connect and communicate with the MySQL container.
* **python-dotenv:** Loads environment variables from a `.env` file to manage sensitive credentials (like database passwords) securely.

## 🛠️ Pre-requirements

Before you begin, ensure you have the following installed on your machine:
* [Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* *Optional:* [Postman](https://www.postman.com/) (For testing endpoints)

## 🚀 Getting Started

Follow these steps to get the application up and running in your local environment.

### 1. Clone the Repository
Clone this repository to your local machine and navigate into the project directory:
```bash
git clone https://github.com/Sera-DAI/integration-python-db.git
cd integration-python-db
```

### 2. Environment Variables (Optional)
If your project uses an `.env` file for database credentials, duplicate the example file and configure your variables:
```bash
cp .env.example .env
```

### 3. Build and Run with Docker
Spin up both the Python application and the MySQL database containers in the background using Docker Compose:
```bash
docker-compose up -d --build
```
*Note: The first run might take a few minutes as Docker downloads the necessary Python and MySQL images.*

### 4. Verify the Services
Check if the containers are running successfully:
```bash
docker ps
```
The application should now be integrated and accessible (usually via `http://localhost:5000` or your defined port).

### 5. Setup the Python Virtual Environment
Create and activate an isolated environment for the application dependencies.

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**On Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 6. Install Requirements
With the virtual environment activated, install the required Python modules:
```bash
pip install -r requirements.txt
```

### 7. Run the Application
Start the local Python development server:
```bash
python app.py
```
*(Or `flask run`, depending on your main file configuration).*
The API should now be successfully connected to the Dockerized MySQL database!

## 🌐 API Endpoints & Testing

All endpoints can be tested using **Postman**. If there is an exported Postman collection inside this repository, you can import it directly to test the data flow between Python and MySQL.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/52076750/2sBXwyF6aL)

## 🛑 Stopping the Application

To stop the containers and gracefully shut down the services without losing your database data, run:
```bash
docker-compose down
```
*(Note: If you want to wipe the database volumes entirely and start fresh, you can append the `-v` flag: `docker-compose down -v`)*
