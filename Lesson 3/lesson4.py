names = ["rijaN","leke"]
for i in names:
    print(i)



sentence = "rijani"

for character in sentence:
    if character.isalpha():
        print(character)



for number in range(1,6):
   print(number)

numbers = [12,45,6,72,21,8,94,57]

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    print("the maximum valuw in the list is ", maximum)


count = 1
while count <= 5:
    print("iteration", count)
    count +=1

while True:
    user_input = input("enter a positive number: ")
    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break

        print("invalid input please try again")

        print("You have entered a positive number: ", number)


################################################

    numberlist = [1,2,3,4,5,6,7]
    target = 4
    for number in numberlist:
        print(number)
        if number == target:
            print("target found")
            break

