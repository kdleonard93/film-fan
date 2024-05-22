# Film Fan

## Description

Film Fan is sleek web application built using Svelte and Django, designed for movie enthusiasts. This app allows users to create personalized accounts, build, and manage their film lists with comprehensive CRUD (Create, Read, Update, Delete) functionalities.

## **Project Setup**

### **Prerequisites**

- Python 3.8 or higher
- Node.js and npm
- A PostgreSQL database (or another database of your choice, but you'll need to configure it in Django settings)

## Installation

### **Backend Setup (Django)**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kdleonard93/film-fan.git
   cd film-fan
   ```

2. **Set Up a Virtual Environment (Optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Backend Dependencies**

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Database Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Django Server**

   ```bash
   python manage.py runserver
   ```

### **Frontend Setup (SvelteKit)**

1. **Navigate to the Frontend Directory**

   ```bash
   cd ../frontend  # Assuming you're in the backend directory
   ```

2. **Install Frontend Dependencies**

   ```bash
   npm install
   ```

3. **Run the Development Server**

   ```bash
   npm run dev
   ```

## **Using the Application**

- The Django backend serves a RESTful API for film data.
- The SvelteKit frontend provides an interactive UI to view, add, and manage films.
- Visit `http://localhost:5173` (or however your local is set) in your browser to interact with the application.

## **Deployment**

- Instructions for deploying the Django backend (TBD)
- Instructions for deploying the SvelteKit frontend (TBD)

## **License**

This project is licensed under the MIT License

## **Acknowledgments**

- This project was built as part of a learning journey in full-stack development.
- Special thanks to the SvelteKit and Django communities for their extensive documentation and support.

## **Contact**

For any queries or suggestions, feel free to contact Kyle Leonard - contact@digitaldopamine.dev.
