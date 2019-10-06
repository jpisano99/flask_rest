from my_app import db
from my_app.models import *


def create_tables(tbl_name='all'):
    created = False
    if tbl_name == 'all':
        db.create_all()
        print('ALL Tables created')
        created = True
    elif table_exist(tbl_name) is False:
        try:
            eval(tbl_name)
        except NameError:
            print(tbl_name, "Model Not Found - Nothing Created")
            created = False
        else:
            print(tbl_name, "Not Found")
            db_cmd = tbl_name + ".__table__.create(db.session.bind)"
            exec(db_cmd)
            print('CREATED Table:', tbl_name)
            created = True
    elif table_exist(tbl_name) is True:
        print(tbl_name, 'Already Exists')
        created = False
    return created


def drop_tables(tbl_name='all'):
    dropped = False
    if tbl_name == 'all':
        db.drop_all()
        print('ALL Tables deleted')
        dropped = True
    elif table_exist(tbl_name) is True:
        sql = "DROP TABLE "+tbl_name+";"
        db.engine.execute(sql)
        print('DELETED Table:', tbl_name)
        dropped = True
    elif table_exist(tbl_name) is False:
        print(tbl_name, " does NOT exist")
        dropped = False
    return dropped


def table_exist(tbl_name):
    tbl_name = tbl_name.lower()
    sql = "SHOW TABLES;"
    existing_tbls = db.engine.execute(sql)
    tbl_exists = False

    for t_name in existing_tbls:
        if tbl_name == t_name[0]:
            tbl_exists = True
            break
    return tbl_exists


# def create_schema():
#     engine = sqlalchemy.create_engine('mysql://root:password@localhost')  # connect to server
#     engine.execute("CREATE SCHEMA IF NOT EXISTS `testdb`;")  # create db
#     engine.execute("USE testdb;")  # select new db
#
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:8milerun@localhost/testdb'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off annoying message
#     db = SQLAlchemy(app)
#     return




# def createdb():
#     #create_database('mysql+pymysql://root:YOUR_PASSWORD@aay9qgi0q2ps45.cp1kaaiuayns.us-east-1.rds.amazonaws.com/cust_ref_db')
#     print('Database created')
