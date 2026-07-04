# 📡 Week 5 · Day 1: Model OSI Layer (Bagian 1)

> **Rank**: PACKET | **Minggu ke-5**, Hari 1/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 5 · Day 1/5 | PACKET Rank (Minggu 1 dari 5) | Overall: 21/120 hari (17%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep dasar di balik komunikasi dua komputer
2. **Menjelaskan** tujuan dari Model referensi OSI
3. **Mengidentifikasi** fungsi spesifik dari Layer 1 hingga Layer 4 (Lower Layers)

---

## 📖 Materi Inti

### Selamat Datang di PACKET Rank!

Mulai minggu ini, kita akan membongkar urat nadi internet: **Jaringan Komputer**. Jika kamu ingin menjadi *hacker* (Red Team) atau *defender* (Blue Team) yang hebat, kamu HARUS tahu persis bagaimana data berpindah dari Titik A ke Titik B.

> *"If you don't know how a network works, you can't break into it, and you certainly can't protect it."*

### Apa itu Model OSI?

Bayangkan kamu memesan barang dari toko online luar negeri:
1. Kamu klik "Beli" di aplikasi.
2. Gudang membungkus barangmu.
3. Barang dimasukkan ke payload pesawat.
4. Barang tiba di bandara lokalku, pindah ke truk kurir.
5. Kurir menyerahkan ke tanganmu.

Agar semua proses itu berjalan lancar tanpa kebingungan bahasa antar negara, dibutuhkan **aturan standar**. Di dunia komputer, aturan ini disebut **Model OSI** (*Open Systems Interconnection*).

Model OSI membagi proses pengiriman data yang sangat rumit menjadi **7 lapisan (Layer) kecil yang terpisah**. 

Hari ini kita bahas 4 layer paling bawah (Fokus pada pengiriman fisik).

### Lower Layers (Layer 1 - 4)

```
[Layer Atas: Fokus pada Aplikasi - Dibahas Besok]

4️⃣ TRANSPORT LAYER (Segmen)
3️⃣ NETWORK LAYER (Paket)
2️⃣ DATA LINK LAYER (Frame)
1️⃣ PHYSICAL LAYER (Bit)

[Kabel / Wi-Fi / Sinyal Fisik]
```

#### Layer 1: Physical Layer (Fisik)
- **Tugas:** Mentransfer data mentah berupa angka 0 dan 1 (*Bits*) melalui media fisik (kabel tembaga, fiber optik, atau gelombang radio/Wi-Fi).
- **Analogi:** Jalan aspal, truk kurir, atau rel kereta.
- **Perangkat:** Kabel UTP, Hub, Repeater.

#### Layer 2: Data Link Layer
- **Tugas:** Memastikan data dari Layer 1 bebas dari error dan menentukan ke "MAC Address" mana data harus dikirim di dalam jaringan lokal (satu rumah/kantor). Bentuk datanya disebut *Frame*.
- **Analogi:** Petugas sortir di kantor pos cabang yang mengecek nama jalan.
- **Perangkat:** Switch, Network Interface Card (NIC).

#### Layer 3: Network Layer (Jaringan)
- **Tugas:** Menentukan rute (*routing*) dari satu komputer ke komputer lain di beda kota/negara menggunakan **IP Address**. Bentuk datanya disebut *Packet*. (Inilah asal nama rank kita!).
- **Analogi:** GPS dan Kode Pos.
- **Perangkat:** Router.
- **Protokol Terkenal:** IP (Internet Protocol).

#### Layer 4: Transport Layer (Transportasi)
- **Tugas:** Memecah data besar menjadi potongan kecil (*Segment*). Memastikan data sampai dengan selamat dan utuh, atau mengirimnya dengan sangat cepat (memilih antara keandalan vs kecepatan). Mengatur **Port**.
- **Analogi:** Layanan resi paket (apakah pakai asuransi yang dijamin sampai, atau pengiriman kilat biasa).
- **Protokol Terkenal:** TCP (Aman/Reliabel), UDP (Cepat).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari kita lihat perangkat keras yang bekerja di Layer 2 (MAC Address) pada komputermu sendiri.

**Windows:**
1. Buka Command Prompt (`cmd`).
2. Ketik perintah: `getmac -v` lalu tekan Enter.

**Mac/Linux:**
1. Buka Terminal.
2. Ketik perintah: `ifconfig | grep ether` (Mac) atau `ip link` (Linux).

**Expected Output:**
Kamu akan melihat deretan huruf dan angka sepanjang 12 karakter yang dipisah titik dua atau strip (Contoh: `00-1B-44-11-3A-B7`). 

Itu adalah **MAC Address**. Ini adalah "KTP Permanen" dari kartu jaringanmu, dan MAC Address adalah pemain utama di **Layer 2 (Data Link)**.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa kita perlu membagi proses jaringan komputer menjadi 7 Layer OSI?</summary>

**Jawaban:** Untuk memecah masalah komunikasi yang sangat kompleks menjadi bagian-bagian kecil (modular). Dengan begitu, perusahaan yang membuat kabel jaringan (Layer 1) tidak perlu pusing memikirkan cara kerja browser web (Layer 7). Jika terjadi kerusakan (troubleshooting), kita juga bisa melacaknya lapis demi lapis.

</details>

<details>
<summary>❓ Layer mana yang bertanggung jawab mencarikan rute tercepat melalui internet menggunakan IP Address?</summary>

**Jawaban:** **Layer 3 (Network Layer)**. Alat utamanya adalah **Router**.

</details>

<details>
<summary>❓ Kabel LAN yang sering kamu colok ke laptop bekerja di Layer berapa?</summary>

**Jawaban:** **Layer 1 (Physical Layer)**. Di sinilah sinyal listrik nyata bergerak mengirimkan rentetan angka 1 dan 0.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami konsep dasar dari Model referensi OSI
- [ ] Saya hafal fungsi Layer 1 (Physical)
- [ ] Saya hafal fungsi Layer 2 (Data Link)
- [ ] Saya hafal fungsi Layer 3 (Network)
- [ ] Saya hafal fungsi Layer 4 (Transport)
- [ ] Saya sudah melihat MAC Address di komputer saya
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [NetworkChuck: You NEED to learn the OSI Model](https://www.youtube.com/watch?v=qB2pYmBpq4U) — Penjelasan OSI model paling seru yang menggunakan analogi pizza.

---

## ➡️ Besok

**Day 2: Model OSI Layer (Bagian 2)** — Besok kita selesaikan pendakian kita ke puncak! Kita akan melihat bagaimana Layer 5, 6, dan 7 berinteraksi langsung dengan aplikasi yang kamu pakai setiap hari (seperti Chrome atau WhatsApp).

---

*📅 TISS Null Teaming · Week 5 · Day 1 · PACKET Rank*
