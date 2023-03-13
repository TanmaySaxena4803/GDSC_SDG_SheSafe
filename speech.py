import geocoder
from twilio.rest import Client
import speech_recognition as sr
import pyttsx3

# Twilio API credentials
account_sid = '<your_account_sid>'
auth_token = '<your_auth_token>'
client = Client(account_sid, auth_token)

# Recipient's phone number
recipient = '<recipient_phone_number>'

# Speech recognition engine
r = sr.Recognizer()

# Text to speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_location():
    # Get the current location using geocoder
    g = geocoder.ip('me')
    return g.latlng

def send_message(location):
    # Compose the message
    message = f"Help! I need your help. I am at {location[0]}, {location[1]}"

    try:
        # Send the message using Twilio API
        message = client.messages.create(to=recipient, from_="+14158494036", body=message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")

def call_recipient():
    try:
        # Call the recipient using Twilio API
        call = client.calls.create(to=recipient, from_="+14158494036", url='http://demo.twilio.com/docs/voice.xml')
        print("Call initiated successfully!")
    except Exception as e:
        print(f"An error occurred while making the call: {e}")

def protect_me():
    with sr.Microphone() as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Processing your request...")

    try:
        text = r.recognize_google(audio)
        if "protect me" in text.lower():
            print("Protecting you now...")
            location = get_location()
            send_message(location)
            call_recipient()
        else:
            print("Sorry, I didn't get that.")
    except Exception as e:
        print(f"An error occurred: {e}")

protect_me()
