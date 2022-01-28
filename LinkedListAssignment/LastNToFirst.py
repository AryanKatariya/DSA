class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):

    while head is not None:
        print(str(head.data) + "->",end="")
        head = head.next
    print("None")
    return

def append(head,n): # NOTE: Appends Last N elements to First
    if n == 0:
        return None

    pos = length(head) - n
    curr = head
    prev = head

    for i in range(1,pos):
        curr = curr.next

    last = curr
    temp = curr.next
    head = temp

    while curr.next is not None:
        curr = curr.next
    curr.next = prev
    last.next = None

    return head


def takeInput(str):

    inputList = [int(ele) for ele in str.split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break

        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

head = takeInput("1 2 3 4 5 6 -1")
printLL(head)
head = delete(head,2)
printLL(head)
