## <h1 align="center">  Workforce Management System (Backend) </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-Django%20%26%20DRF-darkgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Auth-JWT-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Caching-django Cache-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/API%20Testing-Postman-orange?style=for-the-badge" />
</p>


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


## ⚡ Caching Strategy

- Attendance list cached per project

- Cache key format:
        
        attendance_project_<project_id>

- Cache invalidated automatically on:

    - Create

    - Update

    - Delete

## 🧪 Testing
- Model-level validations

- Business rule enforcement

- Permission-based access testing

- Cache invalidation tested manually via API calls  

## 🗄️ Database

- PostgreSQL as primary database

- Secure credentials via .env

- Proper migrations applied

- Relational integrity maintained

## 🧪 Getting Started (Local Setup)
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



