# ml_dbms
# 📊 Machine Learning Dataset Management System (MLDMS)

## 📌 Project Overview

The **Machine Learning Dataset Management System (MLDMS)** is a Python-based web application designed to organize and manage datasets used in machine learning projects. It provides a centralized platform for uploading datasets, maintaining dataset versions, tracking preprocessing activities, managing ML model details, and monitoring model performance.

The application uses **Streamlit** for its user interface and **MySQL** for storing structured project information.

## 🎯 Objectives

- Simplify the uploading and management of ML datasets.
- Maintain dataset versions and track changes.
- Record dataset preprocessing activities.
- Manage machine learning model information.
- Store and monitor model performance metrics.
- Generate reports through a centralized dashboard.
- Provide user authentication and organization workspace features.

## ✨ Features

### 1. User Authentication
- User registration and login.
- Password hashing for secure password storage.
- Role-based user information.

### 2. Dataset Management
- Upload datasets.
- View and organize uploaded datasets.
- Maintain dataset information in the database.

### 3. Dataset Version Control
- Add new versions of datasets.
- Maintain version history.
- Track changes between dataset versions.

### 4. Data Preprocessing
- Record preprocessing operations.
- View preprocessing history for datasets.

### 5. ML Model Management
- Maintain information about machine learning models.
- View registered models and their associated datasets.

### 6. Performance Tracking
- Store model evaluation metrics such as accuracy, precision, recall, and F1-score.
- View recorded model performance information.

### 7. Dashboard and Reports
- Display dataset and model information.
- View summarized project statistics and reports.

### 8. Organization Workspace
- Create organizations and projects.
- Manage organization membership and roles.

*Note: Organization membership features are under development. Full organization-level data isolation should be implemented before using the application with sensitive or confidential datasets.*

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web application interface |
| MySQL | Database management |
| Pandas | Dataset handling |
| Bcrypt | Password hashing |
| SQL | Queries and database operations |
| Git and GitHub | Version control and source code management |

## 📂 Project Structure

```text
ML_Dataset_Management/
│
├── app.py
├── database.py
├── auth.py
├── reports.py
├── datasets.py
├── versions.py
├── preprocessing.py
├── models.py
├── performance.py
├── organization.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── uploads/
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or another version compatible with your dependencies.
- MySQL Server and MySQL Workbench.
- Git.
- Visual Studio Code or another Python editor.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ML_Dataset_Management
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure that `requirements.txt` contains all the packages imported by your project.

### Step 4: Configure MySQL

1. Open MySQL Workbench.
2. Create the database:

```sql
CREATE DATABASE ml_dataset_management;
```

3. Select the database and execute the SQL statements required to create the project's tables, views, indexes, triggers, and stored procedures.
4. Configure the database connection in `database.py` using your local MySQL settings.

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not, open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 📈 Model Performance Metrics

The application can record and display evaluation metrics for machine learning models, including:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted positive cases that are correct.
- **Recall:** Proportion of actual positive cases correctly identified.
- **F1-score:** Harmonic mean of precision and recall.

The system manages model information and recorded metrics; it does not automatically train machine learning models unless that functionality is implemented separately.

## 🔐 Security Considerations

- Passwords should be stored as secure hashes rather than plain text.
- Database credentials must not be committed to GitHub.
- Use Streamlit secrets or environment-based configuration for deployed applications.
- Configure appropriate database permissions and organization-level access controls before handling confidential data.

## 🚀 Deployment

The application can be deployed using **Streamlit Community Cloud**.

Deployment requires:
1. A GitHub repository containing the application files.
2. A valid `requirements.txt`.
3. A reachable hosted MySQL database.
4. Secure database credentials configured through Streamlit secrets.

A local MySQL database using `localhost` cannot be accessed directly by a cloud-hosted application.

## 🔮 Future Enhancements

- Automatic machine learning model training and evaluation.
- Dataset quality checks and visualization.
- Advanced dataset comparison and version-difference reports.
- Improved organization-based access control.
- Dataset search, filtering, and tagging.
- Integration with cloud storage.
- Exportable performance reports.

## 👩‍💻 Project Purpose

This project demonstrates the integration of Python, Streamlit, MySQL, and SQL database concepts to develop a centralized system for managing datasets and tracking machine learning project information.

---

**Project:** Machine Learning Dataset Management System (MLDMS)  
**Domain:** Machine Learning, Data Management, and Database Systems
