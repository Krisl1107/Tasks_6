s = int(input())

numbers = []
for h in range (0, 10):
    numbers.append (h)

for a in range (10, 100):
    numbers.append (a // 10)
    numbers.append (a % 10)

for x in range (100, 201):
    numbers.append ((x // 10) // 10)
    numbers.append ((x // 10) % 10)
    numbers.append (x % 10)

k = numbers[s-1]

print(k)
