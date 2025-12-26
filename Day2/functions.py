# all about functions

def greet():
    return 'hi there','how are you?'

# print(greet())

for g in greet():
    print(g)

def testp(*params):
    for i in params:
        print(i)

testp(1, 2, 3)




def show():
    return "Hello Python","Hello JAVA"

print(show())

def hello(greeting="Hello",name="World"):
    print('%s,%s'%(greeting,name))

hello()

def hello1(greeting,name):
    print('%s,%s'%(greeting,name))
hello1(name="PYTHON",greeting="Hi")


def params(*params):
    print(params)
params("Testing")
params(20,30,40)

def namedparam(**params):
    print(params)
namedparam(x=1,y=2,z=3)


def params_1(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)

params_1(30,40,60,70,80,f=1,g=2)


x=10
def test():
    x=100
    print(globals()['x'])

test()


class Student:
    def show(self):
        print("Original Function")
def new_show(self):
    print("modified using the monkey patching")

s=Student()
s.show()
Student.show=new_show
s.show()



