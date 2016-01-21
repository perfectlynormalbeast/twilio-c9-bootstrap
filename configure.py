import json
import os
import sys

if __name__ == "__main__":
    # Parse command line arguments
    argc = len(sys.argv)
    if argc != 2:
        print "Usage: python configure.py <config_file>"
        exit(-1)
    else:
        config_filepath = sys.argv[1]

    # Check for existing configuration file
    if os.path.isfile(config_filepath):
        override = raw_input(
            "Do you want to overwrite your existing configuration file? (y/n): ")
        if override == 'y':
            os.remove(config_filepath)
        elif override == 'n':
            exit(0)
        else:
            print "Unknown response: " + override
            exit(-1)

    # Get new configuration
    properties = {}
    properties['account_sid'] = raw_input("Account SID: ")
    properties['auth_token'] = raw_input("Auth Token: ")
    properties['phone_number_sid'] = raw_input("Phone Number SID: ")

    # Store new configuration
    print "Storing configuration in: " + config_filepath
    config_file = open(config_filepath, 'w')
    json.dump(properties, config_file)
    config_file.flush()
    config_file.close()
