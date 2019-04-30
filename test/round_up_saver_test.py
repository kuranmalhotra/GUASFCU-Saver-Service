### The purpose of this testing application is to continuously test the functionality of the round up saver. 
# Import necessary packages

from datetime import datetime
from dotenv import load_dotenv
import httpsig
import json
import os
import pprint
import requests
from twilio.rest import Client

from apps.round_up_saver import (
	tare_cents,
	round_up,
	create_https_header,
	TOKEN,
	SECRET,
	date,
	checking_id,
	savings_id,
	base_url,
	algorithm
	)

# Static Call Variables:

load_dotenv()

test_url = os.environ.get("baseurl")

def test_tare_cents():
	result = tare_cents(-2332)
	assert result == 32

def test_round_up():
	result = round_up(32)
	assert result == 68

def test_base_url():
	assert base_url == test_url

def test_algorithm():
	assert algorithm == 'hmac-sha256'

def test_create_https_header():
	result = create_https_header()
	algorithm = 'hmac-sha256'
	signed_headers = ['date']
	hs = httpsig.HeaderSigner(TOKEN, SECRET, algorithm=algorithm, headers=signed_headers)
	hs.signature_template = 'keyId="{}",algorithm="{}",signature="%s",headers="{}"'.format(TOKEN, algorithm, ' '.join(signed_headers))
	signature = hs.sign({'Date': date,})

	header_params_test = {}
	header_params_test['Authorization'] = 'Bearer {}'.format(TOKEN)
	header_params_test['Signature'] = signature['authorization']
	header_params_test['Date'] = date
	assert result == header_params_test

def test_last_tranID_file():
	last_tranID_filepath = 'storage/last_tranID.txt'
	assert os.path.isfile(last_tranID_filepath) == True

def test_api_link():
	test_url = f'{base_url}/ping'
	result = requests.get(test_url)
	result_string = str(result)
	assert result_string == '<Response [200]>'
