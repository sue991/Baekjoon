apb = [0]*26
for x in input():
    apb[ord(x)-97] += 1
print(*apb)