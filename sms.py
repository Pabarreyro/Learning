from twilio import rest  # Importing the specific attribute "twilio.rest"

# Account SID from twilio.com/console
account_sid = "ACccf86cb549019c89a4d30a14ddca1b75"
# Auth Token from twilio.com/console
auth_token  = "64953930b47fd741ce348107c61656f0"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+12025382341",
    from_="+12405707370",
    body="Hello from Python!")

print(message.sid)

# What's happening in the background...
# class TwilioRestClient():
#     def __init__(self):
        