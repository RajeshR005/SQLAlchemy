# 🌟 SQLAlchemy Mastery: A Hands-On Journey

![SQLAlchemy Banner](https://raw.githubusercontent.com/RajeshR005/SQLAlchemy/main/assets/sqlalchemy_banner.gif)

Welcome to the **SQLAlchemy Mastery** repository — a comprehensive, hands-on guide to mastering [SQLAlchemy](https://www.sqlalchemy.org/), Python’s powerful SQL toolkit and Object Relational Mapper (ORM). This repository is crafted to help you understand and implement SQLAlchemy's core features through practical examples and real-world scenarios.

---

## 📂 Project Structure

```
SQLAlchemy/
├── assets/                     # Images and animations for documentation
├── Student_task/               # Exercises and tasks related to student management
├── employee_task/              # Employee-related database operations
├── __pycache__/                # Compiled bytecode files
├── app.py                      # Main application script
├── createdb.py                 # Script to create the database and tables
├── delete.py                   # Examples of delete operations
├── grouping_chaining.py        # Demonstrations of grouping and chaining queries
├── insert.py                   # Examples of insert operations
├── joins.py                    # Demonstrations of various join operations
├── loading-techniques.py       # Examples of different loading strategies
├── many2many.py                # Many-to-many relationship examples
├── models.py                   # SQLAlchemy ORM models
├── one2one.py                  # One-to-one relationship examples
├── queries.py                  # Complex query examples
├── read.py                     # Examples of read operations
├── self-relation.py            # Self-referential relationship examples
├── tablecreation.py            # Table creation scripts
├── update.py                   # Examples of update operations
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
- A supported database (e.g., SQLite, PostgreSQL, MySQL)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/RajeshR005/SQLAlchemy.git
cd SQLAlchemy

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🧠 What You'll Learn

- 📌 Database Connections using `create_engine`
- 📌 Table Definitions with SQLAlchemy ORM
- 📌 CRUD Operations (Create, Read, Update, Delete)
- 📌 One-to-One, One-to-Many, Many-to-Many & Self-Relations
- 📌 Complex Querying (joins, chaining, grouping)
- 📌 Lazy vs Eager Loading (loading techniques)
- 📌 Scalar Queries and Aggregations
- 📌 ORM Best Practices for real-world apps

---

## 🎯 How to Use

Each Python file in this repository is self-contained and targets a specific concept or feature in SQLAlchemy. Run them independently to explore:

```bash
python createdb.py           # Creates database tables
python insert.py             # Insert records
python read.py               # Query data
python update.py             # Update data
python delete.py             # Delete data
python joins.py              # Demonstrate join operations
python one2one.py            # One-to-one relation example
python many2many.py          # Many-to-many relation example
python self-relation.py      # Self-referencing relation
python loading-techniques.py # Loading strategies: lazy, joinedload, etc.
```

## 🧑‍💻 Author

**Rajesh R**   
[![Gmail](https://img.shields.io/badge/Gmail-rajeshr005%40gmail.com-red?logo=gmail&logoColor=white)](mailto:rajeshr30072002@gmail.com) 

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> 🔥 Whether you're a beginner or brushing up your ORM skills — this repo is built to make you SQLAlchemy-strong 💪
