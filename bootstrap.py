import json
import os
import sys
from twilio.rest import TwilioRestClient

VARNAME_HOSTNAME = 'C9_HOSTNAME'
DEFAULT_APP_ROUTE = 'app'

if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) != 2:
        print "Usage: python run.py <config_file>"
        exit(-1)
    config_filepath = sys.argv[1]

    # Get app path from user
    app_route = raw_input("Enter custom app route (press return to use default): ");
    if len(app_route) is 0:
        app_route = DEFAULT_APP_ROUTE

    # Parse configuration file
    try:
        config_file = open(config_filepath, 'r')
        config = json.load(config_file)
    except IOError:
        print "Configuration file not found - run `make install`"
        exit(-1)
    print "Account SID: " + config['account_sid']
    print "Auth Token: " + config['auth_token']
    print "Phone Number SID: " + config['phone_number_sid']

    # Scrape app url from env and update PN SMS URL
    app_url = 'http://' + os.environ[VARNAME_HOSTNAME] + '/' + app_route
    print "App URL: " + app_url
    print "Updating SMS URL for phone number..."
    client = TwilioRestClient(config['account_sid'], config['auth_token'])
    try:
        number = client.phone_numbers.update(config['phone_number_sid'], sms_url=app_url)
    except:
        print "Could not update your Twilio phone number SMS URL"
        print "First, check your internet connection"
        print "Also, try reconfiguring by running `make configure`"
        exit(-1)
