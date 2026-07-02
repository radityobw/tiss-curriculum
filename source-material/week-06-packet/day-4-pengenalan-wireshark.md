# 📡 Week 6 · Day 4: Pengenalan Wireshark

> **Rank**: PACKET | **Minggu ke-6**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 6 · Day 4/5 | PACKET Rank (Minggu 2 dari 5) | Overall: 29/120 hari (24%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** fungsi Wireshark sebagai *Packet Sniffer / Protocol Analyzer*
2. **Menginstal** Wireshark di OS komputermu
3. **Mengoperasikan** antarmuka dasar Wireshark dan memahami kegunaan *Display Filters*

---

## 📖 Materi Inti

### Kacamata Sinar-X Internet: Wireshark 🦈

Pernah berkhayal bisa melihat data yang melayang-layang di kabel LAN atau sinyal WiFi di kosanmu? 

**Wireshark** adalah alatnya. Wireshark adalah perangkat lunak penganalisis paket jaringan (*Packet Sniffer*) paling populer di dunia. 
Ini adalah tool yang wajib dimiliki oleh semua orang di IT, baik *Network Engineer* yang sedang mencari masalah server, *Blue Team* yang mendeteksi intrusi *hacker*, maupun *Red Team* yang mencari celah dan mencuri password.

> ⚠️ **Peringatan Etika**: Menggunakan Wireshark untuk merekam (sniffing) jaringan publik (seperti WiFi Cafe atau kampus) tanpa izin adalah **tindakan ilegal**. Gunakan Wireshark HANYA pada komputermu sendiri (localhost) atau pada jaringan rumah yang kamu miliki!

### Bagaimana Wireshark Bekerja?

Biasanya, kartu jaringan (WiFi/Ethernet) di komputermu sangat sopan. Jika ada paket data yang lewat di udara, tapi label tujuannya BUKAN MAC Address milikmu, kartu jaringanmu akan membuangnya. (Ini disebut *Normal Mode*).

Saat kamu menyalakan Wireshark (khususnya dengan *Promiscuous Mode* aktif), kartu jaringanmu menjadi rakus. Ia akan menyedot dan membaca **semua** paket data yang melintas, terlepas ditujukan untuk siapa paket itu!

### Tiga Bagian Utama Wireshark

Ketika kamu berhasil melakukan "Capture" (merekam trafik), antarmuka Wireshark terbagi menjadi 3 baris horisontal:

1. **Packet List (Atas)**: Daftar antrean setiap paket yang ditangkap (No, Waktu, IP Asal, IP Tujuan, Protokol, Info).
2. **Packet Details (Tengah)**: Jika kamu klik satu baris di atas, kotak tengah ini akan membedah isi paket tersebut lapis demi lapis berdasarkan **OSI Layer**! (Mulai dari Layer 2 Ethernet, Layer 3 IPv4, Layer 4 TCP, dst).
3. **Packet Bytes (Bawah)**: Menampilkan data dalam format Hexadecimal dan ASCII (huruf mentah). Di sinilah password atau data telanjang (*plaintext*) bisa terbaca.

### Menjinakkan Lautan Data (Display Filters)

Masalah utama Wireshark adalah ia **terlalu detail**. Dalam 10 detik merekam jaringan yang sepi sekalipun, ia bisa menangkap ribuan baris paket (karena komputer diam-diam selalu *update* aplikasi di *background*).

Untuk tidak kebanjiran data, kita menggunakan kolom hijau di bagian atas yang disebut **Display Filter**.

Contoh filter ajaib:
- `http` → Hanya tampilkan lalu lintas web yang tidak terenkripsi.
- `dns` → Hanya tampilkan query resolusi nama (buku telepon).
- `ip.addr == 8.8.8.8` → Hanya tampilkan data yang dikirim KE atau DARI IP Google.
- `tcp.port == 443` → Hanya tampilkan koneksi HTTPS (web aman).

---

## 🧪 Mini Lab

**Durasi**: ~20 menit

Waktunya menginstal Wireshark! (Tool ini gratis dan open-source).

1. Buka [wireshark.org/download](https://www.wireshark.org/download.html).
2. Download *installer* yang sesuai dengan OS-mu.
3. **Instruksi Khusus Windows**: Saat instalasi, pastikan kamu menceklis **Install Npcap**. Npcap adalah driver wajib agar Wireshark bisa mencegat trafik langsung dari *hardware* jaringanmu.
4. **Instruksi Khusus Linux/Mac**: Kamu mungkin harus menjalankan wireshark dengan perintah `sudo wireshark` (karena menangkap paket di bawah layar membutuhkan akses *Root/Admin*).

**Uji Coba Pertama:**
1. Buka aplikasi Wireshark.
2. Di layar beranda, kamu akan melihat grafik detak jantung (*sparkline*) di sebelah nama-nama adapter (misal: *Wi-Fi* atau *Ethernet*). Pilih adapter yang grafiknya bergerak-gerak.
3. Klik kanan pada nama adapter itu, lalu pilih **Start Capture**.
4. Biarkan berjalan selama 10 detik (kamu akan melihat ribuan baris warna-warni berlarian).
5. Klik ikon kotak merah (Stop Capture) di pojok kiri atas.

Selamat! Kamu baru saja menyadap jaringan komputermu sendiri untuk pertama kalinya.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa itu "Promiscuous Mode" pada Network Interface Card?</summary>

**Jawaban:** Mode di mana kartu jaringan diinstruksikan untuk mencegat (menyalin) **semua lalu lintas** jaringan yang lewat, bahkan jika paket data tersebut secara fisik/logis bukan ditujukan untuk MAC Address komputer tersebut.

</details>

<details>
<summary>❓ Apa perbedaan antara "Packet List" dan "Packet Details" di antarmuka Wireshark?</summary>

**Jawaban:** *Packet List* menampilkan daftar rangkuman semua paket data secara kronologis (per baris). Sedangkan *Packet Details* membedah isi dari satu paket spesifik secara mendalam (di-breakdown berdasarkan struktur layer protokol/OSI Layer).

</details>

<details>
<summary>❓ Jika kamu ingin memfilter dan hanya melihat paket yang ditujukan ke website dengan keamanan HTTPS, filter apa yang harus kamu ketik?</summary>

**Jawaban:** `tcp.port == 443` (atau cukup mengetik `tls`). Karena HTTPS beroperasi pada protokol TCP port 443 dan menggunakan TLS untuk enkripsi.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami cara kerja Wireshark sebagai sniffer
- [ ] Saya mengerti aturan etika/hukum (jangan sniff jaringan publik/kampus!)
- [ ] Saya berhasil menginstal Wireshark (dan Npcap jika di Windows)
- [ ] Saya sudah melakukan lab uji coba tangkapan pertama (10 detik capture)
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Wireshark Official User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/) — Dokumentasi super lengkap jika kamu bingung arti sebuah tombol.

---

## ➡️ Besok

**Day 5: Lab & Mission: Analisis Trafik Wireshark** — Kita tutup minggu kedua PACKET Rank dengan sesi peretasan ringan. Kamu akan memantau trafikmu sendiri saat login ke website HTTP (tidak aman) dan menemukan passwordmu di dalam Wireshark!

---

*📅 TISS Null Teaming · Week 6 · Day 4 · PACKET Rank*
