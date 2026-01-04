# 🧑‍💼 Employee Management System (EMS)

A secure and user-friendly **Employee Management System** built using **Python (Flask)** and **SQLite**, designed to perform complete **CRUD operations** on employee records with proper **authentication and validation**.

This project was developed as part of my **Internship Project** to demonstrate full-stack development skills, backend logic, and secure data handling.

---

## 🚀 Features

- 🔐 **Admin Authentication**
  - Secure login system
  - Session-based access control

- 👥 **Employee Management (CRUD)**
  - Add new employees
  - View employee records
  - Edit employee details
  - Delete employees

- 🛡️ **Data Security**
  - Input validation
  - Protected routes (admin-only access)
  - Secure handling of employee data

- 🗄️ **Database Integration**
  - SQLite database for persistent storage
  - Structured employee table

- 🎨 **Clean UI**
  - HTML templates with CSS styling
  - Simple and intuitive dashboard

---

## 🧰 Tech Stack

| Layer        | Technology |
|-------------|------------|
| Backend     | Python, Flask |
| Frontend    | HTML, CSS |
| Database    | SQLite |
| Authentication | Flask Sessions |
| Tools       | VS Code, GitHub |

---

## 📁 Project Structure

```

employee-management-system/
│
├── app.py
├── employees.db
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── add_employee.html
│   ├── edit_employee.html
│
└── static/
└── style.css

````

---

## ⚙️ Installation & Setup (Run Locally)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ashwincyberlab/employee-management-system.git
cd employee-management-system
````

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔑 Default Admin Credentials (Demo)

```
Username: admin
Password: admin123
```

> ⚠️ *For production, credentials should be encrypted and stored securely.*

---

## 📊 Learning Outcomes

* Hands-on experience with **Flask backend development**
* Understanding of **CRUD operations**
* Implementation of **authentication & authorization**
* Working with **SQLite databases**
* Structuring real-world Python projects
* Version control using **Git & GitHub**

---

## 🏢 Internship Context

* **Internship Project**
* Focused on backend development & system design
* Demonstrates practical industry-level application logic

---

## 🔮 Future Enhancements

* Role-based access (Admin / HR)
* Password hashing (bcrypt)
* Search & filter employees
* Pagination
* REST API integration
* Deployment on cloud (Render / Railway)

---

## 👨‍💻 Author

**Ashwin Yadav**
GitHub: [https://github.com/Ashwincyberlab](https://github.com/Ashwincyberlab)

---

⭐ *If you like this project, feel free to star the repository!*
