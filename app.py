import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", 
            "help", 
            "laptop",
            "desktop",
            "phone",
            "info",
            "apple_phone",
            "apple_laptop",
            "apple_desktop",
            "samsung",
            "asus_laptop",
            "asus_desktop",
            "msi_laptop",
            "msi_desktop",
            "hwawei",
            "microsoft",
            "youtuber",
            "report",
            "ted"
            ],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "help",
            "conditions": "is_going_to_help",
        },
        {
            "trigger": "advance",
            "source": "help",
            "dest": "laptop",
            "conditions": "is_going_to_laptop",
        },
        {
            "trigger": "advance",
            "source": "help",
            "dest": "desktop",
            "conditions": "is_going_to_desktop",
        },
        {
            "trigger": "advance",
            "source": "help",
            "dest": "phone",
            "conditions": "is_going_to_phone",
        },
        {
            "trigger": "advance",
            "source": "help",
            "dest": "info",
            "conditions": "is_going_to_info",
        },
        {
            "trigger": "advance",
            "source": "laptop",
            "dest": "apple_laptop",
            "conditions": "is_going_to_apple_laptop",
        },
        {
            "trigger": "advance",
            "source": "laptop",
            "dest": "microsoft",
            "conditions": "is_going_to_microsoft",
        },
        {
            "trigger": "advance",
            "source": "laptop",
            "dest": "asus_laptop",
            "conditions": "is_going_to_asus_laptop",
        },
        {
            "trigger": "advance",
            "source": "laptop",
            "dest": "msi_laptop",
            "conditions": "is_going_to_msi_laptop",
        },
        {
            "trigger": "advance",
            "source": "desktop",
            "dest": "apple_desktop",
            "conditions": "is_going_to_apple_desktop",
        },
        {
            "trigger": "advance",
            "source": "desktop",
            "dest": "asus_desktop",
            "conditions": "is_going_to_asus_desktop",
        },
        {
            "trigger": "advance",
            "source": "desktop",
            "dest": "msi_desktop",
            "conditions": "is_going_to_msi_desktop",
        },
        {
            "trigger": "advance",
            "source": "phone",
            "dest": "apple_phone",
            "conditions": "is_going_to_apple_phone",
        },
        {
            "trigger": "advance",
            "source": "phone",
            "dest": "samsung",
            "conditions": "is_going_to_samsung",
        },
        {
            "trigger": "advance",
            "source": "phone",
            "dest": "hwawei",
            "conditions": "is_going_to_hwawei",
        },
        {
            "trigger": "advance",
            "source": "info",
            "dest": "ted",
            "conditions": "is_going_to_ted",
        },
        {
            "trigger": "advance",
            "source": "info",
            "dest": "report",
            "conditions": "is_going_to_report",
        },
        {
            "trigger": "advance",
            "source": "info",
            "dest": "youtuber",
            "conditions": "is_going_to_youtuber",
        },
        {"trigger": "go_back", "source": ["help", "laptop", "gender", "desktop", "info","apple_phone","apple_desktop","apple_laptop","msi_desktop","msi_laptop","asus_laptop","asus_desktop","microsoft","hwawei","samsung", "youtuber", "report", "ted"], "dest": "help"},
        {"trigger": "advance", "source": ["apple_phone","apple_desktop","apple_laptop","msi_desktop","msi_laptop","asus_laptop","asus_desktop","microsoft","hwawei","samsung", "youtuber", "report", "ted"], "dest": "help"}
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)



app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def webhook_handler():
    
    signature = request.headers["X-Line-Signature"]
    
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        
        # user state will stop here
        if (machine.state == "user" and response == False):
            send_text_message(event.reply_token, "Interact with our ordering system <HELP> to get more !!!")
            print(f"P1 STATE: \n{machine.state}")
            print(f"P1 EVENT: \n{event}")
            print(f"P1 RESPONSE: \n{response}")
            continue
        
        else:
            
            # start the code here
            # other states will start from here 

            if (machine.state == event.message.text.lower()):
               machine.advance(event)
               
            else:
                # after executing the instruction 
                machine.go_back(event)
            
            continue


    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")

    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)

