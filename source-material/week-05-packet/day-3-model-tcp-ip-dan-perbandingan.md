# 📡 Week 5 · Day 3: Model TCP/IP & Perbandingan

> **Rank**: PACKET | **Minggu ke-5**, Hari 3/5 | **Durasi**: ~35 menit

📊 **Progress**: Week 5 · Day 3/5 | PACKET Rank (Minggu 1 dari 5) | Overall: 23/120 hari (19%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menjelaskan** apa itu Model TCP/IP dan mengapa ia memenangkan "perang standar" internet
2. **Memetakan** persamaan dan perbedaan antara Model OSI (7 Layer) dengan Model TCP/IP (4 Layer)
3. **Memahami** fungsi praktis dari pemodelan ini di dunia nyata (troubleshooting)

---

## 📖 Materi Inti

### Plot Twist: Internet Tidak Pakai OSI Model!

Dua hari kemarin kita susah payah menghafal 7 layer OSI. Namun faktanya, saat kamu membaca ini, komputermu dan internet **TIDAK** beroperasi menggunakan arsitektur OSI.

Internet di seluruh dunia beroperasi menggunakan standar yang lebih ringan dan tangguh: **Model TCP/IP**.

*Kenapa kita repot-repot belajar OSI?*
Karena OSI adalah **model konseptual/teori terbaik** untuk referensi pembelajaran dan sertifikasi IT di seluruh dunia, sedangkan TCP/IP adalah **model praktis/faktual** yang benar-benar tertulis di dalam kode sistem operasi komputermu.

### Membandingkan OSI dan TCP/IP

TCP/IP menggabungkan beberapa layer OSI yang dianggap terlalu detail menjadi lapisan-lapisan yang lebih simpel. Awalnya TCP/IP punya 4 layer, namun versi terbarunya sering diajarkan menjadi 5 layer. Kita akan berpegang pada model 4 layer tradisional.

| Layer OSI (7 Layer) | Layer TCP/IP (4 Layer) | Penjelasan TCP/IP |
|--------------------|------------------------|-------------------|
| 7. Application | \multirow{3}{*}{**4. Application**} | Menggabungkan Layer 5, 6, 7 OSI. Aplikasi modern mengurus sesi dan enkripsi mereka sendiri (HTTPS/TLS). |
| 6. Presentation| | |
| 5. Session | | |
| 4. Transport | **3. Transport** | Sama persis. Mengatur flow data (TCP & UDP). |
| 3. Network | **2. Internet** | Sama persis. Mengatur IP dan Routing. |
| 2. Data Link | \multirow{2}{*}{**1. Network Access**} | Menggabungkan hardware (kabel fisik dan MAC address/Switch) menjadi satu kesatuan. |
| 1. Physical | | |

> 💡 **Analogi**: 
> Model OSI adalah manual perakitan mobil setebal 1000 halaman yang sangat rinci (sampai baut terkecil). 
> Model TCP/IP adalah manual praktis 4 halaman untuk mekanik: Mesin, Rangka, Kelistrikan, dan Interior.

### Mengapa TCP/IP Menang?

Pada era 1980-an, terjadi "Protocol Wars". TCP/IP didanai oleh militer AS (ARPANET) dan dikembangkan dengan filosofi: *"Coding dulu, buat standar teorinya belakangan agar cepat jalan."*
Sementara itu, OSI dikembangkan oleh lembaga internasional dengan filosofi: *"Bikin teori standarnya yang sempurna dulu, baru kita coding."*

Hasilnya, TCP/IP diadopsi secara luas lebih dulu dan menjadi pondasi internet sebelum OSI sempat merilis produk nyata.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Di dunia *cybersecurity*, pemahaman layer sangat penting untuk **troubleshooting** (mencari letak masalah) saat server down atau koneksi gagal. Seorang SysAdmin akan selalu mengecek dari bawah ke atas.

**Studi Kasus:**
Kamu tidak bisa membuka halaman web `google.com`. 
Uji logikamu dengan menebak di layer mana (versi TCP/IP) masalah berikut terjadi:

1. Kabel LAN-mu digigit tikus dan putus. (Layer apa?)
2. Website tidak terbuka karena sertifikat keamanannya (SSL) kedaluwarsa. (Layer apa?)
3. IP Address komputermu bentrok dengan IP orang lain. (Layer apa?)

<details>
<summary>🔑 Klik untuk melihat kunci jawaban</summary>

1. Kabel putus = **Layer 1 (Network Access)** (karena urusan kabel fisik).
2. Sertifikat SSL bermasalah = **Layer 4 (Application)** (karena berkaitan dengan presentasi enkripsi web browser).
3. IP Address bentrok = **Layer 2 (Internet)** (karena berkaitan dengan rute logis jaringan).

Troubleshooting selalu dimulai dari Layer 1 (Cek kabelnya!) lalu naik ke atas. Jangan utak-atik settingan browser (Layer 4) jika ternyata kabel LAN belum dicolok!

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Berapa jumlah layer pada model OSI dan model TCP/IP tradisional?</summary>

**Jawaban:** OSI memiliki **7 Layer**, sedangkan TCP/IP memiliki **4 Layer** (atau 5 layer pada buku teks modern).

</details>

<details>
<summary>❓ Layer "Application" pada model TCP/IP merupakan gabungan dari 3 layer apa saja di model OSI?</summary>

**Jawaban:** Menggabungkan Layer 5 (Session), Layer 6 (Presentation), dan Layer 7 (Application).

</details>

<details>
<summary>❓ Mengapa kita masih mempelajari Model OSI padahal internet menggunakan TCP/IP?</summary>

**Jawaban:** Karena OSI jauh lebih detail dan sistematis. OSI adalah **bahasa universal** (*lingua franca*) para ahli IT. Jika kamu bicara dengan network engineer lain dan berkata "ada masalah di Layer 2", semua orang di dunia langsung paham maksudmu adalah isu MAC Address / Switch tanpa perlu penjelasan panjang lebar.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya mengetahui bahwa internet berjalan menggunakan TCP/IP, bukan OSI
- [ ] Saya tahu TCP/IP terdiri dari 4 (atau 5) layer
- [ ] Saya bisa memetakan 7 Layer OSI ke dalam 4 Layer TCP/IP
- [ ] Saya paham konsep dasar *troubleshooting* dari layer paling bawah
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [OSI vs TCP/IP Model (Cisco NetAcad)](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13769-5.html) — Dokumentasi perbandingan resmi standar Cisco.

---

## ➡️ Besok

**Day 4: IP Address, Subnet & DNS** — Kita akan membedah buku telepon dunia (DNS) dan memahami bagaimana IP Address disusun seperti blok perumahan. Persiapkan logikamu, karena kita akan bermain dengan angka-angka jaringan!

---

*📅 TISS Null Teaming · Week 5 · Day 3 · PACKET Rank*
