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
  <img src="https://img.shields.io/github/repo-size/Sera-DAI/tasks-creator?style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/Sera-DAI/tasks-creator?style=for-the-badge" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Tests-Postman%20Verified-orange?style=flat-square&logo=postman" />
  <img src="https://img.shields.io/badge/Environment-Docker%20%2B%20MySQL-0275d8?style=flat-square&logo=docker" />
</p>

---
## 📝 About

This project demonstrates a robust backend integration between a **Python** application and a **MySQL** database, fully containerized using **Docker**. The main goal is to provide a reliable, scalable, and easy-to-reproduce environment for API development and data persistence.

## 🏛️ Architecture

* **Backend:** Python application handling the core business logic, API routing, and database communication.
* **Database:** MySQL relational database storing structured application data.
* **Infrastructure:** Docker and Docker Compose for seamless environment replication, networking, and dependency management.

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

## 🌐 API Endpoints & Testing

All endpoints can be tested using **Postman**. If there is an exported Postman collection inside this repository, you can import it directly to test the data flow between Python and MySQL.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/)

## 🛑 Stopping the Application

To stop the containers and gracefully shut down the services without losing your database data, run:
```bash
docker-compose down
```
*(Note: If you want to wipe the database volumes entirely and start fresh, you can append the `-v` flag: `docker-compose down -v`)*
