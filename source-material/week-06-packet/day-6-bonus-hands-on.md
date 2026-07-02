# 🎯 Week 6 · Day 6 (Bonus): Hands-On Learning

> **Rank**: PACKET | **Minggu ke-6** | Bonus Day

---

## 🌐 Platform Hari Ini

**[Cisco Skills for All — Network Addressing and Basic Troubleshooting](https://skillsforall.com/course/network-addressing-and-basic-troubleshooting)**
Kursus lanjutan Cisco yang membahas pengalamatan IP, subnetting, dan teknik troubleshooting jaringan menggunakan CLI.

💰 **Biaya**: Gratis (kursus + digital badge gratis)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Memahami pengalamatan IPv4 dan prinsip dasar subnetting di platform Cisco
2. Menggunakan perintah troubleshooting jaringan (`ping`, `traceroute`) dan mengkorelasikan hasilnya dengan tangkapan Wireshark
3. Memulai progres kursus *Network Addressing and Basic Troubleshooting*

---

## 📋 Requirement

* Akun Cisco Skills for All (sudah dibuat di Week 5 Day 6)
* Peramban web modern (Chrome/Firefox)
* Terminal CLI (Command Prompt/Bash) — sudah tersedia di sistem operasi
* Wireshark terinstal (sudah diinstal di Day 4 minggu ini)

> ⚠️ **Jika Wireshark belum terinstal**: Unduh dari [wireshark.org/download](https://www.wireshark.org/download.html) — gratis dan open source. Ikuti wizard instalasi standar.

---

## 📝 Prosedur

### Langkah 1: Enroll & Mulai Kursus Cisco
1. Login ke [skillsforall.com](https://skillsforall.com)
2. Cari dan enroll ke kursus **"Network Addressing and Basic Troubleshooting"**
3. Buka **Module 1** — fokus pada konsep pengalamatan IP

### Langkah 2: Kerjakan Modul Pengalamatan IP
1. Pelajari materi tentang IPv4 addressing dan subnet mask
2. Kerjakan aktivitas interaktif (kalkulasi subnet, identifikasi network/host)
3. Selesaikan kuis di akhir modul

> 💡 **Jika subnetting terasa sulit**: Fokus pada memahami konsep Network ID vs Host ID terlebih dahulu. Kalkulasi detail bisa dipraktikkan bertahap.

### Langkah 3: Praktik CLI + Wireshark (Lokal)
1. Buka terminal di komputer lokal
2. Jalankan perintah berikut dan amati hasilnya:
 ```bash
 ping 8.8.8.8
 traceroute 8.8.8.8 # Linux/Mac
 # atau: tracert 8.8.8.8 # Windows
 ```
3. Buka Wireshark, pilih *interface* jaringan aktif (wlan0/eth0/Wi-Fi)
4. Mulai *capture*, lalu jalankan ulang perintah `ping 8.8.8.8`
5. Di Wireshark, terapkan filter: `icmp`
6. Amati paket ICMP Request dan Reply — cocokkan dengan output terminal

### Langkah 4: Dokumentasi
1. Ambil tangkapan layar:
 - Output terminal `ping` dan `traceroute`
 - Wireshark menampilkan paket ICMP yang tertangkap
2. Catat: Berapa hop yang dilalui paket dari komputer kamu ke 8.8.8.8?

---

## 🏁 Target Output

* ✅ Minimal **Module 1** kursus Network Addressing selesai
* 📸 Tangkapan layar terminal: output `ping 8.8.8.8` dan `traceroute 8.8.8.8`
* 📸 Tangkapan layar Wireshark: paket ICMP tertangkap dengan filter `icmp`
* 📝 Catatan: Jumlah hop ke 8.8.8.8 dan observasi singkat tentang paket ICMP

---

## 🔄 Fallback

Jika Cisco Skills for All tidak bisa diakses:
1. Buka [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures) (gratis)
2. Unduh file capture `http.cap` atau `telnet-raw.pcap`
3. Buka di Wireshark dan analisis protokol yang terlihat
4. Tetap lakukan praktik CLI `ping` dan `traceroute` di terminal lokal
