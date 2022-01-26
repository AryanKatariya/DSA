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
            tail = newNode # NOTE: for first element head and tail are same.
        else:
            tail.next = newNode # NOTE: node1 next will became address of newNode i.e. node2
            tail = newNode
    return head

head = takeInput("1 2 3 4 5 6 -1")
printLL(head)
