# Book Management API

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.x
- Docker 

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/"yourcompany"/book-management-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd book-management-api
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

If you're not using Docker, make sure you have PostgreSQL installed and create a database for the project. Then, update the database settings in `myproject/settings.py` accordingly.

If you're using Docker, you can run the PostgreSQL database in a container. Make sure Docker is installed on your machine, then run the following command:

```bash
docker-compose up -d
```

4. Create PostgreSQL database (If not using Docker):
   
   - Open PostgreSQL shell:

     ```bash
     psql -U <username>
     ```

   - Create a new database:

     ```sql
     CREATE DATABASE <database_name>;
     ```

5. Update database settings:

    - Open `settings.py` file located in `myproject` directory.
    
    - Update the database configuration with your PostgreSQL credentials:

      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': '<database_name>',
              'USER': '<username>',
              'PASSWORD': '<password>',
              'HOST': 'localhost',
              'PORT': '5432',
          }
      }
      ```

6. Apply migrations:

    ```bash
    python manage.py makemigrations books 
    ```

7. Apply migrate:

    ```bash
    python manage.py migrate
    ```

8. Populate initial data:

    Run the following command to populate the database with initial data provided in the `populate_books.py` file:

    ```bash
    python manage.py populate_books
    ```

9. Running the server: 

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```
    The server should now be running locally at http://127.0.0.1:8000/
