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

def removeElements(head,int):
        temp = Node(None)
        temp.next = head
        node = temp

        while node.next:
            if node.next.data == int:
                node.next = node.next.next
            else:
                node = node.next

        return temp.next

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
head = removeElements(head,4)
printLL(head)
