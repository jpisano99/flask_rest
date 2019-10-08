from my_app.func_lib.db_tools import create_tables, drop_tables, table_exist

# Use this file to place scripts that are called from views.py
def get_customer():
    create_tables("Test_Table")
    print('Hello from main.py')
    return ('Hello')
    # return cust.first_name
