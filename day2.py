light = False
def light_switch():
    global light
    if light:
        print("whoa it's bright in here!")
        light=False
    else:
        print("Who turned the lights out?")
        light=True

light_switch()
light_switch()

str = input("Enter the string: ")
i = len(str)
x = i-1
y = 0
while y < x:
    if str[y] == str[x]:
        index = y + 1
        x = x-1
        print("\nString is a palindrome\n")
        break
    else:
        print("\nString is not a palindrome\n")
        break

def number():
    num=input("\nPlease enter a number: ")
    num=int(num)
    if num % 1 == 0:
        print("Integer!")
    else:
        ("Try again!")
        number()

ghosts=("")