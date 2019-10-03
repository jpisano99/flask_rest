from my_app.my_secrets import passwords
import os

# database configuration settings
db_config = dict(
    DATABASE="ta_customer_db",
    USER="root",
    PASSWORD=passwords["DB_PASSWORD"],
    HOST="localhost"
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



