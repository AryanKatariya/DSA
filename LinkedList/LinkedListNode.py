class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# a = Node(13)
# print(a.next)
# b = Node(15)
# a.next = b
# print(a.data)
# print(b.data)
# print(a.next.data)
# print(a)
# print(a.next) # same
# print(b) # to this
# print(b.next.data)# NOTE:None is stored in next field
def printLL(head):

    while head is not None:
        print(str(head.data) + "->",end="")
        head = head.next
    print("None")
    return

def takeInput(str):

    inputList = [int(ele) for ele in str.split()]
    head = None
    for currData in inputList:
        if currData == -1:
            break

        newNode = Node(currData) # NOTE: here only the self.data is filled and self.next remains None.
        if head is None: # NOTE:this will save the address of node 1 in head.
            head = newNode
        else:
            curr = head
            while curr.next is not None:# NOTE: To find the last node in list to link it with new node.
                curr = curr.next
            curr.next = newNode

    return head

head = takeInput("1 2 3 4 5 6 -1")
printLL(head)
