T = int(input())
for _ in range(T):
    sen1, sen2 = input().split()
    sen1_c = sen1
    if len(sen1) != len(sen2):
        print(sen1,"&",sen2,"are NOT anagrams.")
        continue
    for x in sen2:
        if x in sen1_c:
            sen1_c = sen1_c.replace(x,"",1)
    if not sen1_c:
        print(sen1,"&",sen2,"are anagrams.")
    else:
        print(sen1,"&",sen2,"are NOT anagrams.")