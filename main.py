import datetime
import random

'''
def even(x):
  if (type(x) != int):
    print("your input is not supported")
  elif (x % 2 == 0):
    print("your input is even")
  else:
    print("your input is odd")
'''
'''
#excersise 1 p17
print("|apple|banana|blueberry|pear|strawberry|")
print(9.42 + 5.67 + 3.25 + 13.40 + (7.50)*5)
print(len("blood-oxygenation level dependent functional magnetic resonance imaging"))
print("apple " * 100)
'''
'''
#excersise 2 p21
snack1 = "corn "
snack2 = "chips "
print((snack1+snack2) * 10)
groceries = ["apple","banana","blueberry","pear","strawberry"]
print("corn" in groceries)
snack1,snack2 = snack2,snack1
print((snack1+snack2) * 10)
'''
'''
#excersise 3 p23
prices=[8.42,5.67,3.25,13.40,7.51]
print(min(prices),max(prices))
help(random.randint)
randsnack = random.randint(1,10)
print("corn " * randsnack)
price = random.choice(prices)
print(round(price))
'''
'''
#excersise 4 p25
spacer = " "
def snacks(x, num):
  x=str(x)
  print((x + spacer) * num)
groceries = ["apple","banana","blueberry","pear","strawberry"]
def inlist(x):
  print(x in groceries)
def randchoice():
  print(random.choice(groceries))
'''
'''
#excersise 5 p26
def snacks(x, spacer = ", ", num=100):
  x=str(x)
  print((x + spacer) * num)
'''
'''
#excersise 6 p27
my_color=input("what is your color? ")
other_color=input("what is another color? ")
my_num=input("what is your number? ")
my_num=int(my_num)
print(2+my_num)
print("your color is: " + other_color + " the other color is: " + my_color)
'''
'''
#excersise 7 p32
num = random.randint(0,5)
print(num > 2)
fruit = ["apple","pear","mango"]
print(random.choice(fruit) == "apple")
'''
'''
#excersise 8 p33
fruit = ["apple","pear","mango"]
def fruitcheck(x):
  if(x in fruit):
    print("your fruit is in the list")
  elif(type(x) != str):
    print("your input needs to be a string")
  else:
    print("your fruit is not in the list")
'''
'''
#excersise 9 p35
snack="apple"
snacknum=0
while(snacknum<=10):
  print(snack)
  snacknum+=1
else:
  snacknum=0
while (snacknum<=10):
  print(snack * snacknum)
  snacknum+=1
else:
  snacknum=0
'''
'''
#excersise 10 p38
x=1
for i in[1,2,3,4,5,"x","y","z"]:
  print(i, type(i))
for i in["blood oxygenation level functional magnetic resonance imaging"]:
  print(i)
for i in["apple","corn","tomato","cucumber","lemon"]:
  print(x, i)
  x+=1
  if (i=="cucumber"):
    break
for i in str.split("blueberry pie brownie cupcake"):
  print(i)
'''
#excersise 11 p50
x = 0
a = [1,2,2,3,4,5,5,5]
final = []
for i in range(100):
    if(i%3==0 or i%5==0):
        x = x+i
        print(i)
a = [1,2,2,3,4,5,5,5]
final = []
dupes = []
def duplicates(x):
    print(x)
    y=set()
    for i in x:
        if i not in y:
            final.append(i)
            y.add(i)
        else:
            dupes.append(i)
    print(final)
    print(dupes)
duplicates(a)
