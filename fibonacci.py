num=18

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence 
print(fibonacci_sequence(num))