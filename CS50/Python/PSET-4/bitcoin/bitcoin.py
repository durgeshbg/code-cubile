import requests
import sys

if len(sys.argv) != 2:
    sys.exit('Missing command-line argument ')

try:
    n = int(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')
