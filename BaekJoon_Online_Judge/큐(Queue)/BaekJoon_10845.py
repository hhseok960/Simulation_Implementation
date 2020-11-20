import sys
input = sys.stdin.readline


class Queue:
    def __init__(self):
        self.idx = -1
        self.queue = []

    def push(self, x):
        self.queue.append(x)
        self.idx += 1

    def pop(self):
        if self.idx == -1:
            print(-1)
        else:
            front = self.queue.pop(0)
            self.idx -= 1
            print(front)

    def size(self):
        print(self.idx + 1)

    def empty(self):
        if self.idx == -1:
            print(1)
        else:
            print(0)

    def front(self):
        if self.idx == -1:
            print(-1)
        else:
            print(self.queue[0])

    def back(self):
        if self.idx == -1:
            print(-1)
        else:
            print(self.queue[self.idx])


N = int(input())
qu = Queue()

for i in range(N):
    command = input().split()
    if command[0] == "push":
        qu.push(int(command[1]))
    elif command[0] == "pop":
        qu.pop()
    elif command[0] == "size":
        qu.size()
    elif command[0] == "empty":
        qu.empty()
    elif command[0] == "front":
        qu.front()
    elif command[0] == "back":
        qu.back()