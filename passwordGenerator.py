#Simple Password generator

import random

chars = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!£$%&/()=?^'

length = int(input("Lunghezza della password --> "))
quante = int(input("Quante password generare --> "))

for i in range(quante):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
  
