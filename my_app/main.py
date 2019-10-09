from my_app.func_lib.db_tools import create_tables, drop_tables, table_exist
from my_app.func_lib.get_list_from_ss import get_list_from_ss
from my_app.func_lib.open_wb  import open_wb
from my_app.func_lib.push_list_to_xls import push_list_to_xls


# Use this file to place scripts that are called from views.py
def get_customer():
    print('Hello from main.py')

    create_tables("Test_Table")

    ss_test_list = get_list_from_ss('Tetration SKUs')
    print('Rows in my SmartSheet', len(ss_test_list))

    push_list_to_xls(ss_test_list,'jim.xlsx')



    # xws, wb = open_wb('test.xlsx')
    return ('Hello')
    # return cust.first_name
