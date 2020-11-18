def balance_sentence(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[":
            stack.append(string[i])
        elif string[i] == ")":
            if len(stack) == 0 or stack[-1] != "(":
                print("no")
                return
            else:
                stack.pop()
        elif string[i] == "]":
            if len(stack) == 0 or stack[-1] != "[":
                print("no")
                return
            else:
                stack.pop()
    if len(stack) == 0:
        print("yes")
    else:
        print("no")

while True:
    sentence = input()
    if sentence == ".":
        break
    else:
        balance_sentence(sentence)