from my_app.models import Test_Table
from my_app.func_lib.db_tools import create_tables, drop_tables, table_exist


def get_customer():
    create_tables("Test_Table")
    print('Hello from main.py')
    return ('Hello')
    # return cust.first_name
