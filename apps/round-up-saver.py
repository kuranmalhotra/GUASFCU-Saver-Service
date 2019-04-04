# # Round-Up Saver Application
# ## The purpose of this application is to help the user save money incrementally, by rounding up the transactions they perform on a daily basis to the nearest dollar, and depositing those extra few pennies into their savings account. 

import os
from datetime import datetime
import json
import requests
# from dotenv import load_dotenv
import banking_client

# load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

token_key = os.environ.get("token")
secret_key = os.environ.get("secret")
current_date = datetime.now()

header = {
	'token': token_key,
	'secret': secret_key, 
	'date': current_date
}

print(header)
