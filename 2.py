sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]

juft =0
toq =0
for son in sonlar:
    if int(son) % 2 == 0:
        juft+=1
    else:
        toq +=1
    

print(f"Juft sonlar: {juft}")
print(f"toq sonlar {toq}")