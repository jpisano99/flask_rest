def main():
    print('Hello from main.py')
    return

DS-2CD2342WD-I newer
DS-2CD2332-I
DS-2CD2332-I

import sys
path = '/home/jpisano/ta_adoption_r2/'
if path not in sys.path:
    sys.path.append(path)

from ta_adoption import app as application  # noqa
