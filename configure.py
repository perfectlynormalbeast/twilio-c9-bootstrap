import json
import os

CONFIG_FILE = 'configure.json'

if __name__ == "__main__":
    properties = {}
    properties['account_sid'] = raw_input("Account SID: ")
    properties['auth_token'] = raw_input("Auth Token: ")
    properties['phone_number_sid'] = raw_input("Phone Number SID: ")
    try:
        os.remove(CONFIG_FILE)
    except OSError:
        pass
    config_file = open(CONFIG_FILE, 'w')
    json.dump(properties, config_file)
