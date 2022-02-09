def capitalize(s):
    for i in s.split():
        s = s.Replace(i,i.capitalize())
    return s
