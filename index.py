# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client # type: ignore

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="This is an example message with MMS",
    from_="+15017122661",
    media_url=[
        "https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg"
    ],
    to="+15558675310",
)

print(message.body)