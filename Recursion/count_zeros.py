def countZeros(a):
    if a < 10:
        if a == 0:
            return 1
    else:
        return 0

    smalleroutput = countZeros(a // 10)
    if a%10 == 0:
        return smalleroutput+1

    return countZeros(a/10)

a = 1001
print(countZeros(a))

count=0
def count_digit(num):
    global count
    if (num > 0):
        if(num%10==0):
            count +=1
        count_digit(num // 10)
    return count
n=int(input("Enter a number:"))
print("The number of Zeros in the Given number is:",count_digit(n))
