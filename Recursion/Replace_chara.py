def ReplaceChar(s,a,b):
    l = len(s)
    if l == 0:
        return s

    SmallerString = ReplaceChar(s[1:],a,b)
    if s[0] == a:
        return b + SmallerString
    else:
        return s[0] + SmallerString

print(ReplaceChar("dacdxcd","c","x"))

# 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
