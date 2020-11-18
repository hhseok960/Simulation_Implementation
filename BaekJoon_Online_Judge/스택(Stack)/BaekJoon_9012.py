def valid_PS(string):
    det = 0
    for i in range(len(string)):
        if string[i] == "(":
            det += 1
        elif string[i] == ")":
            det -= 1
        if det < 0:
            print("NO")
            return
    if det == 0:
        print("YES")
    else:
        print("NO")


T = int(input())
for i in range(T):
    parenthesis_string = input()
    valid_PS(parenthesis_string)