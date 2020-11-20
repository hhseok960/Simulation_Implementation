import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
qu = deque([])

for i in range(N):
    command = input().split()
    if command[0] == 'push':
        qu.append(command[1])
    elif command[0] == 'pop':
        if not qu:
            print(-1)
        else:
            print(qu.popleft())
    elif command[0] == 'size':
        print(len(qu))
    elif command[0] == 'empty':
        if not qu:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not qu:
            print(-1)
        else:
            print(qu[0])
    elif command[0] == 'back':
        if not qu:
            print(-1)
        else:
            print(qu[-1])