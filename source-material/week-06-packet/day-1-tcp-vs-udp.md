# 📡 Week 6 · Day 1: TCP vs UDP (Pertarungan Dua Raksasa)

> **Rank**: PACKET | **Minggu ke-6**, Hari 1/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 6 · Day 1/5 | PACKET Rank (Minggu 2 dari 5) | Overall: 26/120 hari (21%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** cara kerja TCP (Reliable) dan UDP (Fast)
2. **Menjelaskan** proses TCP *Three-Way Handshake*
3. **Menganalisis** kapan sebuah aplikasi harus menggunakan TCP dan kapan harus menggunakan UDP

---

## 📖 Materi Inti

### Transport Layer (Layer 4)

Minggu lalu kita belajar bahwa **Layer 3 (IP Address)** berfungsi mengantarkan paket ke komputer tujuan. Setelah paket sampai di komputer, siapa yang bertugas membagikan data tersebut ke aplikasi yang benar (misal: apakah ini untuk WhatsApp, atau untuk Chrome)? 

Itu adalah tugas **Transport Layer (Layer 4)**. Layer ini memilah data menggunakan "pintu-pintu" virtual yang disebut **Port** (Ada 65.535 port di komputermu!). 

Di layer ini, ada dua protokol pengiriman yang saling bertolak belakang: **TCP** dan **UDP**.

---

### 1. TCP (Transmission Control Protocol)

**Sifat:** Reliabel, Terurut, dan Sopan (Connection-oriented).
**Analogi:** Mengirim surat tercatat yang harus ditandatangani penerima. Jika kurir gagal mengirim, kurir akan kembali mengirim ulang sampai berhasil.

**Cara Kerja (TCP Three-Way Handshake):**
Sebelum TCP mengirim data sekecil apa pun, ia akan mengajak komputer tujuan berkenalan (bersalaman 3 kali):

1. **SYN** (Synchronize)
 Komputer A: *"Halo Server, apakah kamu hidup dan mau mengobrol denganku?"*
2. **SYN-ACK** (Synchronize-Acknowledge)
 Server: *"Halo A, ya aku hidup dan siap mengobrol. Ini balasan dariku."*
3. **ACK** (Acknowledge)
 Komputer A: *"Oke mantap, percakapan dimulai. Ini datanya..."*

Setelah selesai, TCP akan memecah data menjadi paket-paket bernomor urut. Jika ada paket nomor 3 yang hilang di jalan, TCP akan meminta server mengirim ulang paket nomor 3 tersebut.
- **Kelebihan**: Data dijamin utuh dan urut 100%. (Bagus untuk File Transfer, Email, Halaman Web).
- **Kekurangan**: Lebih lambat karena banyak proses verifikasi.

---

### 2. UDP (User Datagram Protocol)

**Sifat:** Super Cepat, Tanpa Jaminan, "Bodo Amat" (Connectionless).
**Analogi:** Seseorang yang melempar koran dari sepeda ke halaman rumahmu. Dia tidak peduli korannya sampai di teras atau nyangkut di atap, dia langsung pergi.

**Cara Kerja:**
UDP tidak kenal basa-basi (tidak ada *Handshake*). Begitu kamu minta, UDP langsung mengirimkan ribuan paket data ke IP tujuan secara brutal. Tidak ada nomor urut, tidak ada pengecekan ulang. Jika paket hilang di jalan, ya sudah hilang selamanya.
- **Kelebihan**: Kecepatan maksimal, tidak ada *delay* verifikasi.
- **Kekurangan**: Data bisa tiba dengan urutan acak atau hilang (*packet loss*).

**Kapan menggunakan UDP?**
- **Live Streaming / Video Call (Zoom, Discord)**: Jika ada 1 *frame* videomu yang hilang/nge-lag, Zoom tidak akan memintanya dikirim ulang (karena percuma, momennya sudah lewat). Mending lanjut ke *frame* berikutnya agar video tidak putus-putus.
- **Game Online (Valorant, Mobile Legends)**: Kamu butuh info posisi musuh *saat ini juga*, bukan posisi musuh 1 detik yang lalu.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Buka aplikasi **Spotify** atau **YouTube**, putar satu video/lagu. Kemudian buka website **Internet Banking** atau web **SIAKAD/Portal Kampus** (halaman login).

**Pertanyaan Refleksi:**
Menurut logikamu, protokol mana yang digunakan oleh Spotify/YouTube, dan protokol mana yang digunakan oleh Portal Kampus?

<details>
<summary>🔑 Klik untuk Pembahasan</summary>

- **Portal Kampus / Bank**: 100% menggunakan **TCP**. Saat kamu mentransfer uang, kamu tidak mau ada satu pun angka (byte) yang hilang di tengah jalan karena akan fatal! Keutuhan data adalah nomor satu.
- **Spotify / YouTube (Streaming)**: Sebagian besar menggunakan campuran, tapi intinya bergantung pada metode transmisi cepat mirip **UDP** (terutama untuk *Live streaming*). Jika beberapa bit audio hilang, suaranya mungkin sedikit kresek/turun kualitas sedetik, tapi lagunya tidak akan *pause* setiap detik hanya untuk mengecek data. (Catatan: YouTube juga menggunakan QUIC/UDP modern untuk mempercepat loading video).

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Jika kamu sedang men-download game berukuran 50GB, apakah sistem akan menggunakan TCP atau UDP?</summary>

**Jawaban:** **TCP**. Mengunduh file (*file transfer*) membutuhkan keutuhan data 100%. Jika 1 *byte* saja hilang atau urutannya terbalik, file game 50GB tersebut akan *corrupt* (rusak) dan tidak bisa di-install. TCP memastikan setiap byte di-download ulang jika gagal di tengah jalan.

</details>

<details>
<summary>❓ Proses perkenalan 3 langkah yang dilakukan oleh TCP sebelum mengirim data disebut apa?</summary>

**Jawaban:** **Three-Way Handshake**. Urutannya adalah: SYN (Tanya) → SYN-ACK (Jawab) → ACK (Konfirmasi).

</details>

<details>
<summary>❓ Mengapa game kompetitif seperti Valorant lebih memilih UDP daripada TCP?</summary>

**Jawaban:** Karena game kompetitif membutuhkan kecepatan (*low latency*). Jika TCP digunakan, saat ada data posisi pemain yang hilang karena koneksi jelek, game akan "berhenti" sebentar menunggu data itu dikirim ulang (membuat game terasa berat/nge-lag parah). Dengan UDP, game akan mengabaikan data yang hilang dan terus lanjut me-render data terbaru.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya bisa menjelaskan perbedaan utama TCP (utuh/lambat) dan UDP (cepat/tanpa jaminan)
- [ ] Saya hafal 3 langkah TCP Handshake (SYN, SYN-ACK, ACK)
- [ ] Saya bisa memberi contoh nyata aplikasi yang menggunakan TCP
- [ ] Saya bisa memberi contoh nyata aplikasi yang menggunakan UDP
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [TCP vs UDP Comparison (Video)](https://www.youtube.com/watch?v=uESXOAVbO-U) — Penjelasan visual pendek tapi padat tentang duel dua protokol ini.

---

## ➡️ Besok

**Day 2: HTTP/HTTPS Deep-Dive** — Besok kita akan naik ke Layer 7 (Application) dan membongkar protokol yang paling sering kamu gunakan: HTTP. Kamu akan tahu bedanya kode `200 OK` dengan `404 Not Found` (selain fakta bahwa 404 itu menyebalkan)!

---

*📅 TISS Null Teaming · Week 6 · Day 1 · PACKET Rank*
