'''Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
NOTE: String A is haystack, B is needle.'''

def strStrIB(A, B):
        if B == "" or A == "":
            return -1

        for i in range(len(A)+1-len(B)):
            for j in range(len(B)):
                if A[i+j] != B[j]:
                    break
                if j == len(B) - 1:
                    return i
        return -1

def strStr(self, haystack: str, needle: str):
        if needle == "":
            return 0

        for i in range(len(haystack)+1-len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
