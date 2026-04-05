# 💰 Financial Records Management System

A full-stack financial tracking application built using **FastAPI (backend)** and **Streamlit (frontend)**.
It allows users to manage income and expenses, analyze spending patterns, and visualize financial data.


Live app : https://financial-records-management.streamlit.app/

Fastapi Link : https://financial-records-management-production.up.railway.app/
---

## 🚀 Features

### 🔐 Authentication

* User Signup & Login
* Password hashing using `bcrypt`
* JWT-based authentication
* Secure API access

### 💵 Financial Management

* Add income & expense records
* Categorize transactions (Rent, Groceries, Salary, etc.)
* Add notes to transactions

### 📊 Analytics & Insights

* Total Income, Expense & Balance
* Monthly Income vs Expense summary
* Category-wise breakdown
* Data visualization using charts

### 🧾 CRUD Operations

* Create, Read, Update, Delete financial records
* Filter by:

  * Date
  * Category
  * Type (Income/Expense)
* Sort records by amount or date

---

## 🏗️ Project Structure

```
project/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app (routes)
│   ├── database.py      # Database connection & queries
│   ├── crud.py          # Business logic
│   ├── schemas.py       # Pydantic models
│   ├── auth.py          # Authentication (JWT, hashing)
│   ├── analytics.py     # Data analysis
│
├── frontend/
│   └── frontend.py      # Streamlit UI
│
├── financial_db.db      # SQLite database
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Database:** SQLite
* **Authentication:** JWT + bcrypt
* **Data Analysis:** Pandas

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/financial-records-management.git
cd financial-records-management
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

👉 API Docs: http://127.0.0.1:8000/docs

---

### 5️⃣ Run Frontend (Streamlit)

```bash
streamlit run frontend/frontend.py
```

---

## 🔐 Authentication Flow

1. User signs up → `/signup`
2. User logs in → `/login`
3. Server returns JWT token
4. Token is used in headers:

```
Authorization: Bearer <your_token>
```

---

## 📊 Example Categories

* Salary
* Business
* Rent
* Groceries
* Education
* Entertainment
* Utilities
* Transportation
* Healthcare

---

## 📌 API Endpoints

| Method | Endpoint                       | Description        |
| ------ | ------------------------------ | ------------------ |
| POST   | `/signup`                      | Register new user  |
| POST   | `/login`                       | Login user         |
| POST   | `/create`                      | Add record         |
| GET    | `/records`                     | Get all records    |
| GET    | `/records/date/{date}`         | Filter by date     |
| GET    | `/records/category/{category}` | Filter by category |
| GET    | `/records/type/{type}`         | Filter by type     |
| GET    | `/sort`                        | Sort records       |
| PUT    | `/update/{id}`                 | Update record      |
| DELETE | `/records/{id}`                | Delete record      |

---

## 📈 Future Improvements

* 🔁 Refresh tokens
* 👥 Multi-user dashboard
* ☁️ PostgreSQL integration
* 📱 Mobile-friendly UI
* 📊 Advanced charts (Pie, Line, Trends)
* 🔔 Budget alerts & notifications

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Bikram Maity**

---

⭐ If you like this project, don’t forget to give it a star!
