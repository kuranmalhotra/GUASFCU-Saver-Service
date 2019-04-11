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
checking_id = os.environ.get("FROMACCT_ID")
checking_bal_id = f'abl_{checking_id}'
savings_id = os.environ.get("TOACCT_ID")
savings_bal_id = f'abl_{savings_id}'
signature_imported = os.environ.get("sig")
base_url = 'https://api.guasfcu.com/v1/'
line = "-"*50

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

def round_up(my_amount):
		round_val = 100-my_amount
		return(round_val)


total_savings = 0

with open('test.txt') as json_file:
	data=json.load(json_file)
	for p in data['transactions']:
		if p['source'] == "card":
			cents = int(str(p['amount'])[-2:])
			
			print(p['amount'])
			print(cents)
			
			if (cents) != 0:
				rounded_val = round_up(cents)
			else: rounded_val = 0

			total_savings = total_savings + rounded_val
			
			print(rounded_val)
			print('-----')

print(total_savings)
print(line)



