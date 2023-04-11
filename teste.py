grafo = [['c', 0], ['b', 1]]

for p, v in enumerate(grafo):
    print(v)
    if type(v) == list:
        for q, u in enumerate(v):
            if q == 0:
                print(u)
            # print(var[0])
    else:
        if p == 0:
            print(v)