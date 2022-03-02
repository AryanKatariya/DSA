def len(A):
        cnt, tmp = 0, A
        while tmp:
            cnt, tmp = cnt + 1, tmp.next
        return cnt

def removeNthFromEnd(A, B):
    n = max(0, self.len(A) - B)

    fake = ListNode(0)
    fake.next = A
    tmp = fake

    while n:
        n, tmp = n - 1, tmp.next

    tmp.next = tmp.next.next

    return fake.next
