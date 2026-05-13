# lower()
def greeting():
    return "Welcome to CBC!"

myname = "Sadeed"
myname = input("Enter your name: ")

def newgreeting():
    return f"{myname}, Welcome to learning Python"


def newgreeting2():
    return f"{myname}, {greeting()}" 


print(newgreeting())
print(newgreeting2())

