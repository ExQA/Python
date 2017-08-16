import requests
import json

URL = 'stage.api.agendoapp.com/v1/auth/register'
payload = {
    'Email': 'python@gmail.com',
    'Firstname': 'Firstname',
    'LanguageCulture': 'ru_UA',
    'Password': 'qwertyui',
    'Surname': 'Surname'
}
#session = requests.session()
r = requests.post(URL, data=payload)
r.headers ['Content-Type']:'application/x-www-form-urlencoded; charset=utf-8'
print (r.content)

