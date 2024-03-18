# Chaos.py
# Random Chaos function exercises.

def main():
    n = eval(input("How many numbers should I print? "))
    x = eval(input("Pick a number between 0 and 1: "))
    y = eval(input("Pick another number between 0 and 1: "))
    print(x , y)
    print("-----------------")
    for i in range (n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * x * (1 - x)
        print(x , y)
