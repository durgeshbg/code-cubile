import requests
import sys

if len(sys.argv) != 2:
    sys.exit('Missing command-line argument ')

try:
    n = int(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')
try:
    res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.ConnectionError:
    sys.exit('Connection Error')
except requests.Timeout:
    sys.exit('Request Timed Out')
except requests.HTTPError:
    sys.exit('HTTP Error')
except requests.RequestException:
    sys.exit('Ambiguous Error')

response = res.json()
price = response['bpi']['USD']['rate_float'] * n
print(f'${price:,.4f}')