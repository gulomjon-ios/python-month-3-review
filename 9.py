matn = input().split()

sozlar = {}

for s in matn:
    s = s.lower()
    if s in sozlar:
        sozlar[s] += 1
    else:
        sozlar[s] = 1

for k, v in sozlar.items():
    print(f"{k}: {v}")