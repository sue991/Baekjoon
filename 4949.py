while True:
    n = input()
    if n == ".":
        break

    stack = []
    num = 0

    for x in n:
        if x == "(" or x == "[":
            stack.append(x)

        elif x == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                num = 1
                break

        elif x == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                num = 1
                break

    if len(stack) == 0 and num == 0:
        print("yes")
    else:
        print("no")

