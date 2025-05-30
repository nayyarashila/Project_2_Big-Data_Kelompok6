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
[Road Accident (United Kingdom (UK)) Dataset
](https://www.kaggle.com/datasets/devansodariya/road-accident-united-kingdom-uk-dataset) 

**Deskripsi**

Pemerintah Inggris mengumpulkan data kecelakaan lalu lintas dari tahun 2000 hingga 2018, mencatat lebih dari 1,8 juta kecelakaan. Ini menjadikan dataset ini salah satu yang paling komprehensif terkait kecelakaan lalu lintas, memberikan gambaran besar tentang perubahan yang terjadi di negara tersebut selama hampir dua dekade.

**Isi Dataset**

Dataset ini terdiri dari 1 file CSV utama yang berisi data kecelakaan. Setiap kecelakaan direferensikan dengan Accident_Index yang bisa digunakan untuk menghubungkan data korban dan kendaraan (jika tersedia di tabel terpisah). Namun, dalam set ini hanya tersedia data utama kecelakaan.

**Deskripsi Fitur**

Dataset ini memiliki 33 fitur (kolom) dan lebih dari 1,8 juta baris data. Beberapa fitur utama yang tersedia antara lain:
`Longitude / Latitude: Lokasi kecelakaan`

`Accident_Severity: Tingkat keparahan kecelakaan (skala 1 sampai 5)`

`Number_of_Vehicles: Jumlah kendaraan yang terlibat`

`Number_of_Casualties: Jumlah korban dalam kecelakaan`

`Light_Conditions: Kondisi pencahayaan saat kecelakaan`

`Weather_Conditions: Kondisi cuaca saat kecelakaan`

`Road_Surface_Conditions: Kondisi permukaan jalan di lokasi kecelakaan`

`Year: Tahun terjadinya kecelakaan`

### Struktur File
```
bigdata-project-2/
├── api/
│   └── app.py                  # REST API (Flask/FastAPI), load & serve model
│
├── batch_data/                
│   └── ...
│
├── consumer/
│   └── kafka_consumer.py      # Listen dari Kafka dan bisa simpan ke file / call training
│
├── models/                    # Directory untuk simpan model hasil training
│   └── model_1.pkl
│   └── model_2.pkl
│   └── ...
│
├── producer/
│   └── kafka_producer.py      # Streaming data ke Kafka
│
├── spark/
│   └── spark_training.py      # Training model Spark dari data stream / file
│
├── UK_Accident.csv            # Dataset
├── requirements.txt           # Python dependencies
├── Docker-compose.yml         # Docker compose untuk Zookeeper, Kafka, Spark
├── README.md

```

run `producer.py`

![image](https://github.com/user-attachments/assets/4199e8b6-5cb7-4f76-9cf0-b35eaf8e4f87)



run `customer.py`



