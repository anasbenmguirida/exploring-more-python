#in python (same a java / c# ) everything is an object than inherit from the base class object



""" x= "hello world" 
print(type(x)) # type kay3ti dima <class type>

y = 10 
print(type(y))

z= 1 + 1j 
print("possible complexe data type")
print(type(z))
print("imaginaire " , z.imag ) """


""" import random 

random_number = random.randrange(0 , 6)

x = input("enter un nombre entre 0 et 6 : ") # str type khsni n convertih l int bach anani n8d ncpmpareh 
x= int(x)
if x < 0 or x>6 :
    print("rentrez un autre nombre")
else:
    if x ==random_number :
        print("rbe7ti")
    else:
        print("khsrtiii , r9m kan howa " , random_number)"""


#string manipulation 
#string sont immutables , si on veut les modifier on doit les convertir en listes ! 
"""immutable_string = "testing" 
immutable_string[len(immutable_string)]=" 2" #string object CANT be changed ama l variable peut pointer sur un autre string object
print("my immutable test on strings  : " , immutable_string)"""

my_string = "hello world" 
print("string in py are similar to arrays => sequence! ")
print("char at index 2  : "  , my_string[2])

# slicing 
print("***********slicing ***********")
print("apres l'index 3 : " , my_string[3:])

upper_string = my_string.upper() 
print(upper_string)

