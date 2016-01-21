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
  - In your newly created workspace, click on the terminal window (bottom pane).
  - Type `make` and return.
  - Enter your credentials from steps 1 and 2 when prompted.

Now, send a text to your Twilio number. You should get a response from your app! You're all set to start developing your first Twilio app.

##### `make` options
- `make clean` - Uninstalls your app.
- `make install` - Installs and configures your app.
- Use `make configure` if you want to change your stored configuration.
- `make serve` - Starts your server.
- `make serve app_route=<app_route>` - Starts your server and points your Twilio phone number's SMS URL to the custom application path specified on your server.
