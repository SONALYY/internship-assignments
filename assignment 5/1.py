stack, min_stack = [], []

def push(val):
    stack.append(val)
    min_stack.append(val if not min_stack or val < min_stack[-1] else min_stack[-1])

def pop():
    if stack: stack.pop(), min_stack.pop()

def top():
    return stack[-1] if stack else -1

def getMin():
    return min_stack[-1] if min_stack else -1

commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
values = [[], [-2], [0], [-3], [], [], [], []]
output = ["null"]

for i in range(1, len(commands)):
    if commands[i] == "push":
        push(values[i][0])
        output.append("null")
    elif commands[i] == "pop":
        pop()
        output.append("null")
    elif commands[i] == "top":
        output.append(str(top()))
    elif commands[i] == "getMin":
        output.append(str(getMin()))

print("[" + ",".join(output) + "]")
