from my_app.models import Bookings


def get_customer():
    cust = Bookings.query.filter_by(erp_end_customer_name='Clarivate Analytics').first()
    print(cust.erp_end_customer_name)
    print('Hello from main.py')
    return cust.erp_end_customer_name
