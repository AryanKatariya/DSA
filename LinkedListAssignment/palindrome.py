class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    lst = []
    while head is not None:
        lst.append(head.data)
        head = head.next
    return lst

def reverseLL(head):
    lst = []
    while head is not None:
        lst.insert(0,head.data)
        head = head.next
    return lst

def check_palindrome(head):

    if printLL(head) == reverseLL(head):
        return True
    else:
        return False

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

head = takeInput("1 2 3 2 1")
print(check_palindrome(head))
