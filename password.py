import random

PassLenght = int(input("Enter the lenght of the password: "))
Chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/*!@#$%^&()<>"
Password = "".join (random.sample(Chars,Passlenght))
print("This is you random password: \n"p)
