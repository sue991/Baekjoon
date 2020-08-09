n = list(input())
for x in n:
    if x in "ABC":
        print(chr(ord(x)+23),end="")
    else:
        print(chr(ord(x)-3),end="")