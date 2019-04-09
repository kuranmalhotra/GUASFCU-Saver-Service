# # Round-Up Saver Application
# ## The purpose of this application is to help the user save money incrementally, by rounding up the transactions they perform on a daily basis to the nearest dollar, and depositing those extra few pennies into their savings account. 

import os
from datetime import datetime
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# Static Call Variables:

TOKEN = os.environ.get("token")
secret = os.environ.get("secret")
checking_id = os.environ.get("42993X_ID")
savings_id = os.environ.get("42993X_ID")
signature_imported = os.environ.get("sig")
base_url = 'https://api.guasfcu.com/v1/'

# Commented out code to ignore pull request and just work off of a transaction pull json output file (ignored to preserve personal data)

# date = os.environ.get("NARMI_DATE", datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"))
# TRANSACTION_URL = f'{base_url}accounts/{checking_id}/transactions'

# sig = os.environ.get("NARMI_SIG", "OOPS")
# signature = f'keyId="{TOKEN}",algorithm="hmac-sha256",headers="date",signature="{sig}"'

# headers = {
#     "Authorization": f"Bearer {TOKEN}",
#     "Date": date,
#     "Signature": signature
# }
# print(headers)

# response = requests.get(TRANSACTION_URL, headers=headers)

# Open sample json transaction data
file = open('test.txt', 'r')
parsed_response = file.read()
file.close()

print("-------------------")
# print("RESPONSE:", type(response))
# print(response.status_code)
print(parsed_response)

