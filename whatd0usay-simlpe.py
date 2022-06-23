from web3 import Web3
from time import sleep
import requests


provider = 'https://smartbch.fountainhead.cash/mainnet'
my_contract = '0x35b2dA94A08980DB5FBA6D9a980761e72e5Eb80b'


abi_file = 'messySpeaker-v2.2-abi.json'
with open(abi_file, 'r') as f:
	my_abi = f.read()




w3 = Web3(Web3.HTTPProvider(provider))
contract = w3.eth.contract(address=my_contract, abi=my_abi)

fn = "last_words_on_chain.txt"

if w3.isConnected():
	print('	Connect to Provider Successful')
	#last = contract.functions.what_do_you_say().call()
	with open(fn, 'r', encoding='utf-8') as f:
		last = f.read()
	while True:
		try:
			now = contract.functions.what_do_you_say().call()
			print(now)
			if last != now:
				speakOutLoud(now)
				last = now
			with open(fn, 'w', encoding='utf-8') as f:
				f.write(now)
			sleep(5)
		except:
			sleep(10)
			continue

		

















