H Leads CRM

Leads CRM is a web-based application developed using Python, Django, HTML, and Tailwind CSS. This application helps manage leads and clients efficiently, with features to view, add, edit, and delete records. It also includes authentication methods for secure access.

## Features

- **Dashboard:** Provides an overview and detailed information about leads and clients.
- **Leads Management:** Add, edit, view, and delete leads.
- **Clients Management:** Add, edit, view, and delete clients.
- **Authentication:** Secure user registration, login, and logout functionalities.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (default)

## Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.10 or later
- Node.js and npm (for Tailwind CSS)
- Django 5.0.6 or later

### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Mohshaikh23/Leads-CRM.git
   cd leads-crm
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv crm_django
   ```

3. **Activate the virtual environment:**

   ```sh
   # On Windows
   crm_django\Scripts\activate

   # On macOS/Linux
   source crm_django/bin/activate
   ```

4. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Install Node.js dependencies:**

   ```sh
   npm install
   ```

6. **Run database migrations:**

   ```sh
   python manage.py migrate
   ```

7. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

8. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

9. **Compile Tailwind CSS:**

   ```sh
   npx tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --watch
   ```

### Accessing the Application

Open your web browser and go to `http://127.0.0.1:8000/` to access the Leads CRM application. You can log in using the superuser credentials created earlier.

## Usage

### Dashboard

The dashboard provides an overview of the leads and clients. It displays the total number of leads and clients, along with some recent entries.

### Leads Management

- **View Leads:** Navigate to the Leads tab to view all leads.
- **Add Lead:** Click on the "Add Lead" button to add a new lead.
- **Edit Lead:** Click on the "Edit" button next to a lead to edit its details.
- **Delete Lead:** Click on the "Delete" button next to a lead to delete it.

### Clients Management

- **View Clients:** Navigate to the Clients tab to view all clients.
- **Add Client:** Click on the "Add Client" button to add a new client.
- **Edit Client:** Click on the "Edit" button next to a client to edit its details.
- **Delete Client:** Click on the "Delete" button next to a client to delete it.

### Authentication

- **Signup:** New users can register by clicking on the "Signup" link.
- **Login:** Registered users can log in using their credentials.
- **Logout:** Users can log out by clicking on the "Logout" link.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
```
