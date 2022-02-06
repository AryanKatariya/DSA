class Node:
    def __init__(self):
        self.data = 0
        self.next = None

def sortedIntersect(a, b):
    dummy = Node()
    tail = dummy;
    dummy.next = None;

    while (a != None and b != None):
        if (a.data == b.data):
            tail.next = push((tail.next), a.data);
            tail = tail.next;
            a = a.next;
            b = b.next;

        elif(a.data < b.data):
            a = a.next;
        else:
            b = b.next;
    return (dummy.next);

def push(head_ref, new_data):

    new_node = Node()

    new_node.data = new_data;

    new_node.next = (head_ref);

    (head_ref) = new_node;
    return head_ref

def printList(node):
    while (node != None):
        print(node.data, end=' ')
        node = node.next;

if __name__=='__main__':

    a = None;
    b = None;
    intersect = None;


    a = push(a, 6);
    a = push(a, 5);
    a = push(a, 4);
    a = push(a, 3);
    a = push(a, 2);
    a = push(a, 1);
    printList(a)

    b = push(b, 8);
    b = push(b, 6);
    b = push(b, 4);
    b = push(b, 2);
    printList(b)

    intersect = sortedIntersect(a, b);

    print("Linked list containing common items of a & b ");
    printList(intersect)
