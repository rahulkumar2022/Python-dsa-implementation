stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushing 1, 2, 3:", stack)

# Peek
top_element = stack[-1] if stack else None
print("Top element after pushing:", top_element)


# Pop
popped_element = stack.pop() if stack else None
print("Popped element:", popped_element)
print("Stack after popping:", stack)


# isEmpty
is_empty = len(stack) == 0
print("Is stack empty?", is_empty)

is_empty = not bool(stack)
print("Is stack empty using bool?", is_empty)

#size
stack_size = len(stack)
print("Size of stack:", stack_size)


