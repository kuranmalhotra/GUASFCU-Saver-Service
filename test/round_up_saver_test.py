### The purpose of this testing application is to continuously test the functionality of the round up saver. 

from apps.round_up_saver import tare_cents
from apps.round_up_saver import round_up

def test_tare_cents():
	result = tare_cents(-2332)
	assert result == 32

def test_round_up():
	result = round_up(32)
	assert result == 68