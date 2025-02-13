def red(s):
    stack = []
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    r = ''
    for char in stack:
        r += char

    return r

i1 = "aabccd"
r1 = red(i1)
print(f"Input: '{i1}' -> Output: '{r1}'")

i2 = "aabbccd"
r2 = red(i2)
print(f"Input: '{i2}' -> Output: '{r2}'")