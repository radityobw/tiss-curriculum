# 📡 Week 7 · Day 1: Kenapa Hacker Pakai Linux?

> **Rank**: PACKET | **Minggu ke-7**, Hari 1/5 | **Durasi**: ~35 menit

📊 **Progress**: Week 7 · Day 1/5 | PACKET Rank (Minggu 3 dari 5) | Overall: 31/120 hari (26%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** alasan teknis mengapa Linux menjadi standar industri *cybersecurity*
2. **Mengenali** perbedaan antara GNU/Linux, Distro, dan Kernel
3. **Membedakan** peruntukan antara Ubuntu dan Kali Linux

---

## 📖 Materi Inti

### Selamat Tinggal, Mouse!

Di film-film, seorang *hacker* selalu digambarkan mengetik super cepat di layar hitam berhuruf hijau. Mereka tidak pernah menggunakan *mouse*. Layar hitam itu disebut **Terminal (Command Line Interface / CLI)**, dan sistem operasi yang mereka gunakan hampir pasti adalah **Linux**.

Mengapa *hacker* dan praktisi IT lebih memilih Linux daripada Windows atau macOS?

### 1. FOSS (Free and Open-Source Software)
Windows adalah *closed-source* (kode sumbernya dirahasiakan oleh Microsoft). Kamu harus membayar lisensi untuk memakainya, dan kamu dilarang mengubah cara kerjanya.
Linux adalah **Open-Source**. Kode sumbernya terbuka gratis untuk siapa saja. Kamu bisa membongkarnya, memodifikasinya, dan mengaturnya sesuka hati. Bagi seorang peretas yang pekerjaannya mengoprek sistem, kebebasan ini diperlukan.

### 2. Dibuat Oleh Programmer, Untuk Programmer
Linux (dan nenek moyangnya, UNIX) diciptakan dengan filosofi: *"Buatlah program kecil yang melakukan satu hal dengan sangat baik, lalu gabungkan mereka."*
Alat-alat di Linux dirancang untuk berjalan super cepat lewat teks (CLI). Menjalankan 100 perintah jaringan di Linux jauh lebih stabil dan cepat dibanding mengklik 100 tombol GUI (Grafis) di Windows.

### 3. Dunia Berjalan di Atas Linux
- **90%** dari server cloud (AWS, Google Cloud) dan website di seluruh dunia menggunakan Linux.
- **100%** dari 500 Superkomputer tercepat di dunia menggunakan Linux.
- Android di HP-mu menggunakan inti (Kernel) Linux.
Jika kamu ingin meretas atau melindungi server, kamu HARUS bisa berbicara bahasa server tersebut: Linux.

### Anatomi Linux: Kernel vs Distro

**Linux sebenarnya HANYA sebuah Kernel (Inti Mesin).**
Kernel adalah jembatan yang menghubungkan *software* (aplikasimu) dengan *hardware* (RAM, Processor).

Karena Kernel Linux itu gratis dan *open-source*, banyak perusahaan/komunitas yang mengambil Kernel ini, menempelkan tampilan grafis (Desktop), dan memasukkan aplikasi tambahan. Hasil racikan ini disebut **Distribusi Linux (Distro)**.

**2 Distro yang Paling Sering Kamu Dengar:**
1. **Ubuntu** 🟠
 - **Tujuan**: Untuk *general-purpose* (harian) atau Server.
 - **Sifat**: Sangat ramah pemula, stabil, dan komunitasnya terbesar. 
 - **Rekomendasi TISS**: **Gunakan ini dulu!** Belajarlah mengemudi di jalan yang lurus (Ubuntu) sebelum mengendarai mobil balap F1 (Kali).
2. **Kali Linux** 🐉
 - **Tujuan**: Khusus untuk *Penetration Testing* (Hacking).
 - **Sifat**: Membawa ribuan *tools hacking* bawaan yang berbahaya. Tidak stabil untuk pemakaian sehari-hari (buat ngetik tugas kampus/main game). 
 - **Catatan**: Jangan langsung install Kali jika kamu belum paham perintah dasar Linux. Kamu hanya akan bingung!

---

## 🧪 Mini Lab

**Durasi**: ~5 menit

Buka Google dan cari: **"Kali Linux vs Ubuntu for beginners"**
Baca 1-2 artikel atau tonton 1 video singkat yang muncul di halaman pertama.

**Tugas Refleksi:**
Banyak "hacker wannabe" yang pamer menginstal Kali Linux di hari pertama mereka belajar IT, tapi berakhir hanya menggunakan browser-nya saja untuk buka YouTube karena bingung. Berdasarkan pencarianmu, mengapa para ahli sangat TIDAK merekomendasikan Kali Linux untuk pemula total?

<details>
<summary>🔑 Pembahasan</summary>

Kali Linux sengaja didesain dengan tingkat keamanan yang sangat longgar (semua *tools* berjalan sebagai `root` atau Super Admin). Ini sangat berbahaya bagi pemula, karena salah mengetik satu perintah saja bisa merusak sistem tanpa peringatan. Selain itu, Kali tidak fokus pada *driver hardware* sehari-hari (seperti printer atau VGA game), sehingga sangat tidak nyaman dipakai kuliah. Belajarlah dasar Linux di Ubuntu dulu!

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa itu FOSS?</summary>

**Jawaban:** **Free and Open-Source Software**. FOSS berarti perangkat lunak tersebut gratis untuk digunakan, disebarluaskan, dan kode sumbernya (*source code*) bisa dibaca serta dimodifikasi oleh siapa saja secara publik.

</details>

<details>
<summary>❓ Jika seseorang bertanya: "Kamu pakai OS apa?", dan kamu menjawab "Linux", secara teknis jawaban itu kurang akurat. Mengapa?</summary>

**Jawaban:** Karena secara teknis, Linux HANYA merujuk pada **Kernel** (inti sistem). Jawaban yang lebih akurat adalah menyebutkan nama **Distro**-nya, misalnya "Saya menggunakan Ubuntu" atau "Saya menggunakan Linux Mint".

</details>

<details>
<summary>❓ Mengapa kita sangat disarankan menggunakan Command Line Interface (CLI/Terminal) di Linux dibanding antarmuka grafis (GUI) yang pakai mouse?</summary>

**Jawaban:** Karena sebagian besar server di dunia nyata beroperasi berstatus **Headless** (tanpa layar grafis/desktop) untuk menghemat RAM dan CPU. Kamu hanya bisa mengakses dan mengontrol server tersebut dari jarak jauh menggunakan teks (CLI). Selain itu, perintah teks bisa diotomatisasi dengan *script*, jauh lebih cepat dibanding mengklik mouse.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami alasan dominasi Linux di ranah Server dan Cybersecurity
- [ ] Saya mengerti bedanya Kernel Linux dan Distro Linux
- [ ] Saya paham mengapa sebaiknya belajar dari Ubuntu dulu ketimbang Kali Linux
- [ ] Saya siap untuk meninggalkan GUI dan mulai mengetik perintah di Terminal
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Linux Journey: Getting Started](https://linuxjourney.com/lesson/getting-started) — Website interaktif terbaik untuk belajar Linux dari nol (Bahasa Inggris).

---

## ➡️ Besok

**Day 2: File System (CLI)** — Waktunya praktik! Kita akan membuka layar hitam dan belajar bagaimana cara berpindah-pindah folder tanpa menggunakan File Explorer/Finder. Bersiaplah mengetik perintah `pwd`, `ls`, dan `cd` pertamamu!

---

*📅 TISS Null Teaming · Week 7 · Day 1 · PACKET Rank*
