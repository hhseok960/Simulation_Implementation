import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.idx = -1
        self.stack = []

    def push(self, num):
        self.stack.append(num)
        self.idx += 1

    def pop(self):
        if self.idx == -1:
            print(-1)
            # return -1
        else:
            num = self.stack.pop()
            self.idx -= 1
            print(num)
            # return num

    def size(self):
        print(self.idx + 1)
        # return self.idx + 1

    def empty(self):
        if self.idx == -1:
            print(1)
            # return 0
        else:
            print(0)
            # return 1

    def top(self):
        if self.idx == -1:
            print(-1)
            # return -1
        else:
            top_num = self.stack[self.idx]
            print(top_num)
            # return top_num


N = int(input())

st = Stack()

for i in range(N):
    command = input().split()
    if command[0] == "push":
        st.push(int(command[1]))
    elif command[0] == "pop":
        st.pop()
    elif command[0] == "size":
        st.size()
    elif command[0] == "empty":
        st.empty()
    elif command[0] == "top":
        st.top()
