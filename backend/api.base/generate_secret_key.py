import os
#get a random string of 24 bytes
print(os.urandom(24))
#convert the bytes to a hex string for use in the app
print(os.urandom(24).hex())
