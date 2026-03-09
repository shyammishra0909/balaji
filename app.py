from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'error': 'All fields are required'}), 400

    # Save to database
    new_contact = Contact(name=name, email=email, message=message)
    db.session.add(new_contact)
    db.session.commit()

    print(f"New contact message saved: {name} ({email})")

    return jsonify({'message': 'Thank you for your message! We will get back to you soon.'})

@app.route('/admin/contacts')
def view_contacts():
    contacts = Contact.query.all()
    contacts_list = []
    for contact in contacts:
        contacts_list.append({
            'id': contact.id,
            'name': contact.name,
            'email': contact.email,
            'message': contact.message,
            'timestamp': contact.timestamp
        })
    return jsonify(contacts_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)