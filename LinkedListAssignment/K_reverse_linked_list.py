'''Example :
Given 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
return 2 -> 1 -> 4 -> 3 -> 6 -> 5'''

def reverseList(A, B):
		head = last = None
        while A:
            start = A
            prev = A
            A = A.next
            for i in range(1, B):
                next = A.next
                A.next = prev
                prev = A
                A = next
            if last:
                last.next = prev
            last = start

            if not head:
                head = prev
        if last:
            last.next = None

        return head
