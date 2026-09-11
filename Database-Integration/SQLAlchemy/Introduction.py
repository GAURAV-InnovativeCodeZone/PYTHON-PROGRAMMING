# ============================================================
#                    SQLALCHEMY - INTRODUCTION
# ============================================================
#
# SQLAlchemy is a Python SQL toolkit and Object Relational
# Mapper (ORM) that allows Python applications to work with
# relational databases.
#
# SQLAlchemy has two major components:
#
# 1. SQLAlchemy Core
# 2. SQLAlchemy ORM
#
# In this file, we are understanding the basic architecture
# and terminology before writing database operations.
# ============================================================


# ============================================================
#                    1. WHAT IS SQLALCHEMY?
# ============================================================
#
# SQLAlchemy allows Python applications to communicate with
# relational databases such as:
#
# - PostgreSQL
# - MySQL
# - SQLite
# - Oracle
# - Microsoft SQL Server
#
# Basic flow:
#
# Python Application
#        ↓
#    SQLAlchemy
#        ↓
#     Database
#
# ============================================================


# ============================================================
#                    2. SQLALCHEMY CORE
# ============================================================
#
# SQLAlchemy Core is the lower-level SQL toolkit.
#
# It provides objects and APIs for constructing and executing
# SQL statements.
#
# Important Core concepts:
#
# - Engine
# - Connection
# - MetaData
# - Table
# - Column
# - SQL expressions
# - Transactions
#
# Conceptually:
#
# Python
#   ↓
# SQLAlchemy Core
#   ↓
# SQL
#   ↓
# Database
#
# ============================================================


# ============================================================
#                    3. SQLALCHEMY ORM
# ============================================================
#
# ORM = Object Relational Mapping
#
# SQLAlchemy ORM allows us to work with database data using
# Python classes and objects.
#
# Basic mapping:
#
# Python                Database
# --------------------------------
# Class          →      Table
# Object         →      Row
# Attribute      →      Column
#
# Example:
#
# class User:
#     name
#     email
#
#        ↓
#
# users table
# -------------------
# name | email
#
# ============================================================


# ============================================================
#                    4. CORE vs ORM
# ============================================================
#
# SQLAlchemy Core:
#
# Python
#   ↓
# SQLAlchemy Core
#   ↓
# SQL statements
#   ↓
# Database
#
#
# SQLAlchemy ORM:
#
# Python Object
#      ↓
# SQLAlchemy ORM
#      ↓
# SQL statements
#      ↓
# Database
#
#
# ORM internally uses SQLAlchemy Core.
#
# So:
#
# ORM
#  ↓
# Core
#  ↓
# Database
#
# ============================================================


# ============================================================
#                    5. DATABASE
# ============================================================
#
# Database and table are NOT the same thing.
#
# Example:
#
# PostgreSQL Server
# │
# └── ecommerce          ← Database
#     │
#     ├── users          ← Table
#     ├── products       ← Table
#     └── orders         ← Table
#
# A database can contain multiple tables.
#
# ============================================================


# ============================================================
#                    6. TABLE
# ============================================================
#
# A table stores related records.
#
# Example:
#
# users
# --------------------------------
# id | name   | email
# --------------------------------
# 1  | Gaurav | ...
# 2  | Rahul  | ...
#
# SQLAlchemy Core represents database tables using the
# Table object.
#
# ============================================================


# ============================================================
#                    7. ROW
# ============================================================
#
# A row is one record in a database table.
#
# Example:
#
# users
# --------------------------------
# id | name   | email
# --------------------------------
# 1  | Gaurav | ...
#
# The complete:
#
# 1 | Gaurav | ...
#
# is one row/record.
#
# ============================================================


# ============================================================
#                    8. COLUMN
# ============================================================
#
# A column represents one field/property of the table.
#
# Example:
#
# users
# --------------------------
# id | name | email
# --------------------------
#
# id
# name
# email
#
# are columns.
#
# ============================================================


# ============================================================
#                    9. ENGINE
# ============================================================
#
# Engine is SQLAlchemy's main database connectivity
# infrastructure.
#
# Basic architecture:
#
# Application
#      ↓
#    Engine
#      ↓
#   Database
#
# Engine is NOT the database itself.
#
# It provides the infrastructure through which SQLAlchemy
# communicates with the database.
#
# We will study Engine in:
#
# 02_engine.py
#
# ============================================================


# ============================================================
#                    10. CONNECTION
# ============================================================
#
# A Connection represents an active database connection.
#
# Conceptually:
#
# Engine
#   ↓
# Connection
#   ↓
# Database
#
# Engine manages the infrastructure for obtaining/using
# connections.
#
# We will study this in:
#
# 05_connection.py
#
# ============================================================


# ============================================================
#                    11. METADATA
# ============================================================
#
# MetaData represents a collection of database schema
# information known to SQLAlchemy.
#
# It can contain information about:
#
# - Tables
# - Columns
# - Constraints
# - Indexes
# etc.
#
# Conceptually:
#
# MetaData
# │
# ├── users
# ├── products
# └── orders
#
# We will study this in:
#
# 06_metadata.py
#
# ============================================================


# ============================================================
#                    12. DIALECT
# ============================================================
#
# Different databases have different SQL behavior.
#
# SQLAlchemy uses a Dialect to handle database-specific
# SQL behavior.
#
# Examples:
#
# - PostgreSQL dialect
# - MySQL dialect
# - SQLite dialect
# - Oracle dialect
#
# ============================================================


# ============================================================
#                    13. DRIVER
# ============================================================
#
# Driver is the database-specific Python DBAPI implementation
# used for communication with the database.
#
# Examples:
#
# PostgreSQL:
#     psycopg
#     asyncpg
#
# MySQL:
#     PyMySQL
#     mysqlclient
#
# SQLite:
#     sqlite3
#
# Conceptually:
#
# SQLAlchemy
#     ↓
# Dialect
#     ↓
# Driver
#     ↓
# Database
#
# ============================================================


# ============================================================
#                    14. DATABASE URL
# ============================================================
#
# SQLAlchemy needs a URL describing how to connect to the
# database.
#
# General structure:
#
# dialect+driver://username:password@host:port/database
#
# Example:
#
# postgresql+psycopg://user:password@localhost:5432/mydb
#
# Breakdown:
#
# postgresql → Dialect
# psycopg    → Driver
# user       → Username
# password   → Password
# localhost  → Host
# 5432       → Port
# mydb       → Database
#
# We will study this separately.
#
# ============================================================


# ============================================================
#                    15. IMPORTANT FLOW
# ============================================================
#
# Keep this architecture in mind throughout SQLAlchemy:
#
#
# Python Application
#         ↓
#      SQLAlchemy
#         ↓
#       Engine
#         ↓
# Dialect + Driver
#         ↓
#     Connection
#         ↓
#      Database
#
#
# For ORM:
#
# Python Application
#         ↓
#       Session
#         ↓
#       ORM Model
#         ↓
#       SQLAlchemy
#         ↓
#       Engine
#         ↓
#     Database
#
# ============================================================


# ============================================================
#                    KEY TAKEAWAYS
# ============================================================
#
# 1. SQLAlchemy is a Python SQL toolkit + ORM.
#
# 2. SQLAlchemy has two major parts:
#       - Core
#       - ORM
#
# 3. Core is SQL-oriented.
#
# 4. ORM allows us to work with Python objects/classes.
#
# 5. ORM internally builds on SQLAlchemy Core.
#
# 6. Database != Table.
#
# 7. Engine != Database.
#
# 8. Session != Engine.
#
# 9. Dialect handles database-specific SQL behavior.
#
# 10. Driver communicates with the actual database.
#
# 11. MetaData stores schema/table-related information.
#
# ============================================================