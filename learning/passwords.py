import random
from time import sleep 
letters = "yefgeyzgfezfcbezcjfiofhifhc"
digits  ="0123456789"
symbols = "#[@?!}%£$"
passwords_list = []

#generer des passwrd aleatouire d'apres les 3 sequences que jai
rdm_pass =""
for i in range(0,5):
    for j in range(0,3):
        rdm_pass=rdm_pass + random.choice(letters)
        rdm_pass = rdm_pass + random.choice(digits)
        rdm_pass = rdm_pass + random.choice(symbols)
        
    str(rdm_pass)
    passwords_list.append(rdm_pass)
    rdm_pass=""
       
#analyzing the mdps
print("analysing the passwords .........")

for password in passwords_list:
    l = 0 
    d = 0 
    s = 0
    
    for  caractere in password:
        if caractere in letters:
            l = l+1
        elif caractere in digits:
            d=d+1
        else:
            s=s+1
    print("analyzing password  : " , password)
    sleep(2)
    details = {"letters" : l , "digits" : d  , "symbols" : s }
    print(details)











