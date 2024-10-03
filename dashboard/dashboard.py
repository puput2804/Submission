import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Mengatur layout dashboard dengan sidebar
st.set_page_config(page_title="Dashboard Analisis Data", layout="wide")

# Sidebar untuk navigasi
st.sidebar.title("Menu Navigasi")
st.sidebar.markdown("Submission Proyek Analisis Data:")

# Informasi pengguna di sidebar
st.sidebar.markdown("**Informasi Pengguna**")
st.sidebar.write("Nama: **Putri Bungsu Ratna Sari**")
st.sidebar.write("Email: **M193B4KX3518@bangkit.academy**")
st.sidebar.write("ID Dicoding: **M193B4KX3518**")

# Header judul dashboard
st.title('E-Commerce_Public_Dataset')
st.markdown("---")

# Bagian deskripsi atau pengantar dengan card-style
with st.container():
    st.markdown("""
    <div style="background-color:#2F4F4F;padding:10px;border-radius:5px;">
    <h3 style='text-align: center;'>Selamat datang di Dashboard Proyek Analisis Data</h3>
    <p style='text-align: center;'>Dashboard ini menampilkan analisis data pesanan berdasarkan tahun dan kategori produk</p>
    </div>
    """, unsafe_allow_html=True)

# 1. Membaca Data
st.subheader("Pertanyaan 1 : Apa pola jumlah pesanan berdasarkan tahun?")
st.markdown("---")

# Mendapatkan path direktori kerja saat ini
dir_path = os.path.dirname(os.path.abspath(__file__))

# Tentukan path relatif ke direktori dataset
base_path = os.path.join(dir_path, '..', 'data', 'E-Commerce Public Dataset')

# Memeriksa apakah file ada
orders_path = os.path.join(base_path, 'orders_dataset.csv')
if not os.path.exists(orders_path):
    st.error(f"File tidak ditemukan di path: {orders_path}")
else:
    # Membaca dataset
    orders = pd.read_csv(orders_path)
    order_items = pd.read_csv(os.path.join(base_path, 'order_items_dataset.csv'))

    # Mengonversi kolom waktu dan menambahkan kolom tahun
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['order_purchase_year'] = orders['order_purchase_timestamp'].dt.year.astype(int)

    # Menggabungkan dataset order_items dengan orders
    order_data = pd.merge(order_items, orders[['order_id', 'order_purchase_year']], on='order_id')

    # Menghitung jumlah pesanan berdasarkan tahun
    order_counts = order_data.groupby('order_purchase_year')['order_item_id'].count().reset_index()

    # 4. Menampilkan Visualisasi Tren Pesanan Berdasarkan Tahun
    st.subheader("Tren Pesanan Berdasarkan Tahun")

    # Menggunakan Streamlit untuk menampilkan grafik
    fig, ax = plt.subplots(figsize=(10, 6))  # Ukuran figure
    sns.barplot(x='order_purchase_year', y='order_item_id', data=order_counts, ax=ax)
    ax.set_title('Jumlah Pesanan Berdasarkan Tahun')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Jumlah Pesanan')
    st.pyplot(fig)  # Menampilkan plot di Streamlit

    # Kesimpulan untuk pertanyaan 1
    yearly_order_counts = order_data.groupby('order_purchase_year').size()
    st.info("**Kesimpulan Pertanyaan 1**: Dari visualisasi, terlihat bahwa jumlah pesanan meningkat signifikan pada tahun 2017 dan 2018. Peningkatan ini bisa dikaitkan dengan faktor-faktor tertentu, seperti peluncuran produk baru, promosi besar, atau tren musiman. Analisis lebih lanjut diperlukan untuk memahami alasan di balik tren ini.")

    # Bagian untuk kategori produk
    st.subheader("Pertanyaan 2 : Kategori produk mana yang paling banyak dipesan?")
    st.markdown("---")

    # Membaca Data
    products = pd.read_csv(os.path.join(base_path, 'products_dataset.csv'))
    product_category_translation = pd.read_csv(os.path.join(base_path, 'product_category_name_translation.csv'))

    # Menggabungkan products dan order_items untuk menganalisis pesanan kategori produk
    merged_data = pd.merge(order_items, products, on='product_id')
    merged_data = pd.merge(merged_data, product_category_translation, on='product_category_name')

    # Plot kategori produk terlaris
    top_categories = merged_data['product_category_name_english'].value_counts().head(10)

    # Menampilkan grafik di Streamlit
    st.subheader('Top 10 Kategori Produk yang Dipesan')
    fig, ax = plt.subplots(figsize=(10, 6))  # Ukuran figure
    top_categories.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Top 10 Kategori Produk yang Dipesan', fontsize=20)
    ax.set_ylabel('Jumlah Pesanan', fontsize=15)
    ax.set_xlabel('Kategori Produk', fontsize=15)
    ax.tick_params(axis='x', rotation=45)  # Memutar label sumbu x agar lebih mudah dibaca
    st.pyplot(fig)  # Menampilkan plot di Streamlit

    # Kesimpulan untuk pertanyaan 2
    st.info("**Kesimpulan Pertanyaan 2**: Produk yang paling banyak dipesan adalah kategori 'bed_bath_table', diikuti oleh 'health_beauty' dan 'sports_leisure'. Ini menunjukkan tren preferensi pelanggan yang mengarah pada produk rumah tangga dan kesehatan.")
