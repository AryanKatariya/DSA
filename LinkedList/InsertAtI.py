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

def length(head):

    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def insertAtI(head,i,data): # NOTE: Order of n

    if i < 0 or i > length(head):
        return head

    count = 0
    curr = head
    prev = None

    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    newNode = Node(data) # NOTE: after reaching the ith place new node is created
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr

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
head = insertAtI(head,2,6)
printLL(head)
head = insertAtI(head,0,9)
printLL(head)
head = insertAtI(head,8,10)
printLL(head)
