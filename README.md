# Bike Sharing Dashboard

Dashboard ini digunakan untuk menganalisis data peminjaman sepeda berbasis cuaca, musim, dan faktor lainnya. Dengan visualisasi dan analisis yang interaktif, pengguna dapat memahami tren peminjaman sepeda sepanjang tahun dan pengaruh berbagai faktor cuaca terhadap penggunaan sepeda.

## Fitur Utama
- Visualisasi tren peminjaman sepeda berdasarkan musim dan kondisi cuaca.
- Perbandingan jumlah peminjaman pada hari libur dan hari kerja.
- Analisis pengaruh suhu, kelembaban, dan kecepatan angin terhadap peminjaman sepeda.

## Prasyarat

Sebelum memulai, pastikan Anda telah menginstal Python 3.9 atau lebih baru.

### Setup Environment - Anaconda (Opsional)
1. Buat dan aktifkan environment dengan Anaconda:
   ```bash
   conda create --name bike-sharing python=3.9
   conda activate bike-sharing
2. Instal dependansi
   ```bash
   pip install -r requirements.txt

### Setup Environment - Shell/Terminal
1. Buat direktori baru
   ```bash
    mkdir proyek_bike_sharing
    cd proyek_bike_sharing
2. Inisialisasi environment dengan Pipenv
   ```bash
   pipenv install
   pipenv shell
3. Instal requirements.txt
   ```bash
   pip install -r requirements.txt
### Menajalankan dashboard
```bash
streamlit run dashboard.py atau python -m streamlit run dashboard.py


   
