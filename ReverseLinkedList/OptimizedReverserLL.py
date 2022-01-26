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

def reverse2(head):
    if head is None or head.next is None:
        return head,head


    smallhead,smalltail = reverse2(head.next)
    smalltail.next = head
    head.next = None
    return smallhead,head

def reverse3(head):
    if head is None or head.next is None:
        return head

    smallhead = reverse3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead

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
# head,tail = reverse3(head)
# printLL(head)
head = reverse3(head)
printLL(head)
