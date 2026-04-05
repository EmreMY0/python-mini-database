# python-mini-database
Mini SQL python



---

# Simple SQL-Like Table Manager

Bu proje, Python kullanarak temel SQL komutlarını (CREATE, INSERT, SELECT, UPDATE, DELETE, JOIN, COUNT) taklit eden, dosya tabanlı bir tablo yönetim sistemidir. Bir giriş dosyasındaki komutları okur ve sonuçları formatlı bir şekilde ekrana basar.

## Özellikler

* **Dinamik Tablo Oluşturma:** Verilen sütun isimlerine göre yeni tablolar tanımlayabilir.
* **Veri İşlemleri:** Tablolara veri ekleme, güncelleme ve silme desteği sunar.
* **Koşullu Sorgular:** Belirli kriterlere göre veri seçme ve sayma işlemlerini yapar.
* **Tablo Birleştirme (Join):** İki farklı tabloyu ortak bir sütun üzerinden birleştirerek gösterir.
* **Görsel Çıktı:** Tabloları ASCII karakterleri kullanarak düzgün bir kutu yapısında ekrana yazdırır.

## Kullanım

Programı çalıştırmak için komut satırından giriş dosyasını parametre olarak vermeniz yeterlidir:

```bash
python main.py input.txt
```

## Veri Yapısı

Projenin merkezinde, tablo isimlerini anahtar (key) olarak kullanan bir sözlük (`data`) yapısı bulunur. Tablo sütunları ve satırları bu sözlük içinde iç içe geçmiş listeler ve sözlükler şeklinde tutulur. `table_printer` fonksiyonu, bu veriyi otomatik olarak sütun genişliklerini hesaplayarak ekrana basar.

## Desteklenen Komut Formatları

* `CREATE_TABLE [Tablo_Adı] [Sütun1,Sütun2,...]`
* `INSERT [Tablo_Adı] [Değer1,Değer2,...]`
* `SELECT [Tablo_Adı] [Sütunlar/*] WHERE {Koşullar}`
* `UPDATE [Tablo_Adı] {Yeni_Değerler} WHERE {Koşullar}`
* `DELETE [Tablo_Adı] WHERE {Koşullar}`
* `JOIN [Tablo1,Tablo2] WHERE [Ortak_Sütun]`
* `COUNT [Tablo_Adı] WHERE {Koşullar}`

---
