'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
IV            4
IX            9
XL            40
XC            90
CD            400
CM            900'''

def intToRoman(num):
    symList = [['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],
    ['L',50],['XC',90],['C',100],
    ['CD',400],['D',500],['CM',900],['M',1000]]

    res = ""
    for sym,val in reversed(symList):
        if num // val:
            count = num//val
            res += (sym * count)
            num = num % val
    return res

a = 44
print(intToRoman(a))
