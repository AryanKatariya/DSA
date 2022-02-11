def solve(A):
        A = A.strip()
        A = A.split(" ")
        output = []
        for i in A[::-1]:
            output.append(i)
        return " ".join(output)

a="Aryan Katariya"
b=solve(a)
print(b)
