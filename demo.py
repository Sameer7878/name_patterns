d={'s':[[1, 2, 3, 4, 5], [1], [1], [1, 2, 3, 4, 5], [5], [5], [1, 2, 3, 4, 5]],
        'a':[[1, 2, 3, 4], [1, 4], [1, 4], [1, 2, 3, 4], [1, 4], [1, 4],[1,4]],
        'm':[[1, 2, 8, 9], [1, 3, 7, 9], [1, 4, 6, 9], [1, 5, 9], [1, 9],[1, 9],[1, 9]]
   }

def aiol(s='sam'):
    res=[]
    for i in s:
        res.append(d[i])
    for i in range(1,len(s)):
        m=sorted(res[0])[-1][-1]
        res[0]=[j+[x+m for x in y] for y,j in zip(res[i],res[0])]
    print(res[0])

aiol()