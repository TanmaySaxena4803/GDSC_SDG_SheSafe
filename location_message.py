import requests

# Define the URL of the Geolocation API
url = "https://geolocation-db.com/json/"

# Send a request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response and extract the location data
    data = response.json()
    latitude = data["latitude"]
    longitude = data["longitude"]
    city = data["city"]
    state = data["state"]
    country = data["country_name"]

    # Print the location data
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("City:", city)
    print("State:", state)
    print("Country:", country)
else:
    print("Failed to retrieve location data")



import geocoder
from twilio.rest import Client

# Get the user's location
g = geocoder.ip('me')
latitude, longitude = g.latlng

# Set up the Twilio client
account_sid = "AC066bf6bbc599ba9e59b0f38ebd451c13"
auth_token = "fa7dec81b81f482e8158f027ed6d29c1"
client = Client(account_sid, auth_token)

# Define the message and the recipient
maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
message = f"My location is: {latitude}, {longitude}\nClick here for Google Maps: {maps_link}"
recipient = "+919887551644"

# Send the message
message = client.messages.create(to=recipient, from_="+15746867192", body=message)






from twilio.rest import Client

# Set up the Twilio client
account_sid = "AC066bf6bbc599ba9e59b0f38ebd451c13"
auth_token = "fa7dec81b81f482e8158f027ed6d29c1"
client = Client(account_sid, auth_token)

# Define the recipient
recipient = ["+919887551644"]

# Make the call
call = client.calls.create(to=recipient, from_="+15746867192", url="http://twimlets.com/message?Message%5B0%5D=My%20location%20is%3A%20{}%2C%20{}".format(latitude, longitude))
