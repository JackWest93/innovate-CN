greet="welcome to code nation"

print(len(greet))

evenodd=(len(greet))

if evenodd%2==0:
    print("even")
else:
    print("odd")

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

for letter in alphabet:
    print(letter)

userno=int(input("Please enter a number between 1 and 26: "))-1

print(alphabet[userno])

def add_up():
    num1=input("number 1: ")
    num2=input("number 2: ")

    try:
        print(f"{num1}+{num2} is {(int(num1))+(int(num2))}")
    except:
        print("please print two numbers.")

add_up()