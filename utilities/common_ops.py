import os
import time
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

# Resolve relative to this file's own location, one level up from utilities/,
# so it works regardless of cwd or which script/test invoked it.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CONFIG_PATH = os.path.join(_PROJECT_ROOT, 'configuration', 'data.xml')

# Load a local .env file (not committed) so secrets can be supplied without
# putting them in data.xml. No-op if the file doesn't exist.
load_dotenv(os.path.join(_PROJECT_ROOT, '.env'))

# DB credentials are secrets: prefer environment variables over data.xml.
_ENV_OVERRIDE_MAP = {
    'DB_User': 'DB_USER',
    'DB_Pass': 'DB_PASS',
}


def get_data(node_name):
    #Get configuration data from XML file, with secret keys overridable via environment variables
    env_key = _ENV_OVERRIDE_MAP.get(node_name)
    if env_key:
        env_value = os.environ.get(env_key)
        if env_value:
            return env_value
    root = ET.parse(_CONFIG_PATH).getroot()
    return root.find('.//' + node_name).text

def get_time_stamp():
    # Used to make failure screenshot file names unique
    return  time.time()

#Emum for selecting whether we want to save mortgage transactions or not
class Save:
    Yes = True
    No = False

#Emum for selecting directions
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'

