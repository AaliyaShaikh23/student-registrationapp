# 📘 Flask-Based Student Registration Application with CI/CD Deployment

---

## 📌 Project Title

Flask-Based Student Registration Application with CI/CD Deployment

---

## 📖 Project Description

This project is a web-based student registration system developed using **Flask**. It allows users to enter student details through a form, store them in a **MySQL database**, and view all registered students.

The project also integrates **GitHub for version control** and **Jenkins for CI/CD automation**, enabling automated build and verification of the application.

---

## 🎯 Objectives

* Develop a Flask-based web application
* Store student data in MySQL
* Display registered student details
* Use GitHub for version control
* Implement CI/CD using Jenkins

---

## 🛠️ Technologies Used

* Python (Flask)
* MySQL
* HTML & CSS
* Git & GitHub
* Jenkins

---

## 🏗️ System Architecture

User → HTML Form → Flask Backend → MySQL Database
Developer → GitHub → Jenkins → Automated Build

---

## ⚙️ Project Features

* Student Registration Form
* Input Validation
* Store Data in MySQL Database
* Display Registered Students
* CI/CD Pipeline using Jenkins

---

## 📂 Project Structure

```
student-registration-app/
│
├── app.py
├── config.py
├── requirements.txt
├── schema.sql
├── Jenkinsfile
├── README.md
│
├── templates/
│   ├── index.html
│   ├── students.html
│   └── message.html
│
└── static/
    └── style.css
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AaliyaShaikh23/student-registrationapp.git
cd student-registrationapp
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Database

Update `config.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_mysql_password",
    "database": "studentdb"
}
```

---

### 5️⃣ Setup Database

Run `schema.sql` in MySQL Workbench:
```sql
CREATE DATABASE studentdb;
USE studentdb;
-- run full schema.sql file
```

---

### 6️⃣ Run Application
```bash
python app.py
```
Open in browser:
```
http://127.0.0.1:5000
```
---

## 🔁 CI/CD Implementation (Jenkins)

* Jenkins is configured with a pipeline job
* It connects to GitHub repository
* Automatically pulls latest code
* Installs dependencies
* Verifies Flask application
* Displays build success or failure

---
## ⚠️ Challenges Faced

* MySQL authentication issues
* Jenkins installation issues
* Port conflict (8080 already in use)
* Java compatibility for Jenkins
* SCM configuration errors in Jenkins
* pip command not recognized in Jenkins

---
## 🔮 Future Enhancements

* Add update and delete functionality (CRUD)
* Add login authentication system
* Deploy application on AWS EC2
* Use Docker for containerization
* Add search and filter functionality
* Send email notification after registration

---
## 📌 Conclusion
The project successfully demonstrates a **full-stack web application** using Flask and MySQL along with **CI/CD integration using Jenkins**. It highlights how development and deployment can be automated efficiently.

---
Author
Aaliya Shaikh
