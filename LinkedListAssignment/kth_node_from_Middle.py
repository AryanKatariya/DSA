'''Input :  List is 1->2->3->4->5->6->7
         K= 2
Output : 2

Input :  list is 7->8->9->10->11->12
         K = 3
Output : 7'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    if not head:
        return Node(data)

    new_node = Node(data)

    new_node.next = head

    head = new_node

    return head

def getCount(head):
    count = 0
    current = head
    while (current ):
        count = count + 1
        current = current.next

    return count

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
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def Kthfrommid(head, k):

    n = getCount(head)

    reqNode = int((n / 2 + 1) - k)

    if (reqNode <= 0) :
        return -1

    else :
        current = head
        count = 1
        while (current) :
            if (count == reqNode):
                return (current.data)
            count = count + 1
            current = current.next

head = takeInput("1 2 3 4 5 6 -1")
print(Kthfrommid(head,2))
