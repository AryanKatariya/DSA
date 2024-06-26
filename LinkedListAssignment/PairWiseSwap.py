class Node():

     def __init__(self,data):
         self.data = data
         self.next = None

def printLL(head):

    while head is not None:
        print(str(head.data) + "->",end="")
        head = head.next
    print("None")
    return

def swapNode(head):

    temp = head

    if temp is None:
        return

    while temp and temp.next:
        if temp.data != temp.next.data:
            temp.data , temp.next.data = temp.next.data , temp.data

        temp = temp.next.next

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
head = swapNode(head)
printLL(head)
