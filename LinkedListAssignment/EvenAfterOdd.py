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

def deleteElement(head,key):
        temp = head

        if temp is not None:
            if temp.data == key:
                head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return

        prev.next = temp.next

        temp = None

        return head

def arrange_LinkedList(head):

    if head is None:
        return head
    curr = head

    head1 = None
    head2 = None

    while curr is not None:
        if curr.data &1:
            if head1 is None:
                head1 = curr
                tail1 = curr
            else:
                tail1.next = curr
                tail1 = tail1.next
        else:
            if head2 is None:
                head2 = curr
                tail2 = curr
            else:
                tail2.next = curr
                tail2 = tail2.next

        curr = curr.next

    if head1 is None or head2 is None:
        return head

    tail2.next = None
    tail1.next = head2

    return head1

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
head = arrange_LinkedList(head)
printLL(head)
