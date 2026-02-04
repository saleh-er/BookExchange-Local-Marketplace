# 📚 BookExchange Local Marketplace

A full-stack Django web application for listing and searching books within a local community.

## 🚀 Features
- **User Authentication:** Secure login/logout using Django Auth.
- **Book Listings:** Users can upload book details, prices, and cover images.
- **Live Search:** Filter books by title or author instantly.
- **ISBN Integration:** (In progress) Auto-fill book data using Google Books API.
- **Responsive Design:** Built with Bootstrap 5 for mobile and desktop.

## 🛠️ Tech Stack
- **Backend:** Django 5.x, Python 3.11
- **Database:** SQLite (Development)
- **Frontend:** Bootstrap 5, HTML5/CSS3
- **Environment:** python-dotenv for secret management

## 📦 Installation
1. Clone the repo: `git clone <your-repo-url>`
2. Create venv: `python -m venv venv`
3. Activate venv: `.\venv\Scripts\activate`
4. Install requirements: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`