from random import * 

#In questo progetto andrò a creare un "guess the number" game :

answer = str(input("Vuoi incominciare a giocare?"))
if answer != "No" or answer != "no":
  tentativi = int(input("Digitare il numero di tentativi -->"))
  tt = int(tentativi)
  kk = 0
  print("Perfetto, digitare il range dei numeri...")
  num_min = int(input("Min --> "))
  num_max = int(input("Max --> "))
  final_num = randint(num_min,num_max)
  while not tt == -10 or tt == 0:
    if tt == 0:
      print("Hai perso! Il numero corretto era : ",final_num)
      break
    else:
      if not kk == 1:
        print("Numero generato , provare ad indovinare ")   #,final_num)
        kk = kk + 1
      else:
        answer_ttwo = int(input("Digitare --> "))
        if answer_ttwo == final_num:
          #print("Hai vinto , il numero era ",final_num, "||",tt)
          tt = -10
          print("Hai indovinato il numero : ",final_num)
          continue
        else:
          tt = tt-1
          if not tt == 0:
            print("Riprova, Tentativi rimasti : ",tt)
            continue
          else:
            continue
    
