CONTRIBUTORS = ["Rachid Rahme" , 'Juliano Jawad Gharzeddine' , "Steven EL HAYEK" ,]
git add calculator.py

def add(a, b):
    return a+b 


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a * b



def divide(a, b):
    return a / b


if __name__ == "__main__":
    print(f"Welcome to the Group Calculator, written by {CONTRIBUTORS}")
    print(f"2 + 2 = {add(2, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")