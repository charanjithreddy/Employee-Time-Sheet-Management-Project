# Employee Timesheet Management System

## Overview
The **Employee Timesheet Management System** is a web-based application developed using **Flask** and **Python**. It allows employees to log their work hours, retrieve past records, and manage attendance efficiently.  
The system also supports employee account creation, secure login, and a clear workflow for timesheet updates and retrieval.

---

## Features
- Employee login and logout functionality  
- Entry of daily worked hours  
- Timesheet retrieval for a selected date range  
- Validation for user input and database integrity  
- MySQL database integration  
- Modular routing using Flask Blueprints  
- Flash message support for user feedback  
- Responsive front-end built with HTML and CSS  

---

## Project Structure
ACR_PROJECT/
│
├── app.py → Main Flask application
├── routes/ → Contains route handlers
│ ├── db_connect.py → Database connection module
│ └── timesheet_entry_routes.py → Timesheet handling logic
│
├── templates/ → HTML templates
│ ├── index.html → Entry page
│ ├── login.html → Login screen
│ ├── home.html → Home dashboard
│ ├── timesheet_entry.html → Timesheet data entry and retrieval
│ └── logout.html → Logout confirmation
│
├── static/ → Static assets
│ ├── css/ → Styling files
│ └── js/ → Client-side scripts
│
├── README.md → Project documentation
└── requirements.txt → List of dependencies


---

## Installation and Setup

### 1️⃣ Prerequisites
Ensure the following are installed:
- Python 3.10 or later  
- MySQL / Oracle Database  
- pip (Python package manager)

### 2️⃣ Clone the Repository
```bash
git clone <repository-url>
cd ACR_PROJECT

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Configure the Database

Update the database connection details in routes/db_connect.py.

Import the provided SQL schema (EMPLOYEE and EMP_TIMESHEET tables).

5️⃣ Run the Application

python app.py


The application will be available at:
👉 http://127.0.0.1:5000

Author

A Charanjith Reddy
B.Tech Computer Science and Engineering
Vellore Institute of Technology