from my_app.my_secrets import passwords
import os


# application predefined constants
app_cfg = dict(
    # RUNTIME_ENV='AWS',
    RUNTIME_ENV='LOCAL',
    # RUNTIME_ENV='PYTHONANYWHERE',
    VERSION=1.0,
    GITHUB="{url}",
    HOME=os.path.expanduser("~"),
    WORKING_DIR='my_working_dir',
    UPDATES_SUB_DIR='my_updates',
    ARCHIVES__SUB_DIR='my_archives',
    PROD_DATE='',
    UPDATE_DATE='',
    META_DATA_FILE='config_data.json',
)

# database configuration settings
# selected via the app_cfg['RUNTIME_ENV'] setting
if app_cfg['RUNTIME_ENV'] == 'AWS':
    # This is for a AWS based SQL db
    db_config = dict(
        DATABASE="test_db",
        USER="admin",
        PASSWORD=passwords["DB_PASSWORD"],
        HOST="database-1.cp1kaaiuayns.us-east-1.rds.amazonaws.com"
    )
elif app_cfg['RUNTIME_ENV'] == 'PYTHONANYWHERE':
    # This is for PythonAnywhere based SQL db
    db_config = dict(
        DATABASE="jpisano$test_db",
        USER="jpisano",
        PASSWORD=passwords["DB_PASSWORD"],
        HOST="jpisano.mysql.pythonanywhere-services.com"
    )
elif app_cfg['RUNTIME_ENV'] == 'LOCAL':
    # This is for a local based SQL db
    db_config = dict(
        DATABASE="test_db",
        USER="root",
        PASSWORD=passwords["DB_PASSWORD"],
        HOST="localhost"
    )

# Smart sheet Config settings
ss_token = dict(
    SS_TOKEN=passwords["SS_TOKEN"]
)

