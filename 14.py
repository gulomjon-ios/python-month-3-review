import json

talaba = {
    "ism": "Ali",
    "yosh": 18,
    "ball": 90
}

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(talaba, f, ensure_ascii=False)

with open("student.json", "r", encoding="utf-8") as f:
    malumot = json.load(f)

print(f"Ism: {malumot['ism']}")
print(f"Yosh: {malumot['yosh']}")
print(f"Ball: {malumot['ball']}")