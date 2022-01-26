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

def insertAtIR(head,i,data): # NOTE: order of i
    if i < 0:
        return head

    if i==0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    if head is None:
        return newNode


    smallerHead = insertAtIR(head.next,i-1,data)
    head.next = smallerHead
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
head = insertAtIR(head,2,6)
printLL(head)
head = insertAtIR(head,0,9)
printLL(head)
