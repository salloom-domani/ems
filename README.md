## Requirements

you should have installed in your machine
1. python 3.8 or higher
2. pipenv pakcage which you can install it with

    ```
    pip install pipenv
    ```

## Getting Started

1. clone the repo

    ```
    git clone https://github.com/salloom99/ems
    ```
2. go to the project directory

    ```
    cd ems    
    ```
3. create a virtual environment and install the dependant packages then run the venv shell

    ```
    pipenv install

    pipenv shell
    ```
4. migrate the models of the database to your current sqlite db

    ```
    python manage.py migrate    
    ``` 
5. finally to start the project run the following

    ```
    python manage.py runserver    
    ```

## Additional Commands

- you can create an admin user to acces the admin page

    ```
    python manage.py createsuperuser    
    ```
    and then enters a username and a password for this new account.