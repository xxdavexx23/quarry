import os
#get a random string of 24 bytes
print(os.urandom(24))
#convert the bytes to a hex string for use in the app
print(os.urandom(24).hex())

# Note: the secret key for a flask app should be kept secret and not shared with anyone.
# it's purpose is to cryptographically sign cookies and other data that is sent to the client.