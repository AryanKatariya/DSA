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

def intersectingNode(head1,head2):

    c1 = countNodes(head1)
    c2 = countNodes(head2)

    if c1 > c2:
        d = c1-c2
        return getIntersectingNode(d,head1,head2)
    else:
        d = c2-c1
        return getIntersectingNode(d,head1,head2)

def getIntersectingNode(d,head1,head2):
    curr1 = head1
    curr2 = head2

    for i in range(d):
        if curr1 is None:
            return -1
        curr1 = curr1.next

    while curr1 is not None and curr2 is not None:
         if curr1 is curr2:
             return curr1.data

         curr1 = curr1.next
         curr2 = curr2.next

    return -1

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


common=Node(15)

head1=Node(3)
head1.next=Node(6)
head1.next.next=Node(9)
head1.next.next.next=common
head1.next.next.next.next=Node(30)

head2=Node(10)
head2.next=common
head2.next.next=Node(30)
print(intersectingNode(head1,head2))
