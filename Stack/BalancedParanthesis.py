import queue


def isBalanced(string):
    stack = []


    for char in string:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True


s = queue.LifoQueue()

def isBalanced(str):

    for i in str:
        if i in "{([":
            s.put(i)

        elif i == '}':
            if (s.empty() or s.queue[-1] != '{'):
                return False
            s.get()

        elif i == ')':
            if (s.empty() or s.queue[-1] != '('):
                return False
            s.get()

        elif i == ']':
            if (s.empty() or s.queue[-1] != '['):
                return False
            s.get()


    if s.empty():
        return True
    return False

def isBalanced(string):

    s = []
    for char in string:
        if char in '({[':
            s.append(char)
        elif char == ')':
            if not s or s[-1] != '(':
                return False
            s.pop()
        elif char == ']':
            if not s or s[-1] != '[':
                return False
            s.pop()
        elif char == '}':
            if not s or s[-1] != '{':
                return False
            s.pop()

    if (not s):
        return True
    return False

string = input()
ans = isBalanced(string)
print(ans)
