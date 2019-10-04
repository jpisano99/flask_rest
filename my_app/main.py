from my_app.models import Customers


def get_customer():
    cust = Customers.query.filter_by(first_name='Jim').first()
    print(cust.first_name)
    print('Hello from main.py')
    # return ('Hello')
    return cust.first_name
