# ind-preprocessing

Teks processing untuk machine learning bahasa Indonesia.

## Deskripsi

`ind-preprocessing` adalah tool untuk mengolah teks agar dapat dibaca oleh mesin. Library ini menyediakan beberapa metode untuk membersihkan teks, tokenisasi, menghapus kata-kata umum (stopwords), lematization (lematisasi), dan padding token untuk pemrosesan teks dalam bahasa Indonesia. Tool ini belum sempurna karena dictionary belum di tambahkan dan baru beberapa ratus saja. Kode ini bersifat open source dan dapat kalian edit dan modifikasi sesuka kalian.

## Instalasi

Clone repository ini:

```bash
git clone https://github.com/superevilstockholm/ind-preprocessing
```

Untuk menggunakan tool ini, Anda perlu menginstal `pandas` jika belum terpasang. Anda dapat menginstal `pandas` dengan menjalankan:

```bash
pip install pandas
```

## Contoh penggunaan
```python
from text_processing import PreProcessing
processor = PreProcessing()
result = processor.process_text("Ini adalah contoh teks untuk diolah", max_length=10)
print(result)
```

## Struktur file
```
your_python_project/
│
├── data/
│   ├── dict_lematization.csv
│   └── ind_stopwords.txt
│
├── text_processing.py
└── your_code.py
```
