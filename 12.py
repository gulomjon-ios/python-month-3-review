sonlar = list(map(int, input().split()))

juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
kvadrati = list(map(lambda x: x ** 2, juft_sonlar))

print(f"Juft sonlar: {juft_sonlar}")
print(f"Kvadratlari: {kvadrati}")