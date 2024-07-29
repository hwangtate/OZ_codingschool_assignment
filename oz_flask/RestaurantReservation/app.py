from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1025@localhost/restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    customer_phone = db.Column(db.String(255), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.Text)

    def __repr__(self):
        return f"<Reservation {self.customer_name}>"

# Create tables
with app.app_context():
    db.create_all()

# Home route to show reservations and a form to add new ones
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_reservation = Reservation(
            customer_name=request.form['customer_name'],
            customer_phone=request.form['customer_phone'],
            reservation_time=request.form['reservation_time'],
            number_of_people=request.form['number_of_people'],
            special_requests=request.form['special_requests']
        )
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        all_reservations = Reservation.query.all()
        return render_template('index.html', reservations=all_reservations)

if __name__ == '__main__':
    app.run(debug=True)
