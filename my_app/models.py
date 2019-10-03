from my_app import db


class Bookings(db.Model):
    __tablename__ = 'bookings'

    erp_end_customer_name = db.Column(db.String(100))
    total_bookings = db.Column(db.Float)
    product_id = db.Column(db.String(25))
    date_added = db.Column(db.DateTime)
    hash_value = db.Column(db.String(50), primary_key=True)
