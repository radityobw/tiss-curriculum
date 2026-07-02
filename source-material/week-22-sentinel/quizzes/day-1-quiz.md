---
type: quiz
week: 22
day: 1
title: "Quiz: SIEM Concepts & Architecture"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengurai anatomi sistem otomatisasi SOC, apa fungsi utama dari fase <i>Normalize (Normalisasi)</i> pada arsitektur mesin SIEM?
- [x] A. SIEM menerjemahkan bermacam-macam format teks log yang berbeda-beda (misal log dari *Windows* dan log dari *Apache*) lalu merapikannya menjadi satu bentuk struktur data *(Fields)* yang seragam (seperti menyatukan kolom IP sumber menjadi satu variabel `src_ip`), sehingga memudahkan proses analisis dan pencarian data.
- [ ] B. SIEM menormalisasi data dengan cara menghapus seluruh log *Error*.
- [ ] C. Fase ini berfungsi merubah log teks menjadi visual grafik diagram pie (Dashboard).
- [ ] D. SIEM menyatukan IP peretas dengan IP Direktur perusahaan.

### Q2
**Type:** True/False
**Question:** Di arsitektur algoritma SIEM, fase *Correlate (Korelasi)* merupakan proses di mana SIEM menghubungkan dan menautkan peringatan dari sebuah perangkat dengan peringatan dari perangkat lainnya (misal: menyatukan insiden VPN dan log Windows) dalam satu garis waktu kronologis untuk menyimpulkan adanya serangan terstruktur.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat menjalankan instruksi pengumpulan data log dari ribuan peladen (server) korporasi, fase SIEM apakah yang bertugas pertama kali menerima aliran data dari agen pengirim *(Forwarders)*?
**Answer:** Fase Collect (Pengumpulan).

### Q4
**Type:** Short Answer
**Question:** Ketika seorang penganalisis menemukan hasil korelasi kueri yang terbukti melebihi ambang batas risiko, dan sistem SIEM menampilkan notifikasi bahaya (seperti mengirim peringatan ke email), fase SIEM manakah tindakan ini?
**Answer:** Fase Alert (Peringatan).

### Q5
**Type:** Short Answer
**Question:** Dalam standar kepatuhan regulasi korporasi, fase arsitektur SIEM apakah yang difungsikan untuk mengompres dan mengarsipkan data log operasional selama bertahun-tahun demi kebutuhan audit dan forensik masa depan?
**Answer:** Fase Store (Penyimpanan Jangka Panjang).
