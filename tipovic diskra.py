def simetr(n, list):
    sim = 0
    anti_sim = 0
    if n == 0:
        return ("невозможно определить симметричность")
    for i in range(n):
        a = list[i][0]
        b = list[i][1]
        if [b, a] in list :
            sim += 2
        else:
            anti_sim += 2
        if sim != 0 and anti_sim != 0:
            return("не симметричный")

    if sim == 0:
        return("антисимметричный")
    else:
        return("симметричный")

def reflect(n, m, list):
    ref = 0
    if m == 0:
        return ("невозможно определить рефлективность")
    for i in range(n):
        a = list[i][0]
        b = list[i][1]
        if a == b:
            ref += 1
    if ref == m:
        return ("рефлективный")
    elif ref == 0:
        return ("aнтирефлективный")
    else:
        return ("не рефлективный")

def tranzit(m,  list):
    tranz = 0
    anti_tranz = 0
    possible = False
    for i in range(0, m+1):
        for j in range(0, m+1):
            if i == j:
                continue
            for k in range(0, m+1):
                if k == i or k == j:
                    continue
                if [i, j] in list and [j, k] in list:
                    possible = True
                    if [i, k] in list :
                        tranz += 1
                    else:
                        anti_tranz += 1
                    if tranz!= 0 and anti_tranz != 0:
                        return ("не транзитивный")
    if possible == False:
        return ("невозможно определить транзитивность")
    if tranz == 0:
        return ("антитранзитивный")
    else:
        return ("транзитивный")


n, m = map(int, input("Ведите количество ребер и вершин графа: ").split())
list = []
for i in range (n):
    a, b = map(int, input().split())
    list.append([a,b])


list.sort()
print(reflect(n, m, list))
print(simetr(n, list))
print(tranzit(m, list))
