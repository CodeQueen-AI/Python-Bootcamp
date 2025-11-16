import os

# Setting an environment variable (temporary for this session)
os.environ['API_KEY'] = '12345SECRET'

# Accessing environment variable
api_key = os.environ.get('API_KEY')
print("Your API Key is:", api_key)

# Checking if environment variable exists
if api_key:
    print("Environment variable accessed successfully!")
else:
    print("API Key not found!")

# Deleting environment variable (optional)
del os.environ['API_KEY']
print("Environment variable deleted.")
