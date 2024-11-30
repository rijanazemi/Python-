total = 0

for number in range(1,11):
    if number % 2 == 0:
        total += number
        print("shuma e numrave qift prej 1 deri ne 10 eshte:", total)

def greet():
    print("hello world!")

greet()

def greet_person(name):
    print("hello", name)
greet_person("Filan")

#result = add(3,8)
#print("3+7 =", result)

greeting = "hello"
def greet(name):
    message = f"{greeting}, {name}!"
    print(message)
greet("michael")
print(greeting)

def greet_person(name, greeting="hello"):
    message = f"{greeting}, {name}!"
    return message
defaul_greeting = greet_person("Rijan")
custom_greeting = greet_person("eris", "hi")
print(defaul_greeting)
print(custom_greeting)