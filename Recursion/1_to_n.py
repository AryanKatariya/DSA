def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)

def reverse_print1ton(n):
    if n == 0:
        return
    print(n)
    reverse_print1ton(n-1)


p = int(input("Enter a natural number:"))
reverse_print1ton(p)
print_1_to_n(p)
