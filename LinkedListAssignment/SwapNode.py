class Node():

     def __init__(self,data):
         self.data = data
         self.next = None

def printLL(head):

    while head is not None:
        print(str(head.data) + "->",end="")
        head = head.next
    print(None)
    return

def swapNode(head,i,j):

    ptr1 = head
    ptr2 = head

    ctn1 = 0
    ctn2 = 0

    while ctn1 < i:
        ctn1 += 1
        ptr1 = ptr1.next

    while ctn2 < j:
        ctn2 += 1
        ptr2 = ptr2.next

    curr1 = ptr1
    curr2 = ptr2

    data1 = curr1.data
    data2 = curr2.data

    curr1.data = data2
    curr2.data = data1

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
head = swapNode(head,2,5)
printLL(head)
