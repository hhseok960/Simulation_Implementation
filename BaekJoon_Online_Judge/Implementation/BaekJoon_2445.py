N = int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end="")
    for j in range(2*(N-i-1)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print(end="\n")

for i in range(1, N):
    for j in range(N-i):
        print("*", end="")
    for j in range(2*i):
        print(" ", end="")
    for j in range(N-i):
        print("*", end="")
    print(end="\n")