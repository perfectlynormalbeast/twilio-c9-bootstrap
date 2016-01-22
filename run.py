from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)
 
@app.route("/app", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
