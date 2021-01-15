from data_structures.linear_data_structures import Stack

new_stack = Stack()

print(new_stack.is_empty())
new_stack.push(10)
print(new_stack.peek())
new_stack.push(20)
print(new_stack.peek())
print(new_stack.pop())
print(new_stack.peek())
print(new_stack.size())
