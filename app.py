import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///reviews.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Review {self.id}: {self.rating}/10>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    reviews = Review.query.order_by(Review.created_at.desc()).all()
    avg_rating = 0
    if reviews:
        avg_rating = sum(review.rating for review in reviews) / len(reviews)
    return render_template('index.html', reviews=reviews, avg_rating=round(avg_rating, 1))

@app.route('/add_review', methods=['POST'])
def add_review():
    rating = request.form.get('rating', type=int)
    comment = request.form.get('comment')
    
    if not rating or rating < 1 or rating > 10:
        flash('Please provide a valid rating between 1 and 10.')
        return redirect(url_for('index'))
    
    new_review = Review(rating=rating, comment=comment)
    db.session.add(new_review)
    db.session.commit()
    
    flash('Thank you for your feedback!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
