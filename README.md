# Django Blog Application

A modern blog application built with Django, featuring a clean UI with Tailwind CSS and Markdown support for content creation.

## Features

- Create, Read, Update, and Delete blog posts
- Markdown editor support using SimpleMDE
- Responsive design with Tailwind CSS
- Image upload functionality
- User-friendly interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/django-blogs.git
cd django-blogs
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the application.

## Create Superuser

To access the Django admin interface and manage your blog:

1. Create a superuser account:
```bash
python manage.py createsuperuser
```

2. Follow the prompts to set:
   - Username
   - Email address
   - Password

3. Access the admin interface at:
   http://127.0.0.1:8000/admin

## Usage

- **View Blogs**: Visit the homepage to see all blog posts
- **Create Blog**: Click "Create Blog" button to write a new post
- **Edit Blog**: Click "Edit" on any blog post to modify it
- **Delete Blog**: Use the "Delete" button to remove a blog post
- **View Single Blog**: Click on a blog title to view the full post

## Technology Stack

- Django 4.x
- Python 3.x
- Tailwind CSS
- SimpleMDE (Markdown Editor)
- SQLite (Database)