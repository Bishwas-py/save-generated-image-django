# Save generated image programatically in Django

This is a quick simple Django app that allows you to save a generated image in Django. Here
is the [blog post](https://blog.webmatrices.com/how-to-save-generated-image-django/) that explains how
this works. 

## Installation

### Clone the repository

```bash
git clone github.com/bishwas-py/save-generated-image-django.git
```

### Install the requirements

```bash
pip install -r requirements.txt
```

### Migrate the database

```bash
python manage.py migrate
```

### Run the server

```bash
python manage.py runserver
```

## Usage

- Go to `http://localhost:8000/admin` in your browser.
- Click on the `Websites` in the `records` tab.
- Click on `Add` button.
- Enter the `name` and `url` of the website.
- Click on `Save and continue editing` button.
- Go the image link you will see below of the form.

Happy Coding!