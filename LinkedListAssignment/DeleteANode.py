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

def deleteItr(head,i):
    if i < 0 and i > length(head):
        return head
    if i == 0:
        head = head.next
    else:
        curr = head
        for j in range(0,1):
            curr = curr.next
        end = curr.next.next
        curr.next.next = None
        curr.next = end
    return head

def deleteRec(head, i):
    if i < 0:
        return head
    if i == 0 :
        return head.next
    if head == None:
        return None

    dele = deleteRec(head.next, i-1)
    head.next = dele

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
