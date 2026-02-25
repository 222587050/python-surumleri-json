import json

dosya_adi = 'surumler.json'

with open(dosya_adi, 'r', encoding='utf-8') as dosya:
  veriler = json.load(dosya)

print("python surumeri listesi")
print("-" * 25)

for surum in veriler ["python_surumleri"]:
  print(f"Versiyon : {surum['versiyon']} -> {surum['durum']}")
  
