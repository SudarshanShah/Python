try:
    a = int(input("Enter your number : "))
    print(a+5)
except Exception as e:
    print("Some error occured", e)    