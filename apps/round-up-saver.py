# # Round-Up Saver Application
# ## The purpose of this application is to help the user save money incrementally, by rounding up the transactions they perform on a daily basis to the nearest dollar, and depositing those extra few pennies into their savings account. 

# Import necessary packages

import os
from datetime import datetime
import json
import requests
from dotenv import load_dotenv

# Function definition

def tare_cents(my_dollar_value): # <-- remove the dollar value, and keep the cents
	cent_value = int(str(my_dollar_value)[-2:])
	return(cent_value)

def round_up(my_amount): # <-- round up the cent value to the nearest dollar
	round_val = 100-my_amount
	return(round_val)

# Static Call Variables:

load_dotenv()

TOKEN = os.environ.get("TOKEN")
secret = os.environ.get("SECRET")

checking_id = os.environ.get("FROM_ACCT_ID")
checking_bal_id = f'abl_{checking_id}'
savings_id = os.environ.get("TO_ACCT_ID")
savings_bal_id = f'abl_{savings_id}'

signature_imported = os.environ.get("sig")
base_url = os.environ.get("baseurl")
line = "-"*50

date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

sig = os.environ.get("NARMI_SIG", "OOPS")
signature = f'keyId="{TOKEN}",algorithm="hmac-sha256",headers="date",signature="{sig}"'

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Date": date,
    "Signature": signature
}

# Gather last transaction ID

with open('last_tranID.txt') as file:
	last_transaction = file.read()

TRANSACTION_URL = f'{base_url}accounts/{checking_id}/transactions?before={last_transaction}'

total_savings = 0
tranIDs = []

# Open sample json transaction data

with open('test.txt') as json_file:
	data=json.load(json_file)
	
# run transactions off json file

	for p in data['transactions']:
		if p['source'] == "card":
			tranIDs.append(p["id"])
			cents = tare_cents(p['amount'])			
			if (cents) != 0:
				rounded_val = round_up(cents)
			else: rounded_val = 0

			total_savings = total_savings + rounded_val
			
			print(rounded_val)
			print('-----')

last_ID = tranIDs[0]

# Save last transaction ID to text file

with open('last_tranID.txt', 'w') as f:
	f.write(last_ID)

# Initialilze the transfer post request

transfer_url = f"{base_url}transfers/"

# # Create payload to post total savings

# payload ={
# 	"from_account_id": f"{checking_id}",
# 	"to_account_id": f"{savings_id}",
# 	"amount": total_savings
# }

# post_response = requests.post(transfer_url, headers=headers, json=payload)

# print(post_response)
# print(post_response.text)



