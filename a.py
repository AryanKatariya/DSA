#     # str = "I love \India"
# # print(str.split("\"))
# nums = [1,1,1,3,3,4,3,2,4,2]
# # a= list(enumerate(nums))
# prevMap = {}
# for i,n in enumerate(nums):
#     print(i,n)
# n = int(input())
# integer_list = map(int, input().split())
# print(list[integer_list])
s = 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'
def swap_case(s):
    for i in s:
        if i.isupper() is False:
            i.upper()
        else:
            i.lower()

    return s
print(swap_case(s))

for i in s:
    print(i.isupper())
