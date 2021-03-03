from timeit import timeit


func = """
arr = []
for i in range(1000):
    if(i%3):
        arr.append(i)
"""

time = timeit(func, number=10000)
print(f"{'standard':>14} {time}")


func = """
arr = [i for i in range(1000) if i%3]
"""

time = timeit(func, number=10000)
print(f"{'comprehension':>14} {time}")
