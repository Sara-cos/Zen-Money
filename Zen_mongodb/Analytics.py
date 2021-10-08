import requests
from json.decoder import JSONDecodeError

Base = "http://127.0.0.1:5000/"

try:
	response = requests.get(Base + "total_asset")
	print(response.json())
except JSONDecodeError as e:
	print("Decoding Json has failed")