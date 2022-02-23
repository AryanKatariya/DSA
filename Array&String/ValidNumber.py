'''For example,
all the following are valid numbers:["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
"3e+7", "+6e-1", "53.5e93", "-123.456e789"],
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].'''

 def isNumber(s):
        digit,dec,e,symbol = False,False,False,False

        for c in s:
            if c in "0123456789":
                digit = True

            elif c in "+-":
                if symbol or digit or dec:
                    return False
                else:
                    symbol =True
            elif c in "Ee":
                if not digit or e:
                    return False
                else:
                    e = True
                    symbol = False
                    digit = False
                    dec = False
            elif c==".":
                if dec or e:
                    return False
                else:
                    dec = True
            else:
                return False

        return digit
