import sys

MAX = 100
stack = [''] * MAX
top = -1

def push():
    global MAX
    global stack
    global  top

    if top >= MAX - 1:
        print("It's full now !")
    else:
        top += 1
        stack[top] = input("Input something : ")
    show()

def pop():
    global stack
    global top

    if top < 0:
        print("It's empty now !")
    else:
        print("%s is pop out " %stack[top])
        top -= 1
    show()

def printList():
    global stack
    global top

    i = top
    if top < 0:
        print("Nothing in stack")
    while i >= 0:
        print(stack[i])
        i = i - 1
    show()

def show():
    print("*****[ Stack ]*****")
    print("  1. Insert")
    print("  2. Delete")
    print("  3. List")
    print("  4. Exit")
    choose = int(input("Select item : "))
    {
        1: lambda: push(),
        2: lambda: pop(),
        3: lambda: printList(),
        4: lambda: sys.exit(0)
    }.get(choose, lambda : show())()

def main():
    show()

if __name__ == '__main__':
    main()
