sonlar = list(map(int, input().split()))

musbat = []
manfiy = []
nollar = 0

for son in sonlar:
    if son > 0:
        musbat.append(son)
    elif son < 0:
        manfiy.append(son)
    else:
        nollar += 1

print("Musbat:", musbat)
print("Manfiy:", manfiy)
print("Nollar:", nollar)