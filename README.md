## <h1 align="center">  Workforce Management System (Backend) </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-Django%20%26%20DRF-darkgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Auth-JWT-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Caching-django Cache-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/API%20Testing-Postman-orange?style=for-the-badge" />
</p>

## 📘 README Including

<p align="center">
  <img src="DB Schema Diagram/Readme.png" alt="DB Schema Diagram" width="100%" />
</p>

**Quick Visit:**
- [Architecture Explanation](#architecture)
- [Setup Steps](#setup)
- [API Usage](#api-usage)
- [DB Schema Diagram](#db-schema)


---

## ✨ Overview

This project is a **Mini Workforce Management Backend System** built using **Django & Django REST Framework** as part of a backend hiring assignment.

The system manages:

- Organizations  
- Projects  
- Employees  
- Attendance 
- Tasks

It is designed with clean architecture, JWT authentication, role-based permissions, business rule enforcement, PostgreSQL, and caching.

---

## 🛠️ Tech Stack

| Layer         | Technologies Used                                                                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Backend**   | Python, Django, Django REST Framework, PostgreSQL, JWT Authentication, Django Cache (LocMem / Redis ready), Postman (API Testing)                               |


<a id="architecture"></a>
## 🧱 Architecture

- Modular Django apps

- Clear separation of concerns:

    - Models → Data layer

    - Serializers → Validation & transformation

    - Views → Business logic

    - Permissions → Access control

- RESTful APIs

- Production-ready structure

## 📁 Project Structure

    Workforce Management System/
    │
    ├── manage.py
    ├── .env
    ├── requirements.txt
    │
    ├── workforce/
    │   ├── settings.py
    │   ├── urls.py
    │
    ├── organizations/
    ├── projects/
    ├── employees/
    ├── attendance/
    ├── tasks/
    

## 🔐 Authentication

- JWT Authentication using djangorestframework-simplejwt

- All APIs are protected

- Token-based access using: 
        
        Authorization: Bearer <access_token>

## 👥 Roles & Permissions

| Role    | Permissions                        |
| ------- | ---------------------------------- |
| Owner   | Full access                        |
| Manager | Create projects, tasks, attendance |
| Member  | Read-only access to assigned tasks |

Custom permissions implemented using DRF BasePermission.

## 📜 Business Rules Enforced

✔ Employee must belong to the organization

✔ Employee must be assigned to project before task creation

✔ Attendance date is unique per project

✔ Role-based access enforced

✔ Cache invalidation on data changes

<a id="api-usage"></a>
## 🚀 API Endpoints

### Auth
        POST /api/token/
        POST /api/token/refresh/

### Organization
        POST /api/org/create/
        GET  /api/org/list/


### Project
        POST /api/project/create/
        GET  /api/project/list/?organization=<org_id>


### Employee
        POST /api/employee/create/

### Attendance
        POST   /api/attendance/create/
        GET    /api/attendance/list/?project=<project_id>
        PUT    /api/attendance/update/<id>/
        DELETE /api/attendance/delete/<id>/

### Task
        POST /api/task/create/
        GET  /api/task/list/?project=<project_id>
        PUT  /api/task/update/<id>/


<a id="db-schema"></a>
## 🛢 DB Schema Diagram

A simple database schema diagram was created using **draw.io** to visualize entity relationships.

<p align="center">
  <img src="DB Schema Diagram/WMS Diagram.drawio (1).png" alt="DB Schema Diagram" width="100%" />
</p>

## 🗄️ Database

- PostgreSQL as primary database

- Secure credentials via .env

- Proper migrations applied

- Relational integrity maintained

## ⚡ Caching Strategy

- Attendance list cached per project

- Cache key format:
        
        attendance_project_<project_id>

- Cache invalidated automatically on:

    - Create

    - Update

    - Delete

## 🧪 Testing
### ✅ Model Tests

Tested database constraints (example: unique attendance per project per date)

Verified invalid duplicate entries raise errors

> How tested:

> Using Django TestCase to assert model behavior and 

### ✅ API Tests

Tested API creation and response codes

Verified JWT authentication is required

>How tested:

>Using APITestCase to send authenticated requests and validate responses (201, 403, etc.)

### ✅ Permission Tests

Verified members cannot create projects

Verified managers and owners can create allowed resources

>How tested:

>Role-based users were created and API calls were validated to return 403 Forbidden when access was denied.

### ✅ Cache Invalidation Tests

Attendance list was cached on first request

Cache was invalidated after create/update/delete

Fresh data returned after invalidation

>How tested:

>Manually tested using repeated API calls and observing updated responses after mutations.

<a id="setup"></a>
## ⚙️ Getting Started (Local Setup)
  ### 1️⃣ Clone the Repository
        https://github.com/shubhankarchdas/Workforce-Management-System.git
        cd Workforce Management System

  ### 2️⃣ Create Virtual Environment
        python -m venv venv
        venv\Scripts\activate
   

  ### 3️⃣ Install Dependencies
        pip install -r requirements.txt

        
  ### 4️⃣ Configure Environment Variables
  Create .env file:

        SECRET_KEY=django-secret
        DB_NAME=workforce_db
        DB_USER=postgres
        DB_PASSWORD=your_password
        DB_HOST=localhost
        DB_PORT=5432



  ### 5️⃣ Run Migrations
        python manage.py makemigrations
        python manage.py migrate


  ### 6️⃣ Create Superuser
        python manage.py createsuperuser


  ### 7️⃣ Run Server
        python manage.py runserver


## 📚 API Documentation (Swagger)

>Swagger UI available at:

        http://127.0.0.1:8000/swagger/


>ReDoc available at:

        http://127.0.0.1:8000/redoc/

## 🎤 Interview Summary (Short)

“I built a Django REST backend with JWT authentication, role-based permissions, PostgreSQL, caching for attendance optimization, proper testing, and Swagger documentation. All business rules are enforced at serializer and model level.”

## ⭐ Future Enhancements

- Redis for distributed caching

- Celery for async task processing

- Docker for containerization

- Pagination and filtering

- Rate limiting

## 📄 License

Developed as part of a backend hiring assignment for evaluation purposes.
