# The Pooler

This project was developed to serve as a way to examine my abilities during the screening process for AlphaTrade. It consists of a web app created with Django.

The functional requirements were:

"A user must register and then log into the system. As long as this user is connected, he can create as many polls (multiple choice) as he wants, in addition to being able to answer polls created by other users."

## How to install
1. Clone this project
    ```bash
    git clone https://github.com/OsnielLopes/at-screening.git
    ```
2. _Optional_. Create a virtual envirtonment. It helps to keep things organized! 😉 If you don't know how to do it, here you can learn more: [Virtualenv Introduction](https://virtualenv.pypa.io/en/latest/user_guide.html#introduction).
3. Install the requirements
    ```bash
   cd at-screening
    pip install -r requirements.txt
    ```
4. Migrate the database to create and prepare the schema
    ```bash
    python manage.py migrate
    ```
5. Run the project!
    ```bash
   python manage.py runserver
   ```
