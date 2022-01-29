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

def eliminate_duplicate(head):

    if head is None or head.next is None:
        return head

    curr = head
    adv = curr.next

    while adv is not None:
        if curr.data == adv.data:
            curr.next = adv.next
            adv = curr.next
        else:
            curr = curr.next
            adv = adv.next

    return head

def deleteDuplicates(head): # NOTE: for sorted linked list
        if not head:
            return
        prev = head
        curr = head.next
        while curr:
            if prev.data != curr.data:
                prev = curr
                curr = curr.next
            else:
                while prev.data == curr.data:
                    curr = curr.next
                    if not curr:
                        prev.next = None
                        break
                prev.next = curr
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

head = takeInput("1 2 3 4 4")
printLL(head)
hea = deleteDuplicates(head)
printLL(hea)
