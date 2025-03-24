k = int(input())
numbers = []
for c in range (0, 10):
    numbers.append (c)
for b in range (10, 100):
    numbers.append (b // 10)
    numbers.append (b % 10)
for a in range (100, 201):
    numbers.append ((a // 10) // 10)
    numbers.append ((a // 10) % 10)
    numbers.append (a % 10)
t = numbers[k-1]
print(t)
