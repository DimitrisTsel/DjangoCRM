# Django CRM Project

🚀 https://djangocrm-yu3y.onrender.com 

## Overview
This is a Customer Relationship Management (CRM) system built using Django, designed to manage interactions with current and potential customers. It provides user authentication and authorization system for users and administrators. It also provides functionalities for storing customer records, updating and deleting them.

## Features
- **User Authentication**: Secure authentication and authorization system for users.
- **Customer Management**: Create, update, and delete customer profiles.
- **Records**: Create, update, delete customer records.
- **Task Management**: Assign tasks to team members and track their completion.

## Installation
1. Clone the repository:
https://github.com/DimitrisTsel/DjangoCRM.git

2. Navigate to the project directory: `cd dcrm`
3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
4. Install dependencies:
`pip install -r requirements.txt`

5. Apply database migrations:
`python manage.py migrate`

6. Create a superuser account:
   `python manage.py createsuperuser`

7. Start the development server:
`python manage.py runserver`

8. Access the CRM application at `http://localhost:8000` in your web browser.

## Usage
- **Admin Interface**: Access the Django admin interface at `/admin` to manage users, customers, leads, sales opportunities, tasks, etc.
- **API Endpoints**: Utilize the provided API endpoints for programmatic access to CRM functionalities.

## Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/DimitrisTsel/DjangoCRM/tree/main?tab=MIT-1-ov-file#readme) file for details.

## Acknowledgements
- [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines.
- [Bootstrap](https://getbootstrap.com/): Front-end framework for designing responsive and mobile-first websites.


