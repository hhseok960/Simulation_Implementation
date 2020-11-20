N = int(input())

i = N
while i > 0:
    for j in range(N - i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    i -= 1
    print(end="\n")

i = 2
while i <= N:
    for j in range(N - i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    i += 1
    print(end="\n")