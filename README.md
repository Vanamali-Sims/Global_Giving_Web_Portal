# Global_Giving_Web_Portal

# Global Giving Portal

Global Giving Portal is a web application designed to facilitate communication and collaboration between NGOs (Non-Governmental Organizations) and philanthropists. It provides a platform where philanthropists can connect with NGOs, NGOs can find donors, and resources can be allocated efficiently. The portal is built using HTML, CSS with Bootstrap, JavaScript for the frontend, and Django for the backend. It is a dynamic and user-friendly system that supports multiple types of logins based on roles.

## Features

### For NGOs

- **Create and Manage Projects:** NGOs can create and manage projects by providing detailed information, including project goals, descriptions, and resource requirements.

- **Connect with Donors:** NGOs can connect with potential donors who are interested in supporting their projects.

- **Update Project Progress:** NGOs can regularly update project progress to keep donors informed and engaged.

### For Philanthropists

- **Browse Projects:** Philanthropists can browse and search for projects that align with their interests and values.

- **Contribute to Projects:** Philanthropists can contribute to projects by providing financial or other types of support.

- **Track Contributions:** Philanthropists can track their contributions and monitor project progress.

### General Features

- **User Authentication:** The system supports multiple types of logins based on user roles, including NGO representatives, philanthropists, and administrators.

- **User Profiles:** Users can create and update their profiles to showcase their interests, expertise, and contributions.

- **Real-time Messaging:** Users can communicate with each other through a messaging system built into the platform.

- **User-friendly Interface:** The frontend is designed with Bootstrap and offers a responsive and intuitive user interface.

- **Dynamic and Interactive:** The application is dynamic, offering real-time updates and interactions to enhance user experience.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/global-giving-portal.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application by opening a web browser and navigating to [http://localhost:8000](http://localhost:8000).

## Configuration

You can configure the application by modifying the settings in the `globalgiving/settings.py` file. Update database settings, email settings, and other configuration options as needed.

## Usage

1. Create an account based on your role (NGO, Philanthropist, or Administrator).

2. Log in to the portal using your credentials.

3. Explore available projects, create your own projects, connect with donors, or make contributions.

4. Use the built-in messaging system to communicate with other users.

5. Regularly update project progress to keep donors informed and engaged.

