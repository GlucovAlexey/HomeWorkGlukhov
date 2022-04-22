from math import sqrt
n = int(input())
for x in range(1, n + 1):
    if all(x % i != 0 for i in range(2, int(sqrt(x)) + 1)):
        print(x, end=" ")
