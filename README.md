# twilio-bootstrap
###### Jumpstart your first Twilio app!

twilio-bootstrap is designed to make setting up your first Twilio app a breeze. Here's a walkthrough of how to get one up in no time.

1. Set up a Twilio account.
  - Make note of your Account SID & Auth Token, which can be found under your Account Settings page.
1. Buy a phone number.
  - Make note of its SID under the Phone Number page.
1. Set up a Cloud9 account and create a new workspace.
  - Under `Clone from Git or Mercurial URL` use `https://github.com/perfectlynormalbeast/twilio-bootstrap`
  - Under `Choose a template` use `Python`
1. Set up your starter code.
  - In the terminal window in your newly created workspace, enter the following commands:
    * `make install`
    * `make serve account_sid=<account_sid> auth_token=<auth_token> phone_number_sid=<phone_number_sid>`
      - Here fill in the things you made a note of in steps 1 and 2.

Now, send a text to your new Twilio number. You should get a response from your app! You're all set to start developing your first Twilio app.
