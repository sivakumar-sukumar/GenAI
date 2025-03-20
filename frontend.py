from __future__ import print_function # Needed if you want to have console output using Flask
import requests
import sys
import json
import os
import time
from flask import Flask, request
import json
import pika
from webexteamssdk import WebexTeamsAPI
import ssl
import subprocess

token = 'Enter your bot access_token here !'  # You can get it on https://developer.webex.com/endpoint-messages-post.html

app = Flask(__name__)

@app.route("/",methods=['POST'])    # all request for localhost:5000/  will reach this method
def webhook():

    # Get the json data
    json = request.json

    # Retrieving message ID, person ID, email and room ID from message received

    message_id = json["data"]["id"]
    user_id = json["data"]["personId"]
    email = json["data"]["personEmail"]
    room_id = json["data"]["roomId"]

    print (message_id, file = sys.stdout)
    print(user_id, file=sys.stdout)
    print(email, file=sys.stdout)
    print(room_id, file=sys.stdout)


    if user_id != '***INPUT USER ID***':

        #Loading the message with the message ID

        global token  #Retrieving token from Global variable

        header = {"Authorization": "Bearer %s" % token}
        get_rooms_url = "https://api.ciscospark.com/v1/messages/" + message_id
        api_response = requests.get(get_rooms_url, headers=header, verify=False)
        response_json = api_response.json()
        message = response_json["text"]
        p = subprocess.Popen(['python', 'backend.py', arg1], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, errors = p.communicate()    
        print(output)
        print(message, file= sys.stdout)

        print('******************', file=sys.stdout)

        # You can do whatever you want with the message,person_id,room_id over here !

        return "Success!"

    else:

        return "It's my own messages ... ignoring it"



os.popen("pkill ngrok") # clearing previous sessions of ngrok (if any)
os.popen("ngrok http 5000 &")  # Opening Ngrok in background
time.sleep(5) #Leaving some time to Ngrok to open
term_output_json = os.popen('curl http://127.0.0.1:4040/api/tunnels').read()   # Getting public URL on which NGROK is listening to
tunnel_info = json.loads(term_output_json)
public_url = tunnel_info['tunnels'][0]['public_url'] 


# Registering Webhook
header = {"Authorization": "Bearer %s" % token, "content-type": "application/json"}
requests.packages.urllib3.disable_warnings() #removing SSL warnings
post_message_url = "https://api.ciscospark.com/v1/webhooks"

# Preparing the payload to register. We are only interested in messages here, but feel free to change it
payload = {
    "resource": "messages",
    "event": "all",
    "targetUrl": public_url,
    "name": "MyWonderfulWebHook"
}

api_response = requests.post(post_message_url, json=payload, headers=header, verify=False) #Registering webhook

if api_response.status_code != 200:
    print ('Webhook registration Error !')
    exit(0)

if __name__ == '__main__':
    app.run(host='localhost', use_reloader=True, debug=True)
