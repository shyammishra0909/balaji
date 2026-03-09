# TechLearn Institute Website

A responsive website for a computer institute built with HTML, CSS, JavaScript, and Python Flask backend with SQLite database.

## Features

- Responsive design that works on all devices
- Smooth scrolling navigation
- Hero section with background image
- About section with key features
- Courses showcase
- Contact form with backend submission and database storage
- Animated course cards on scroll
- Admin endpoint to view submitted contacts

## How to Run

1. Install dependencies: `pip install flask flask-sqlalchemy`
2. Run the backend: `python app.py`
3. Open your browser and go to `http://127.0.0.1:5000`

## API Endpoints

- `GET /` - Main website
- `POST /contact` - Submit contact form
- `GET /admin/contacts` - View all submitted contacts (JSON)

## Files

- `index.html` - Main HTML structure
- `style.css` - Styling and responsive design
- `script.js` - JavaScript for interactivity and form submission
- `app.py` - Flask backend with SQLite database
- `contacts.db` - SQLite database (created automatically)

## Production Deployment

For production, set `debug=False` in `app.py` and use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 app:app
```

Or use a production server like Nginx + Gunicorn.