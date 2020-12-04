from random import randrange

def generate_random(n):
    rands = []
    for i in range(0, n):
        rands.append(randrange(-100, 100))
    return rands

def sort_func(vector):
    size = len(vector)
    for i in range (size):
        for j in range(i+1, size):
            if vector[i] < vector[j]:
                pass
            else:
                n = vector[i]
                vector[i] = vector[j]
                vector[j] = n


numbers = generate_random(50)
print(f"before sorting: {numbers}")
sort_func(numbers)
print(f"after sorting: {numbers}")
