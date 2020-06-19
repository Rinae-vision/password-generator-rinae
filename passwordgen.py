#python password gen
import random
import string
count = 0
password = ""
length = int(input("How many characters would you like in your code?"))

while count != length:
    upper  = [random.choice("string.ascii_uppercase")]
    lower  = [random.choice("string.ascii_lowrcase")]
    num    = [random.choices("string.digits")]
    symbol = [random.choices("string.punctuation")]
    everything = upper + lower + num + symbol
    password += random.choice("everything")
    count += 1
    continue
    if count == length:
        print("password")
    