# # Round-Up Saver Application
# ## The purpose of this application is to help the user save money incrementally, by rounding up the transactions they perform on a daily basis to the nearest dollar, and depositing those extra few pennies into their savings account. 

import os
import datetime
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# Static Call Variables:

token = os.environ.get("token")
secret = os.environ.get("secret")
signature_imported = os.environ.get("sig")
base_url='https://api.demo.narmitech.com/v1/'

date=datetime.datetime.utcnow().replace(microsecond=0).isoformat()
date=f'{date}Z'
url='https://api.guasfcu.com/v1/accounts/'

signature_written=os.popen(f'echo -n "date: {date}" | openssl dgst -sha256 -binary -hmac "{secret}" | base64').read()
curl_comm=f"""curl -H "Authorization: Bearer {token}" -H "Date: {date}" -H "Signature: keyId=\\\"{token}\\\",algorithm=\\\"hmac-sha256\\\",headers=\\\"date\\\",signature=\\\"{signature_written}\\\"" {url}"""

response=os.popen(curl_comm).read()
print(response)
# Python scripts that don't really work: 

# signature_conc=f'keyId="{token}",algorithm="hmac-sha256",headers="date",signature="{signature_written}"'
# headers = {
#     'Authorization':f'Bearer {token}',
#     'Date':date,
#     'Signature':signature_conc,
# }

# print(signature_written)
# print(headers)
# response = requests.get('https://api.demo.narmitech.com/v1/accounts/', headers=headers)
# response = requests.get('https://api.demo.narmitech.com/v1/accounts/', headers=headers)