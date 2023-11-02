import stack

if __name__ == "__main__":
    stack = stack.Stack()
    stack.push(1)
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    stack.push(2)
    print(stack.peek())
    print(stack.peek())
