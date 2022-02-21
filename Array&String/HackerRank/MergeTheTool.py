'''input
s = 'AABCAAADA'
k = 3
output
AB
CA
AD'''

def merge_the_tool(string,k):
    l = []
    m = 0
    for i in range(len(string)//k):
        l.append(string[m:m+k])
        m += k
    # print(l)
    for j in l:
        # print(list(j)) # NOTE: converts the into list['A','A','B']
        # print(dict.fromkeys(list(j))) # NOTE: Makes a dictionary with value None {'A': None, 'B': None}
        # print(dict.fromkeys(list(j),1)) # NOTE: {'A': 1, 'B': 1}
        # print(list(dict.fromkeys(list(j)).keys())) # NOTE: ['A', 'B']
        print("".join(list(dict.fromkeys(list(j)).keys())))# NOTE: ['A', 'B']




s = 'AABCAAADA'
merge_the_tool(s,3)
