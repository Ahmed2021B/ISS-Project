from pip._vendor.distlib.compat import raw_input
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0d57ba4a9f2c35200e005637afee97e7"
# Your Auth Token from twilio.com/console
auth_token  = "82677a1fc1a20ef0ba7f79ea1b78d06c"

client = Client(account_sid, auth_token)

while 1:
    phone=raw_input("Insert phone number: ")
    text=raw_input("Insert message: ")

    message = client.messages.create(
        to=phone,
        from_="+15039469402",
        body=text)

    print(message.sid)
    print("")
    repeat=raw_input("You want send SMS again (Y/N): ")
    if repeat == "N" or repeat == "n":
        break