print("Stack is a LIFO data structure")
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)



print(stack)


print('Remove and return the first item in the stack')
popVal = stack.pop()
print(popVal)
print(stack)

print('Get the first item in the stack without removing it')
peekVal = stack[-1]
print(peekVal)

print("Get the length of the stack")
print(len(stack))


print("Queue is a FIFO data structure")
import queue

q = queue.Queue()

print("Add items to the queue")
q.put(1)
q.put(2)
q.put(3)
q.put(4)

print("Remove and return the first elements from the queue")
value = q.get()
print(value)

print("Get the first item in the queue without removing it")
value = q.queue[0]
print(value)

print("GET THE LENGTH OF THE QUEUE")
n = q.qsize()
print(n)

print("Chekc if the queue is empty")
if q.empty():
    print("queue is empty")
else:
    print("queue is not empty")
