# Dashboard Analisis Data

## Deskripsi

Dashboard ini adalah proyek analisis data yang dibuat menggunakan Streamlit. Aplikasi ini menampilkan analisis data pesanan berdasarkan tahun dan kategori produk. Dengan menggunakan visualisasi interaktif, pengguna dapat memahami pola dan tren dalam data.

## Fitur

- **Menu Navigasi**: Terdapat sidebar yang menyediakan informasi pengguna dan navigasi.
- **Analisis Jumlah Pesanan Berdasarkan Tahun**: Menampilkan grafik batang yang menunjukkan pola jumlah pesanan dari tahun 2016 hingga 2018.
- **Analisis Kategori Produk**: Menampilkan grafik batang untuk kategori produk yang paling banyak dipesan.
- **Statistik Deskriptif**: Menampilkan statistik deskriptif dari dataset yang digunakan.

## Instalasi

1. Clone repositori ini ke komputer Anda:
    ```bash
    git clone https://github.com/username/repository-name.git
    cd repository-name
    ```

2. Buat lingkungan virtual:
    ```bash
    python -m venv venv
    ```

3. Aktifkan lingkungan virtual:
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

4. Instal dependensi:
    ```bash
    pip install -r requirements.txt
    ```

## Cara Menjalankan

Setelah semua dependensi terinstal, Anda dapat menjalankan aplikasi dengan perintah berikut:

```bash
streamlit run dashboard.py
