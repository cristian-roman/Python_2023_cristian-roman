import stack as s
import queue as q


def run_stack_example():
    print("Stack example")

    stack = s.Stack()

    stack.push(1)
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())

    stack.push(2)
    print(stack.peek())
    print(stack.peek())

    stack.push(3)
    stack.push(4)
    print(stack.peek())

    print()


def run_queue_example():
    print("Queue example")

    queue = q.Queue()

    queue.push(1)
    print(queue.pop())
    print(queue.pop())
    print(queue.peek())

    queue.push(2)
    print(queue.peek())
    print(queue.peek())

    queue.push(3)
    queue.push(4)
    print(queue.peek())

    print()


if __name__ == "__main__":
    run_stack_example()
    run_queue_example()
