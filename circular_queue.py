import sys

MAX = 4
front = MAX - 1
rear = MAX - 1
tag = 0
cq = [''] * MAX

def enqueue():
	global rear, front, MAX, tag, cq

	if rear == front and tag == 1:
		print("It's full now !")
	else :
		rear = (rear + 1) % MAX
		cq[rear] = input("Input something : ")
		if rear == front:
			tag = 1
	print()
	show()

def dequeue():
	global rear, front, MAX, tag, cq
	
	if rear == front and tag == 0:
		print("It's empty now !")			
	else:
		front = (front + 1) % MAX
		print("%s dequeued !" % cq[front])
		if front == rear and tag == 1:
			tag = 0
	print()
	show()

def printList():
	global rear, front, MAX, tag, cq
#	for item in cq:
		
	i = front
	stop = tag
	if i == rear and stop == 0:
		print("It's nothing here!!")
	while i != rear or stop != 0:
		i = (i + 1) % MAX
		print(cq[i])
		if i == rear:
			stop = 0
	print()	
	show()

def show():
	print("*****[ Circular Queue ]*****")
	print("  1. Insert")
	print("  2. Delete")
	print("  3. List")
	print("  4. Exit")
	choose = int(input("Select item : "))
	{
		1: lambda: enqueue(),
		2: lambda: dequeue(),
		3: lambda: printList(),
		4: lambda: sys.exit(0)
	}.get(choose, lambda : show())()
	
def main():
	show()
	
if __name__ == '__main__':
	main()
	
