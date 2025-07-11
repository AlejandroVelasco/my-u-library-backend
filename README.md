# My U Library

A simple university library system with **Django** for the API backend and **React + TypeScript** for the frontend.

## 🗂 Repository Structure (Backend)

```
backend/
├── .env.example          # Example environment variables (DO NOT commit to repo)
├── .gitignore            # Ignore .env, __pycache__, .venv, etc.
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── core/                 # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                # App for user and role management
├── books/                # App for book catalog
└── checkouts/            # App for book checkouts and returns
```

## 🚀 Getting Started (Backend)

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/my-u-library-backend.git
   cd my-u-library-backend/backend
   ```

2. **Create and activate a virtual environment**

   * **PowerShell**:

     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **Command Prompt**:

     ```cmd
     python -m venv .venv
     \.venv\Scripts\activate.bat
     ```

3. **Copy and edit environment variables**

   ```bash
   copy .env.example .env
   ```

   Edit `.env` (DO NOT commit):

   ```ini
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   DATABASE_URL=postgres://django_user:your_password@localhost:5432/myulibrarydb
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create the PostgreSQL database and user**

   ```sql
   -- In psql or your DB client:
   CREATE USER django_user WITH PASSWORD 'your_password';
   CREATE DATABASE myulibrarydb OWNER django_user;
   ```

6. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**

   ```bash
   python manage.py runserver
   ```

   Access the admin at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


---

*This README serves as an initial guide. Feel free to expand with API endpoint details, Docker instructions, frontend setup, or deployment steps as the project evolves.*
