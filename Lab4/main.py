import stack as s
import queue as q
import matrixUtils as mu


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


def run_matrix_example():
    a = mu.Matrix(2, 3)
    b = mu.Matrix(3, 2)

    a.set_element(0, 0, 1)
    a.set_element(0, 1, 2)
    a.set_element(0, 2, 3)
    a.set_element(1, 0, 4)
    a.set_element(1, 1, 5)
    a.set_element(1, 2, 6)

    b.set_element(0, 0, 1)
    b.set_element(0, 1, 2)
    b.set_element(1, 0, 3)
    b.set_element(1, 1, 4)
    b.set_element(2, 0, 5)
    b.set_element(2, 1, 6)

    print("Matrix example")
    print(a)
    print()
    print(b)

    print()

    print("Matrix multiplication example")
    print(mu.multiply_matrices(a, b))

    print()
    print("Matrix iterated with transformation example")
    print(a.iterate_with_transformation(lambda x: x + 1))


if __name__ == "__main__":
    run_stack_example()
    run_queue_example()
    run_matrix_example()
