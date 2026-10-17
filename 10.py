oquvchlar = ["ali", "vali", "sardor", "malika"]
balar = [15, 8, 12, 5]

eng_kop = max(balar)

print(f"Eng yaxshi o'quvchi: {oquvchlar[balar.index(eng_kop)]}-{eng_kop}")
print(f"O'rtacha ball - {sum(balar) / len(balar)}")