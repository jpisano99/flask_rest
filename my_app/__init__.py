import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from my_app.settings import app_cfg, db_config
from base64 import b64encode
from my_app.my_secrets import passwords


app = Flask(__name__)

# Assign App Config Variables / Create a random token for Flask Session
token = os.urandom(64)
token = b64encode(token).decode('utf-8')
app.config['SECRET_KEY'] = token

# Get the Passwords and Keys
print()
print("I have a DB Password: ", my_secrets.passwords["DB_PASSWORD"])
print("I have an API Key: ", my_secrets.passwords["SS_TOKEN"])
print("I have an Flask Secret Key: ", app.config['SECRET_KEY'])
print()

#
# database configuration settings
#
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' +\
                                            db_config['USER'] +\
                                        ':'+db_config['PASSWORD'] +\
                                        '@'+db_config['HOST']+':3306/' +\
                                            db_config['DATABASE']




SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="<the username from the 'Databases' tab>",
    password="<the password you set on the 'Databases' tab>",
    hostname="<the database host address from the 'Databases' tab>",
    databasename="<the database name you chose, probably yourusername$comments>",


#
# # Create db for SQL Alchemy
db = SQLAlchemy(app)

# Are we connected ?
db_host = []
db_port = []
db_user = []
db_status = (db.engine.execute("SHOW VARIABLES WHERE Variable_name = 'port'"))
for x in db_status:
    db_port = x.values()

db_status = (db.engine.execute("SHOW VARIABLES WHERE Variable_name = 'hostname'"))
for x in db_status:
    db_host = x.values()

db_status = (db.engine.execute('SELECT USER()'))
for x in db_status:
    db_user = x.values()

print('You are connected to MySQL Host '+db_host[1]+' on Port '+db_port[1]+' as '+db_user[0])


from my_app import views
from my_app import models
