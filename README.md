# Presentation Feedback Application

A simple web application built with Flask that allows users to rate presentations and leave comments.

## Features

- Rate presentations on a scale of 1-10
- Leave optional comments with your rating
- View all previous ratings and comments
- See the average rating

## Requirements

- Python 3.8 or higher
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set up a Python virtual environment

If using pyenv (as detected in your environment):

```bash
# First make sure the correct Python version is active
pyenv global 3.8.18  # or your preferred version

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

If using standard Python:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python3 app.py
```

The application will be available at http://127.0.0.1:5000/

## Database

The application uses SQLite as its database, which is stored in the file `reviews.db`. This file will be created automatically when you first run the application.

## Project Structure

- `app.py`: Main application file containing the Flask routes and database models
- `templates/index.html`: HTML template for the web interface
- `requirements.txt`: List of Python dependencies
- `reviews.db`: SQLite database file (created on first run)

## Customization

You can customize the application by:

- Modifying the HTML template in `templates/index.html`
- Changing the database configuration in `app.py`
- Adding additional features to the Flask application
