def fibonacciSequence(count):
    fibonacci = []
    if count > 0:
        previous = 0
        current = 1
        while len(fibonacci) < count:
            curr = previous+current
            fibonacci.append(curr)
            previous = current
            current = curr
    return fibonacci
