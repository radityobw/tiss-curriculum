# 🛡️ Week 22 · Day 2: Splunk Basics (Search Processing Language)

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 22 · Day 2/5 | SENTINEL Rank (Minggu 3 dari 5) | Overall: 107/120 hari (89%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengenali** fungsi dan arsitektur pengolahan data pada platform *Splunk*.
2. **Menyusun** kueri pencarian log menggunakan *Search Processing Language* (SPL).
3. **Mengekstrak** dan memfilter data analitik menggunakan perintah `stats`, `table`, dan seleksi *fields*.

---

## 📖 Materi Inti

### Pengantar Fungsionalitas Splunk

Dari semua solusi SIEM tingkat *Enterprise*, **Splunk** merupakan salah satu platform manajemen log terbesar yang paling banyak digunakan oleh perusahaan multinasional dan teknologi global. Kemampuan menyusun kueri pencarian data di Splunk adalah kompetensi inti yang wajib dimiliki oleh analis SOC modern.

Splunk memiliki kemampuan indeksasi (*Indexing*) berkapasitas sangat tinggi, menjadikannya mesin pencari spesifik yang sangat cepat untuk memproses jutaan baris data mesin dan log terpusat.

### Struktur Fundamental Kueri: SPL (Search Processing Language)

Pengoperasian pencarian log pada Splunk dilakukan menggunakan bahasa kueri khusus bernama **SPL (Search Processing Language)**.
Struktur SPL sangat mirip dengan konsep *Piping* di terminal Linux. Satu instruksi kueri akan dirangkaikan ke instruksi penyaringan selanjutnya menggunakan karakter garis vertikal/simbol `|` (Pipe).

**Contoh Struktur SPL Fundamental:**

1. **Pencarian Parameter Dasar (Filtering):**
   `index=web_logs sourcetype=access_combined status=404`
   *(Penjelasan: Mencari data di indeks "web_logs" yang berformat log akses web (Apache/Nginx), dengan memfilter secara spesifik hanya log yang menghasilkan status error 404).*

2. **Membuat Format Tabel (`table`):**
   `index=security_logs EventCode=4625 | table _time, user, src_ip`
   *(Penjelasan: Mencari log kegagalan login (EventCode 4625), lalu menghilangkan teks log mentah yang panjang, dan menyajikannya dalam bentuk tabel ringkas berisi 3 kolom: Waktu kejadian (`_time`), nama pengguna (`user`), dan IP penyerang (`src_ip`)).*

3. **Perhitungan Statistik (`stats count`):**
   `index=web_logs status=401 | stats count by src_ip | sort - count`
   *(Penjelasan: Mengekstrak indikasi akses ditolak (401), menghitung jumlah kejadian berdasarkan IP pelakunya (`src_ip`), lalu mengurutkannya dari jumlah terbanyak hingga terkecil (`sort - count`). Ini adalah teknik utama SOC untuk menemukan IP yang melakukan Brute Force).*

### Ekstraksi Parameter Otomatis (Fields)
Splunk secara dinamis dan otomatis mengekstrak informasi penting dari teks log mentah dan mengubahnya menjadi variabel yang dapat dicari. Variabel ini disebut **Fields**. Sebagai contoh, sistem Splunk dapat secara otomatis mengenali alamat IP seperti `192.168.1.1` di dalam log teks dan memasukkannya ke dalam parameter `src_ip`. Ini sangat memudahkan Analis karena tidak perlu lagi menggunakan alat teks rumit seperti `awk` untuk mengambil kolom tertentu.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan penyusunan bahasa kueri SPL!

1. Asumsikan Anda sedang menggunakan *Splunk Search bar*.
2. **Skenario:** Manajemen SOC melaporkan lonjakan aktivitas kegagalan koneksi *Remote Desktop* (RDP) di luar jam kerja. Anda diminta mencari tahu alamat IP penyerang yang melakukan aktivitas tersebut.
3. **Rencana Eksekusi:** Menulis kueri SPL untuk mencari indikasi penyerangan pada indeks keamanan Windows (`index=win_sec`).
4. **Instruksi 1 (Filter Log Pencarian):**
   Mencari log kegagalan autentikasi RDP: 
   `index=win_sec EventCode=4625 Logon_Type=10`
5. **Instruksi 2 (Kalkulasi Matematis):**
   Merangkai perintah untuk menghitung akumulasi serangan berdasarkan IP klien:
   `| stats count by Source_Network_Address`
6. **Integrasi Kueri Penuh:**
   `index=win_sec EventCode=4625 Logon_Type=10 | stats count by Source_Network_Address | sort - count`
7. **Hasil:** Splunk akan mengeksekusi kueri tersebut dan menampilkan tabel yang menunjukkan bahwa ada satu IP mencurigakan yang telah melakukan 5.000 kali upaya *login* berurutan. Ini mengonfirmasi serangan *Brute Force*.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa kepanjangan dari SPL, bahasa kueri yang digunakan untuk melakukan pencarian dan analisis log di dalam platform Splunk?</summary>

**Jawaban:** Search Processing Language.
</details>

<details>
<summary>❓ Saat menyusun kueri SPL, apa fungsi utama dari argumen perintah `table` (contoh: <code>| table _time, src_ip</code>)?</summary>

**Jawaban:** Berfungsi menghilangkan tampilan teks log mentah (*raw log*) yang kompleks dan merapikan data menjadi tabel yang hanya memuat kolom/parameter (*fields*) yang kita pilih.
</details>

<details>
<summary>❓ Jika seorang Analis SOC menjalankan perintah <code>| stats count by src_ip</code>, proses analitik apa yang akan dilakukan oleh Splunk?</summary>

**Jawaban:** Splunk akan menghitung total frekuensi kemunculan log berdasarkan masing-masing alamat IP pelakunya (*src_ip*).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami peran dan keunggulan *Splunk* sebagai platform SIEM.
- [ ] Saya mampu mendemonstrasikan penyusunan dasar kueri *SPL*.
- [ ] Saya memahami penggunaan parameter `table` untuk merapikan presentasi data.
- [ ] Saya mengerti fungsi ekstraksi metadata dinamis menggunakan taksonomi *Fields*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Splunk SPL Quick Reference Guide](https://www.splunk.com/pdfs/solution-guides/splunk-quick-reference-guide.pdf) — Panduan cepat (*cheat sheet*) resmi dari Splunk mengenai perintah-perintah dasar SPL.

---

## ➡️ Besok

**Day 3: Splunk Dashboards & Alerts** — Rutinitas seorang analis SOC tidak sekadar mengetik ulang kueri (Search String) berulang-ulang saat menelusuri ancaman. Keamanan korporat membutuhkan pemantauan otomatis. Esok hari, kita akan belajar bagaimana mengubah kueri SPL yang sudah kita buat hari ini menjadi visualisasi grafik pemantauan (*Dashboards*) serta menyusun notifikasi peringatan otomatis (*Alerts*).

---

*📅 TISS Null Teaming · Week 22 · Day 2 · SENTINEL Rank*
