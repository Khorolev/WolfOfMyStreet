from flask import Flask, request
import json

# --------------------------------------------------------------
# 1) Download Ngrok
# 2) In the prompt (from the directory containing the ngrok.exe file):
#    ngrok config add-authtoken 2dE7....
# 3) In the prompt - to create the tunnel local host (port 5000) to internet
#    ngrok http 5000
# 4) Copy the link generated by Ngrok under "Forwarding" + '/webhookcallback' from where the webhook will be sent
# --------------------------------------------------------------


app = Flask(__name__)


# --------------------------------------------------------------
# Define endpoint
# --------------------------------------------------------------
@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        print("received data: ", data)
        jdata = json.loads(request.data)
        jdata_formatted = json.dumps(jdata, indent=2)
        print(jdata_formatted)
        return "Webhook received", 200
    if request.method == 'GET':
        print("Received a GET request")
    else:
        return "Request not allowed", 485

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
