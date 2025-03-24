# Ecommerce-Application-using-djangio-and-Python
## 📌 Project Overview

This project is a fully functional E-Commerce Application built using the Django Framework, HTML, and MySQL. The application includes essential e-commerce features such as user authentication, product catalog management, and order processing.

## 🔑 Key Features

User Authentication (Signup, Login, Logout)

Product Catalog (View products, Search, Categories)

Shopping Cart & Checkout

Order Management (Track orders, Order history)

Admin Panel (Manage products, users, and orders)

MySQL Database Integration

## 🛠️ Tech Stack

Backend: Python (Django Framework)

Frontend: HTML, CSS, JavaScript

## Database: MySQL

IDE: Visual Studio Code

🚀 Installation & Setup

## 1️⃣ Clone the Repository

git clone https://github.com/suganthirajayogam/Ecommerce-Application-using-djangio-and-Python

cd ecommerce-django

## 2️⃣ Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate    # For Windows

## 3️⃣ Install Dependencies

pip install -r requirements.txt

## 4️⃣ Configure Database (MySQL)

Create a MySQL database and update the settings.py file with your credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

## 5️⃣ Run Migrations

python manage.py makemigrations
python manage.py migrate

## 6️⃣ Create Superuser (Admin Access)

python manage.py createsuperuser

## 7️⃣ Run the Development Server

#python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to see the app in action! 🚀

## 📂 Project Structure

|-- ecommerce-django/
    |-- ecommerce/
    |-- products/
    |-- users/
    |-- orders/
    |-- static/
    |-- templates/
    |-- db.sqlite3 (if using SQLite)
    |-- manage.py
