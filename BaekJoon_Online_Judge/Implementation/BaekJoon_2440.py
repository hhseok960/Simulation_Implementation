star = int(input())
for i in range(star):
    for j in range(star - i):
        print("*", end="")
    print(end='\n')
