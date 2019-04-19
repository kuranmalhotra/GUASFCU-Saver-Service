# # Round-Up Saver Application
# ## The purpose of this application is to help the user save money incrementally, by rounding up the transactions they perform on a daily basis to the nearest dollar, and depositing those extra few pennies into their savings account. 

# Import necessary packages


from datetime import datetime
from dotenv import load_dotenv
import json
import os
import pprint
import requests
from twilio.rest import Client

# Function definition

def tare_cents(my_dollar_value): # <-- remove the dollar value, and keep the cents
	cent_value = int(str(my_dollar_value)[-2:])
	return(cent_value)

def round_up(my_amount): # <-- round up the cent value to the nearest dollar
	round_val = 100-my_amount
	return(round_val)

# Static Call Variables:

load_dotenv()

TOKEN = os.environ.get("token")
secret = os.environ.get("secret")

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

with open('storage/last_tranID.txt') as file:
	last_transaction = file.read()

TRANSACTION_URL = f'{base_url}/accounts/{checking_id}/transactions?before={last_transaction}'

# tran_response = requests.get(TRANSACTION_URL, headers=headers)

# print(tran_response)


total_savings = 0
total_spend = 0
tranIDs = []

# Open sample json transaction data

with open('test.txt') as json_file:
	data=json.load(json_file)

# run transactions off json file

	for p in data['transactions']:
		if p['source'] == "card":
			tranIDs.append(p["id"])
			total_spend = total_spend + p['amount']
			cents = tare_cents(p['amount'])			
			if (cents) != 0:
				rounded_val = round_up(cents)
			else: rounded_val = 0

			total_savings = total_savings + rounded_val
			
			print(rounded_val)
			print('-----')

last_ID = tranIDs[0]

total_spend_usd = "{0:.2f}".format(-(total_spend/100))
total_spend_formatted = str(f'${total_spend_usd}')

total_savings_usd = "{0:.2f}".format(total_savings/100)
total_savings_formatted = str(f'${total_savings_usd}')

# Save last transaction ID to text file

with open('storage/last_tranID.txt', 'w') as f:
	f.write(last_ID)

# Initialilze the transfer post request

TRANSFER_URL = f"/{base_url}transfers/"

# # Create payload to post total savings

# payload ={
# 	"from_account_id": f"{checking_id}",
# 	"to_account_id": f"{savings_id}",
# 	"amount": total_savings
# }

# post_response = requests.post(TRANSFER_URL, headers=headers, json=payload)

# print(post_response)
# print(post_response.text)


# Send text update

# Initialize environment variables:
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

# AUTHENTICATE

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)

content = f"This is a message from GUASFCU. You spent {total_spend_formatted} and saved {total_savings_formatted}!"

# ISSUE REQUEST (SEND SMS)

message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)

# PARSE RESPONSE

pp = pprint.PrettyPrinter(indent=4)

print("----------------------")
print("SMS")
print("----------------------")
print("RESPONSE: ", type(message))
print("FROM:", message.from_)
print("TO:", message.to)
print("BODY:", message.body)
print("PROPERTIES:")
pp.pprint(dict(message._properties))

