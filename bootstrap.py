import re
import requests
import subprocess
import sys
import time
from twilio.rest import TwilioRestClient

if __name__ == "__main__":
    # TODO Better arg input & validation (maybe using argparse)
    # Validate arguments
    if len(sys.argv) != 4:
        print("Usage: python bootstrap.py <account_sid> <auth_token> <phone_number>")
        sys.exit(-1)
    account_sid = sys.argv[1]
    auth_token = sys.argv[2]
    phone_number_sid = sys.argv[3]
    print "Account SID: " + account_sid
    print "Auth Token: " + auth_token
    print "Phone Number SID: " + phone_number_sid

    # Set up ngrok tunnel
    print "Waiting for ngrok to pick a subdomain..."
    subprocess.Popen(["./ngrok", "http", "5000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for ngrok to pick a subdomain
    time.sleep(5)

    # Scrape subdomain from ngrok
    response = requests.get("http://localhost:4040/inspect/http")
    app_id = re.search('http://(.*?).ngrok.io', response.content).group(1)
    app_url = "http://" + app_id + ".ngrok.io/"
    print "App URL: " + app_url

    # Update phone number SMS url
    print "Updating SMS URL for phone number..."
    client = TwilioRestClient(account_sid, auth_token)
    number = client.phone_numbers.update(phone_number_sid, sms_url=app_url)
