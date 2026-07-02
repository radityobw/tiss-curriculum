---
type: quiz
week: 20
day: 3
title: "Quiz: Log Sources & Syslog"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengurai arsitektur pemantauan , mengapa pencatatan riwayat (<i>Logs</i>) ditahbiskan laksana kamera CCTV bagi kelangsungan hidup Analis <i>Blue Team</i>?
- [x] A. Tanpa arsip <i>Logs</i>, sistem SOC akan buta total terhadap segala kejadian . Log menyuguhkan bukti historis tak terbantahkan (mencakup data krusial : siapa, apa, kapan, dan di mana sebuah aktivitas tereksekusi) yang merupakan landasan tunggal untuk mendeteksi ancaman dan menggelar investigasi forensik.
- [ ] B. Karena <i>Logs</i> otomatis menghapus ancaman <i>Ransomware</i>.
- [ ] C. *Logs* diwajibkan semata-mata guna menghindari serangan <i>CVSS 9.8</i>.
- [ ] D. *Logs* berguna untuk meraba celah <i>IDOR</i> bagi <i>Red Team</i>.

### Q2
**Type:** True/False
**Question:** Ketika seorang Analis keamanan menghendaki penelusuran alamat IP penyerang yang berulang kali menyuntikkan muatan <i>SQL Injection</i> pada parameter <i>URL</i> situs portal web korporasi, jenis sumber log (<i>Log Sources</i>) yang paling tepat untuk diinterogasi adalah <i>Operating System (OS) Logs</i>.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Di ranah arsitektur sentralisasi pengumpulan data , apa nama protokol pengiriman pesan standar (biasanya berjalan di port 514) yang didapuk untuk menyalurkan paket catatan <i>Log</i> dari ratusan klien ke satu <i>Server</i> pengumpul pusat?
**Answer:** Syslog.

### Q4
**Type:** Short Answer
**Question:** Ketika penganalisis menganalisis kueri akses di log <i>Apache/Nginx</i> dan mendapati barisan nilai `Mozilla/5.0...` atau `sqlmap/1.4`, sebutan atribut HTTP apa yang mewakili identitas perangkat peramban tamu ini?
**Answer:** User-Agent.

### Q5
**Type:** Short Answer
**Question:** Bila penganalisis keamanan menginvestigasi log peladen web dan menemukan pergerakan pengunjung normal dengan aktivitas membuka halaman profil, nilai kode balasan status HTTP apa (berawalan angka 2) yang menyuguhkan pertanda bahwa halaman berhasil dimuat tanpa halangan?
**Answer:** 200 (atau 200 OK).
