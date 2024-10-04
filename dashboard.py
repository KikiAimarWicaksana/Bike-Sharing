# Import Libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Dashboard Analisis Penyewaan Sepeda", layout="wide")

# Judul
st.title("Dashboard Analisis Penyewaan Sepeda")

# Sidebar untuk Mengunggah File
st.sidebar.title("Unggah Dataset Anda")
day_data_file = st.sidebar.file_uploader("Unggah Data Harian", type=["csv"])
hour_data_file = st.sidebar.file_uploader("Unggah Data Jam", type=["csv"])

# Load Data
@st.cache_data
def load_data(file):
    if file is not None:
        data = pd.read_csv(file)
        return data
    return None

day_data = load_data(day_data_file)
hour_data = load_data(hour_data_file)

# Jika data tersedia, tampilkan analisis
if day_data is not None and hour_data is not None:

    # Menampilkan ringkasan data
    st.subheader("Tampilan Dataset")
    st.write("Data Harian")
    st.dataframe(day_data.head())

    st.write("Data Jam")
    st.dataframe(hour_data.head())

    # Exploratory Data Analysis (EDA)

    st.subheader("Ringkasan Statistik Data Harian")
    st.write(day_data.describe())

    st.subheader("Ringkasan Statistik Data Jam")
    st.write(hour_data.describe())

    # Konversi kolom dteday ke format tanggal
    day_data['dteday'] = pd.to_datetime(day_data['dteday'])

    # Menjelaskan arti dari kolom season dan weathersit
    st.write("""
    **Arti Kode Kolom:**
    - **Season:**
      - 1: Musim Semi
      - 2: Musim Panas
      - 3: Musim Gugur
      - 4: Musim Dingin

    - **Weathersit:**
      - 1: Cerah
      - 2: Berawan
      - 3: Hujan Ringan
      - 4: Hujan Berat
    """)

    # Analisis 1: Penyewaan Sepeda berdasarkan Musim dan Tahun
    st.subheader("1. Penyewaan Sepeda berdasarkan Musim dan Tahun")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=day_data, x="dteday", y="cnt", hue="season", ax=ax)
    ax.set_title("Tren Penyewaan Sepeda berdasarkan Musim dan Tahun")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Total Penyewaan")
    st.pyplot(fig)

    st.write("""
    **Insight:** Grafik ini menunjukkan tren penyewaan sepeda berdasarkan musim sepanjang tahun. 
    Dari grafik ini, kita dapat melihat bahwa musim panas (musim 2) dan musim semi (musim 1) 
    memiliki jumlah penyewaan yang jauh lebih tinggi dibandingkan musim dingin (musim 4). 
    Ini menunjukkan bahwa faktor cuaca sangat mempengaruhi jumlah penyewaan sepeda.
    """)

    # Analisis 2: Pengaruh Cuaca terhadap Penyewaan Sepeda
    st.subheader("2. Pengaruh Cuaca terhadap Penyewaan Sepeda")
    
    # Suhu vs Penyewaan
    st.write("Suhu vs Total Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=day_data, x="temp", y="cnt", hue="weathersit", ax=ax)
    ax.set_title("Penyewaan Sepeda vs Suhu (Kondisi Cuaca Disorot)")
    ax.set_xlabel("Suhu (Dinormalisasi)")
    ax.set_ylabel("Total Penyewaan")
    st.pyplot(fig)

    st.write("""
    **Insight:** Dari grafik ini, kita dapat melihat hubungan antara suhu dan jumlah penyewaan sepeda. 
    Secara umum, semakin tinggi suhu, semakin banyak penyewaan yang terjadi. 
    Kondisi cuaca juga berperan penting, dengan penyewaan yang lebih tinggi pada cuaca cerah 
    dibandingkan dengan kondisi berawan atau hujan.
    """)

    # Kelembaban vs Penyewaan
    st.write("Kelembaban vs Total Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=day_data, x="hum", y="cnt", hue="weathersit", ax=ax)
    ax.set_title("Penyewaan Sepeda vs Kelembaban (Kondisi Cuaca Disorot)")
    ax.set_xlabel("Kelembaban")
    ax.set_ylabel("Total Penyewaan")
    st.pyplot(fig)

    st.write("""
    **Insight:** Grafik ini menunjukkan bahwa kelembaban juga mempengaruhi penyewaan sepeda. 
    Terlihat bahwa ketika kelembaban meningkat, jumlah penyewaan cenderung menurun. 
    Ini mungkin menunjukkan bahwa orang lebih suka bersepeda pada hari yang kering dan nyaman.
    """)

    # Kecepatan Angin vs Penyewaan
    st.write("Kecepatan Angin vs Total Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=day_data, x="windspeed", y="cnt", hue="weathersit", ax=ax)
    ax.set_title("Penyewaan Sepeda vs Kecepatan Angin (Kondisi Cuaca Disorot)")
    ax.set_xlabel("Kecepatan Angin")
    ax.set_ylabel("Total Penyewaan")
    st.pyplot(fig)

    st.write("""
    **Insight:** Dalam grafik ini, tidak ada hubungan yang jelas antara kecepatan angin dan 
    jumlah penyewaan sepeda. Meskipun ada beberapa penyewaan pada hari berangin, 
    sepertinya faktor lain seperti suhu dan kelembaban memiliki pengaruh yang lebih besar.
    """)

    # Analisis 3: Penyewaan pada Hari Libur vs Hari Kerja
    st.subheader("3. Penyewaan Sepeda: Hari Libur vs Hari Kerja")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=day_data, x="holiday", y="cnt", ax=ax)
    ax.set_title("Penyewaan Sepeda pada Hari Libur vs Non-Hari Libur")
    ax.set_xlabel("Hari Libur (0 = Tidak, 1 = Ya)")
    ax.set_ylabel("Total Penyewaan")
    st.pyplot(fig)

    st.write("""
    **Insight:** Grafik boxplot ini menunjukkan perbandingan penyewaan sepeda pada hari libur 
    dibandingkan dengan hari kerja. Terlihat bahwa penyewaan cenderung lebih tinggi pada hari kerja, 
    mungkin karena lebih banyak orang yang menggunakan sepeda untuk pergi bekerja atau beraktivitas.
    """)

    # Analisis 4: Penyewaan Sepeda per Jam berdasarkan Musim
    st.subheader("4. Penyewaan Sepeda per Jam berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=hour_data, x="hr", y="cnt", hue="season", ax=ax)
    ax.set_title("Penyewaan Sepeda per Jam berdasarkan Musim")
    ax.set_xlabel("Jam dalam Sehari")
    ax.set_ylabel("Total Penyewaan")
    st.pyplot(fig)

    st.write("""
    **Insight:** Grafik ini menunjukkan pola penyewaan sepeda berdasarkan jam dalam sehari 
    untuk setiap musim. Terlihat bahwa penyewaan tertinggi terjadi pada pagi hari dan sore hari, 
    yang sesuai dengan jam sibuk transportasi. Musim panas menunjukkan penyewaan yang lebih tinggi 
    dibandingkan dengan musim lainnya pada jam-jam tertentu.
    """)

else:
    st.write("Silakan unggah kedua data harian dan data jam untuk memulai analisis.")
