# why not print python code in blocks but not in an entire file


# due to maximize the code effeciency by writing in a code and reducing error load on an entire code file



onik = 12;
print(onik)

# variables

a = 5;
b = 10;
c = 15;
d = 20;
e = 25;
sum = a+b+c+d+e;
print(sum);

a = int(input("enter the num :"))
b = int(input("enter the num :"))
c = int(input("enter the num :"))
print(a+b+c)

print(1000000*999999919280)

a = input()
b = input()
sum = a+b
print(sum)

a = 2
b = 3
a = a+b
b = a-b
a = a-b
print(a,b)



for x in range(50):
  if(x%2==0):
    print("even no.",x)
  elif(x%2!=0):
    print("odd no.",x)


x = int(input())

if(x>0):
  print("pos")
elif(x==0):
  print("zero")
else:
  print("neg")

x = input()
if(x == "mon"):
  print("monday")
elif(x == "tue"):
  print("tuesday")
elif(x == "wed"):
  print("wednesday")
elif(x == "thur"):
  print("thursday")
elif(x == "fri"):
  print("friday")
elif(x == "sat"):
  print("saturday")
elif(x == "sun"):
  print("sunday")

for x in range(1,50,2):
  print(x)
 


x = int(input())
while x<10:
  print(x)
  x+=1


x = 7/2
y = 7//2
print(x)
print(y)
z = x*y
a = y**2
print(z)
print(a)



# questions in python

z = input()
is_palin = True
i = z[0]
j = z[len(z)-1]
while(i<j):
  if(i!=j):
    is_palin = False
    break
  i+=1
  j-=1

if(i==j):
  print(is_palin)