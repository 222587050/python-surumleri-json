import json

dosya_adi ='surumler.json'

with open(dosya_adi, 'r', encoding='utf-8') as dosya :
    veriler=json.load(dosya)

print("------yeni surum-------")
girilen_versiyon=input("eklenecek versiyonu yaziniz:")
girilen_durum=input("Versiyon  durumu:")

yeni_surum={"versiyon":girilen_versiyon, "durum":girilen_durum}

veriler["python_surumleri"].append(yeni_surum)

with open(dosya_adi, 'w', encoding='utf-8') as dosya:
    json.dump(veriler, dosya, ensure_ascii=False, indent=4)

print(f"{girilen_versiyon} kaydedildi")