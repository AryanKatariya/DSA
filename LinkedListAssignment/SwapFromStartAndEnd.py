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

def countNodes(head):

    cnt = 0
    while head is not None:
        cnt += 1
        head = head.next
    return cnt

def Kth(head,k):
    n = countNodes(head)

    if n < k:
        return

    if (2*k-1) == n:
        return

    i = head
    i_prev = Node(None)
    for x in range(k-1):
        i_prev = i
        i = i.next

    j = head
    j_prev = Node(None)
    for x in range(n-k):
        j_prev = j
        j = j.next

    if i_prev is not None:
        i_prev.next = j

    if j_prev is not None:
        j_prev.next = i

    temp = i.next
    i.next = j.next
    j.next = temp

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
head = Kth(head,2)
printLL(head)
