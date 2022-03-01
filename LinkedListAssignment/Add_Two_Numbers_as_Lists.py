'''Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
342 + 465 = 807'''

def addTwoNumbers(A, B):
		extra = 0
        a, b = A, B
        head = tmp = None
        while a or b:
            if a and b:
                no = (a.val + b.val + extra) % 10
                extra = (a.val + b.val + extra) // 10
            elif a:
                no = (a.val + extra) % 10
                extra = (a.val + extra) // 10
            else:
                no = (b.val + extra) % 10
                extra = (b.val + extra) // 10

            node = ListNode(no)
            if tmp:
                tmp.next = node
            else:
                head = node
            tmp = node
            a = a.next if a else a
            b = b.next if b else b

        if extra:
            tmp.next = ListNode(extra)

        return head
