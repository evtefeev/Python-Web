import requests
import pprint

res = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
).json()


pprint.pprint(res)