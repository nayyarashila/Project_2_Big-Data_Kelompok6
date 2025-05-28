# Project_2_Big-Data_Kelompok6

| Nama          | NRP          |
| ------------- | ------------ |
| Revalina Fairuzy Azhari Putri | 5027231001 |
| Farida Qurrotu A'yuna | 5027231015 |
| Nayyara Ashila | 5027231083 |

## Project 2 Kafka
![image](https://github.com/user-attachments/assets/f01de3ae-362a-49fb-ba31-0f5072b2d84d)

Terdapat sebuah sistem Big Data dengan arsitektur seperti gambar di atas. Sistem tersebut berfungsi untuk menyimulasikan pemrosesan data stream menggunakan Kafka dan Apache Spark.

## Dataset
Dataset yang kami gunakan terdapat pada link dibawah ini:
[Synthetic Financial Datasets For Fraud Detection 
](https://www.kaggle.com/datasets/ealaxi/paysim1) 

Dataset tersebut membahas tentang PaySim yang mensimulasikan transaksi uang seluler berdasarkan sampel transaksi yang diambil dari catatan keuangan selama satu bulan dari layanan uang seluler yang diterapkan di negara Afrika. Catatan asli disediakan oleh perusahaan multinasional, yang merupakan penyedia layanan keuangan seluler yang saat ini beroperasi di lebih dari 14 negara di seluruh dunia.
Dengan deskripsi sebagai berikut:
- Jumlah record: 6,3 juta (dapat di-sampling menjadi 1,5–3 juta)
- Ukuran: ~200 MB
- Fitur: `amount`, `oldbalanceOrg`, `newbalanceOrig`, `isFraud`, `type` 

### Struktur File
```
tugas-klp-kafka/
│
├── docker-compose.yml
├── Dockerfile
├── app/
│   ├── producer.py
│   ├── consumer.py
│   ├── train_model.py
│   └── api.py
├── batch/         # Hasil dari consumer
├── models/        # Hasil model dari Spark
├── dataset/
│   └── PS_20174392719_1491204439457_log.csv
```

run `producer.py`

![image](https://github.com/user-attachments/assets/237ef27a-0ab5-449a-ac94-491c24435a4b)

![image](https://github.com/user-attachments/assets/278b0f71-055a-4f32-a232-a0dbb695914e)


run `customer.py`

![image](https://github.com/user-attachments/assets/a64be2ea-84f0-434f-80a5-ee88d2389c29)

![image](https://github.com/user-attachments/assets/c96e3339-c4d3-4c9f-b8f4-d9d9821440f1)

![image](https://github.com/user-attachments/assets/f311bb07-17c4-4a9a-884d-c58e460f5d25)


