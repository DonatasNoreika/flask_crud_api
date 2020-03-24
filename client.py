import requests
import json


# Įrašome užduotis
# 1
# nauja_uzduotis = {
#     "pavadinimas": "Išplauti indus",
#     "atlikta": False
# }
#
# r = requests.post('http://127.0.0.1:8000/uzduotis', json=nauja_uzduotis)
# print(json.loads(r.text))

# 2
# 1
# nauja_uzduotis = {
#     "pavadinimas": "Užsakyti picą",
#     "atlikta": True
# }
#
# r = requests.post('http://127.0.0.1:8000/uzduotis', json=nauja_uzduotis)
# print(json.loads(r.text))

# Nuskaitome visas užduotis
r = requests.get('http://127.0.0.1:8000/uzduotis')
print(r.text)
# print(json.loads(r.text))