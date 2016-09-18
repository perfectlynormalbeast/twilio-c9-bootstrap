import json
import os
import re
import sys
from twilio.rest import TwilioRestClient

def validate_input(string, prefix=None):
    if prefix is not None:
        prefix_regexp = re.compile('\A[A-Z]{2}\Z')
        prefix_match = prefix_regexp.match(prefix)
        if prefix_match is None:
            raise RuntimeError('Invalid prefix: ' + prefix)
    else:
        prefix = ''
    sid_regexp = re.compile('\A' + prefix + '[0-9a-f]{32}\Z')
    sid_match = sid_regexp.match(string)
    if sid_match is None:
        raise RuntimeError('Invalid input: ' + string)

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
    validate_input(properties['account_sid'], 'AC')
    properties['auth_token'] = raw_input("Auth Token: ")
    validate_input(properties['auth_token'])
    properties['phone_number_sid'] = raw_input("Phone Number SID: ")
    validate_input(properties['phone_number_sid'], 'PN')

    # Validate credentials and get phone number
    client = TwilioRestClient(properties['account_sid'], properties['auth_token'])
    number = client.phone_numbers.get(properties['phone_number_sid'])
    properties['phone_number'] = number.phone_number
    print "Phone Number: " + properties['phone_number']

    # Store new configuration
    print "Storing configuration in: " + config_filepath
    config_file = open(config_filepath, 'w')
    json.dump(properties, config_file)
    config_file.flush()
    config_file.close()
