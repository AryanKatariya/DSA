class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queueUsingLL:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self,data):
        newNode =Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1

    def dequeue(self):
        if self.__head is None:
            print("Queue is Empty")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data

    def front(self):
        if self.__head is None:
            print("Queue is Empty")
            return
        data = self.__head.data
        return data

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.__count

q = queueUsingLL()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.size())
print(q.isEmpty())

while q.isEmpty() is not True:
    print(q.dequeue())
print(q.front())
