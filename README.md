#  Access Control Service

This project is a **modular access control microservice** designed for a dental/orthodontic SaaS platform.  
It extends the existing single-office user system to support **multi-office access and DSO-level roles** (Dental Service Organizations).

---

##  Features

- Role-Based Access Control (**RBAC**) + Attribute-Based Access Control (**ABAC**) hybrid
- DSO-level and Office-level user permissions
- RESTful APIs for integration with main app
- Built with **Flask + PostgreSQL**
- Modular, extensible, and can run independently

---

##  Project Overview

### Why this exists

Originally, the system supported only single offices.  
However, real-world dental organizations (DSOs) manage multiple offices and staff that may work across locations.  
This service solves that by introducing:
- **DSO entities**
- **DSO–Office mappings**
- **DSO Users** with cross-office roles
- A unified permission system that integrates easily via APIs.

---

##  Project Structure
```bash
access_control_service/
├── app/
│ ├── init.py # Flask app setup
│ ├── config.py # Environment configuration
│ ├── models/ # SQLAlchemy models
│ │ ├── init.py
│ │ ├── dso.py
│ │ ├── office_dso.py
│ │ ├── role.py
│ │ ├── permission.py
│ │ ├── role_permission.py
│ │ ├── user_office_role.py
│ │ └── user_dso_role.py
│ ├── routes/ # API route definitions
│ │ ├── init.py
│ │ ├── access_routes.py
│ │ ├── user_routes.py
│ │ └── dso_routes.py
│ └── services/ # Business logic (ABAC + RBAC)
│ ├── access_service.py
│ ├── role_service.py
│ └── user_service.py
├── app.py # Entry point
├── seed_data.py # Seeds sample DSO, office, role, user data
├── .env # Environment variables
├── requirements.txt # Dependencies
├── README.md # Documentation
└── api.md # API Documentation
```

##  Setup Instructions

### 1️ Clone the Repository
```bash
git clone https://github.com/<your-username>/access_control_service.git
cd access_control_service
```
### 2️ Create and Activate Virtual Environment
### Create venv
```bash
python -m venv venv
```
### Activate it
### On Windows:
```
venv\Scripts\activate
```
### On macOS/Linux:
```
source venv/bin/activate
```

### 3️ Install Dependencies
```
pip install -r requirements.txt
```

### 4️ Configure Environment

Edit .env file with your PostgreSQL credentials:
```
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=supersecretkey_change_this
DATABASE_URL=postgresql://postgres:<your-password>@localhost:5432/access_control_db
```
### 5️ Initialize and Seed Database

Make sure PostgreSQL is running, then run:
```
python seed_data.py
```

### 6️ Run the Application
```
python app.py
```

Your server will start at:

http://127.0.0.1:5000

### 7️ Test APIs in Postman

Import the provided endpoints from api.md or manually test via Postman.
```
 Tech Stack
Component	Technology
Backend	Flask
Database	PostgreSQL
ORM	SQLAlchemy
Auth Model	RBAC + ABAC hybrid
Testing	Postman
```
##  Authorization Logic

The service uses a hybrid RBAC + ABAC approach:

- Roles are stored in the database (RBAC)

Access decisions are evaluated dynamically (ABAC) based on:

- User → role, DSO, office

- Resource → office ownership

- Action → requested operation

###  Example Query

POST /api/check-permission
```json
{
  "userId": 1,
  "officeId": 101,
  "action": "edit_records"
}
```

Response
```json
{
  "allowed": true,
  "granted_by_role": "DSO Admin (DSO Level)"
}
```


---

## 📘 **api.md**

```markdown
#  API Documentation — Access Control Service

All endpoints are prefixed with `/api`.


