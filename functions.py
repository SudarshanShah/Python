def greetHello():
    print("Hello")

def greetHelloWithName(name):
    print("Hello ", name)    


def letterGenerator(name, date):
    str = f"Hi, my name is {name} and today's date is {date}"
    print(str) 

def average(a, b):
    return (a+b)/2    

greetHello()
greetHelloWithName("Sudarshan")
letterGenerator("Sudarshan", "June 20, 2023")
print(average(32, 68))