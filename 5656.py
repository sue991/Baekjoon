i = 1
while i:
    a, B, c = input().split()
    a, c = int(a), int(c)
    if B == "E": break
    elif B == ">" and a>c: print("Case %d: true" %i) 
    elif B == ">=" and a>=c: print("Case %d: true" %i) 
    elif B == "<" and a<c: print("Case %d: true" %i) 
    elif B == "<=" and a<=c: print("Case %d: true" %i) 
    elif B == "==" and a == c: print("Case %d: true" %i) 
    elif B == "!=" and a != c: print("Case %d: true" %i) 
    else:
        print("Case %d: false" %i) 
    i += 1