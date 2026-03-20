### ім'я і все інше
import random
print("Hi, goy. Tell me your name first - ")
name = input()
print("well, now say how old are you - ")
age = int(input())
print("okay, you are ", name, age)
if int(age) < 18:
    print("stay away, goy. you are to young")

### гра з числами 
rnd = random.randint(1, 10)
print("then lets play a game...enter any number you want 1-10 and  I will say, is it correct one - ")
chislo = int(input())

while chislo != rnd:
    if chislo > rnd:
        print("it is too big maan, choose another - ")
    elif chislo < rnd:
        print("it is too small bro, choose another - ")
    chislo = int(input())
    
print("YEEEEH IT IS THE CORRECT ONE")

### виведення числе

print("goy...choose now any number - ")
chislo = int(input())
print("now choose other, BIGER one - ")
chislo1 = int(input())
print("here is your range - ")
for i in range(chislo, chislo1):
    print(i)

### парні числа

print("валяй будь яке число що можна поділити на 2.")
a = int(input())
for i in range(a, 1, -2):
    print(i)


###  факторіал

import math
print("валяй будь яке число, я порахую його факторіал")
a = int(input())
f = math.factorial(a)
print(f)


### підрахунок балллллів

print("well, goy, now tell me your last grade(from 1 to 100) - ")
gr = int(input())
if gr < 50:
    print("dumb goy...")
elif 50 < gr < 70:
    print("normal for usual goy")
elif 70 < gr < 90:
    print("hm, it is better then I thought")
elif 90 < gr < 100:
    print("wou! best goy!")

### калькулятор

print("yeh, goy, say me any number")
a = int(input())
print("nice, say me any other number")
b = int(input())
print("and what do you whant to do with that numbers? +, -, * or / ?")
do = str(input())
if do == "+":
    rs = a + b
    print("result", rs)
elif do == "-":
    rs = a - b
    print("result", rs)
elif do == "*":
    rs = a * b
    print("result", rs)
elif do == "/":
    if b == 0:
        print("you cant do that")
        rs = None
    rs = a / b
    print("result", rs) 