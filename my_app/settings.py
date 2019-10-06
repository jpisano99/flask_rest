from my_app.my_secrets import passwords
import os

# database configuration settings
if os.getenv("PYTHONANYWHERE_DOMAIN") is None:
    # This is for a local SQL db
    db_config = dict(
        DATABASE="ta_customer_db",
        USER="root",
        PASSWORD=passwords["DB_PASSWORD"],
        HOST="localhost"
    )
else:
    # This is for pythonAnywhere
    db_config = dict(
        DATABASE="jpisano$ta_adoption_db",
        USER="jpisano",
        PASSWORD=passwords["DB_PASSWORD"],
        HOST="jpisano.mysql.pythonanywhere-services.com"
    )

# Smart sheet Config settings
ss_token = dict(
    SS_TOKEN=passwords["SS_TOKEN"]
)

# application predefined constants
app_cfg = dict(
    VERSION=1.0,
    GITHUB="{url}",
    HOME=os.path.expanduser("~"),
    WORKING_DIR='ta_adoption_data',
    UPDATES_DIR='ta_data_updates',
    ARCHIVES_DIR='archives',
    PROD_DATE='',
    UPDATE_DATE='',
    META_DATA_FILE='config_data.json',
)
