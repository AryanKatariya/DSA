'''Example 1:
Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:
Input: s = "", t = "y"
Output: "y"'''

from collections import Counter

def findTheDifference(s, t):
        return list((collections.Counter(t) - collections.Counter(s)))[0]
