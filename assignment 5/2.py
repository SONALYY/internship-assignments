def reverseList(head):
    prev, curr = None, head
    while curr:
        next_node = curr[1]
        curr[1] = prev
        prev = curr
        curr = next_node
    return prev

def printList(head):
    while head:
        print(head[0], end=" -> ")
        head = head[1]
    print("None")

head = [1, [2, [3, [4, [5, None]]]]]

print("Original List:")
printList(head)

head = reverseList(head)

print("Reversed List:")
printList(head)
