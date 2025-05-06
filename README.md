# SE_Project_Sem-VI

# Hostel Management System

A Django-based system for managing hostel operations in educational institutions.

## Features
- Student registration and profile management
- Room allocation with interactive floor maps
- Leave application and approval workflow
- Repair request tracking
- Dues management
- Mess rebate calculation
- Guest house booking system

## Installation

bash
# Clone the repository
git clone https://github.com/yourusername/HostelManagementSystem.git
cd HostelManagementSystem

# Set up virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin account
python manage.py createsuperuser

# Optional: Create warden accounts
python fix.py

# Run server
python manage.py runserver

Access the application at http://127.0.0.1:8000/
System Requirements

Python 3.6+
Django 2.1.2
Other dependencies listed in requirements.txt
