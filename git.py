import random

lower = "abcdefghijklmnopqurstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "[ ]{ }# @ ( ) / ? * ;,: % . _ - " " "

all=lower + upper +NUMBER + Symbol
lenght = 9
password = "" .join (random.sample(all, lenght))
print("You were Generate The password :", password)

 