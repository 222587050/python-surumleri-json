import json

dosya_adi ='surumler.json'

with open(dosya_adi, 'r', encoding='utf-8') as dosya :
    veriler=json.load(dosya)

yeni_surum={"versiyon":"3.14", "durum":"geliştirme asamasinda"}

veriler["python_surumleri"].append(yeni_surum)

with open(dosya_adi, 'w', encoding='utf-8') as dosya :
    json.dump(veriler, dosya, ensure_ascii=False, indent=4 )


print("Yeni sürüm (3.14) JSON dosyasına başarıyla kaydedildi.")