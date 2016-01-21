import json
import os
import sys
from twilio.rest import TwilioRestClient

VARNAME_HOSTNAME = 'C9_HOSTNAME'
DEFAULT_APP_ROUTE = 'app'

if __name__ == "__main__":
    # Parse command line arguments
    argc = len(sys.argv)
    if argc < 2 or argc > 3:
        print "Usage: python run.py <config_file> [<app_route>]"
        exit(-1)
    elif argc == 3:
        app_route = sys.argv[2]
        print "Launching custom app route: " + app_route
    else:
        app_route = DEFAULT_APP_ROUTE
        print "Launching default app route"
    config_filepath = sys.argv[1]

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
