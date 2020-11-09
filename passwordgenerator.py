#Dev by Groznek

import random
import pyperclip

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []

length = input("Bienvenue, Entre le nombre de caractère que tu veux dans ton mot de passe ! (default 128)\n")
length = 128 if length is '' else int(length)

#random ascii 

while count < length:
    rand = random.randint (0,3)
    if rand == 0:
        lower += 1
        b = int(random.randint (97,123))
        password.append(b)
    elif rand == 1:
        upper += 1
        b = random.randint (65,91)
        password.append(b)
    elif rand == 2:
        number += 1
        b = random.randint (48,58)
        password.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            b = random.randint (33,48)
            password.append(b)
        elif r == 1:
            b = random.randint (91,97)
            password.append(b)
        elif r == 2:
            b = random.randint (123,126)
            password.append(b)
    count += 1

#convert ascii code to characters
word = "".join([chr(c) for c in password])

#copy pass to clipboard
pyperclip.copy(word)

#print the result
print("Votre mot de passe random %s est: \n" % length)

print('******')
print(word)
print('******')

print("\nIl contient",lower,"minuscules,",upper,"majuscules,",number,"nombres et",symbol,"Charactère symbole")
input('Mot de passe copier !, Appuies sur un bouton pour quitter ...')