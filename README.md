# Superheroes Flask API

This is a simple RESTful API built with Flask for managing superheroes, their powers, and the strengths of those powers.

## Features

- View all heroes
- View hero by ID
- View all powers
- Update a power's description
- Assign powers to heroes with strength levels

## Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd superheroes

2. **install dependencies**
   ```pipenv install
   ```pipenv shell

3. **Set up the database**
     flask db init
flask db migrate -m "Initial migration"
flask db upgrade

4. **run server**
 flask run

Tools

Python 3.13
Flask
SQLAlchemy
Flask-Migrate
SQLite

Testing

You can import the provided Postman collection to test all endpoints manually.

Made by [Jeannette Derek]



