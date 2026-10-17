try:
    with open("matn.txt", "r", encoding="utf-8") as f:
        matn = f.read()
    
    sozlar = matn.split()
    print(f"So'zlar soni: {len(sozlar)}")
except FileNotFoundError:
    print("Fayl topilmadi: matn.txt")