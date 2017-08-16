from urllib import request, parse, json
import sys

myURL = 'http://104.154.147.176:3000/api/Accounts?access_token=' + 'value'
value = {'token' : 'i7QPOaGRGNxBwxoALZFnds1gYxPkqnHd7380PWgHoPmKoMc2FhVEfxSWQFYJeYme'}

myheader = {}
myheader['User-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.3'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myURL = myURL = mydata
    req = request.request(myURL, headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)

#except Exception:
    print('ERROR!!!')
    print(sys.exc_info()[1])