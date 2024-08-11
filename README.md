# dj-RoofRealEstate
## Description
A Django web application designed to provide real estate price estimations, along with additional features like a blog, contact us page, and various informational sections.

## Features
* **Real Estate Price Estimations**: Provide accurate price estimations for real estate properties.
* **Blog**: Share articles and updates related to real estate.
* **Contact Us**: A form for visitors to get in touch with you.
* **Informational Sections**: Various sections to provide detailed information about real estate.
## Database Setup
You need to create the database first. Follow these steps:

1. Install MySQL:
  If you want to use other database management systems, you need to modify the settings.py file accordingly.
   
3. Create Database:
  The default name used in settings.py is `real_estate`
  ```
  CREATE DATABASE `real_estate`;
  ```
## Installation
1. Clone the repository:
```
git clone https://github.com/SamEag1e/dj-RoofRealEstate.git
```
2. Navigate to the project directory:
```
cd dj-RoofRealEstate
```
3. Create a virtual environment:
```
python -m venv env
```
4. Activate the virtual environment:
* On Windows:
```
.\env\Scripts\activate
```
* On macOS and Linux:
```
source env/bin/activate
```
5. Install the required dependencies:
```
pip install -r requirements.txt
```
6. Set up environment variables:
* Create a .env file in the project root directory.
* Add the following environment variables:
```
DJANGO_SECRET_KEY = "your_secret_key"
DEBUG = 1 or 0
DATABASE_USERNAME = "your_database_username"
DATABASE_PASSWORD = "your_database_password"
EMAIL_HOST_USERNAME = "email@example.com"
EMAIL_HOST_PASSWORD = "your_email_host_password"

```
7. Run migrations:
```
python manage.py migrate
```
8. Start the development server:
```
python manage.py runserver
```

## Usage
* Access the web app by navigating to http://127.0.0.1:8000/ in your web browser.
* Use the admin panel to add projects and manage content.
## Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Commit your changes (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.
## License
This project is licensed under the MIT License.
