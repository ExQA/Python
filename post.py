import requests
import json
import random

url = 'http://stage.api.agendoapp.com/'
headers = {'Client-Platform': 'IOS', 'Client-Version': '1.1.4'}
aut = 'v1/auth/register'

random_number = random.randrange(256, 1999, 1)

email = "py%s@gmail.com" % random_number

data = {
    'Email': email,
    'Firstname': 'Firstname',
    'LanguageCulture': 'ru_UA',
    'Password': 'qwertyui',
    'Surname': 'Surname'
       }
r = requests.post(url + aut, headers=headers, data=data)

if r.status_code == 200:
    print("ok")
    token = r.json()["ResultList"][0]["Token"]
    print(token)
else:
    print("LOOoooooSER")


parsed = json.loads(r.content)
print(json.dumps(parsed, indent=4, sort_keys=True))
# print(r.status_code)
#

#'user-agent': 'Agendo/1.1.4 (com.alf.agendo; build:7; iOS 10.2.0) Alamofire/4.4.0',

