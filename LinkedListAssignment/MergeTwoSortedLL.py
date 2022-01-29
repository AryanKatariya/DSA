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

def merge(head1,head2):

    fh = Node(3)
    ft = fh
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            ft.next = head1
            ft = ft.next
            head1 = head1.next
        else:
            ft.next = head2
            ft = ft.next
            head2 = head2.next

    while head1 is not None: # NOTE: for the remaining nodes after comparison b/w head1 and head2 data
        ft.next = head1
        ft = ft.next
        head1 = head1.next

    while head2 is not None:
        ft.next = head2
        ft = ft.next
        head2 = head2.next

    return fh.next

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


head1 = takeInput("1 2 4")
printLL(head1)
head2 = takeInput("5 6 7")
printLL(head2)
head = merge(head1,head2)
printLL(head)
