# print("hello world")

'''
# demo 1
x = input ("enter your age : ")
x = int (x)

if x > 18 :
    print("you are old enough to deal with it")
else :
    print("grow up")

'''


'''
# demo 2

name = 'Dr.Doom'
day = 1
time = 10.11

print(type(name), type(day), type(time))

'''

'''
# demo 3

x=1000
y=200
print("Addition:",x+y)
print("Subtraction:",x-y)
print("Addition:",x*y)
print("Multiplication:",x/y)
print("Division:",x/y)
print("Modulus:",x%y)
print("Exponent:",x**y)
print("Floor Division:",x//y)

'''


'''


# demo 4 strings
s = "hello world!"
print(s[-1])
print(s[-2])
print(s[1:3])
print(s[-3:])








s="This is beautiful day"
t="python"

print(s[-3])
print(s[0:4])
print(s[2:])
print(s[:2])
print(s[::-1])
print(s+t)
print(s*3)
print(len(s))
print("p" not in "python")
print(s.upper())
print(s.strip())
print(s.replace("beautiful","good"))

name="ravi"
age=25

print(f"My name is {name} and age is {age}")

print("my name is {} and age is {}".format(name,age))

print(name.isdigit())

'''


x = 10
def show():
    global x
    x=100
    print("the value of x inside the fuction:", x)


show()
print("the value of x is:", x)