---
type: quiz
week: 22
day: 1
title: "Quiz: SIEM Concepts & Architecture"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa fungsi utama dari fase *Normalize* (Normalisasi) pada arsitektur pemrosesan SIEM?
- [x] A. Mengonversi dan merapikan berbagai format log yang berbeda-beda (misal log Windows dan Apache) menjadi satu struktur tabel *Fields* yang seragam (seperti menyatukan kolom IP sumber menjadi atribut `src_ip`), sehingga memudahkan analisis data.
- [ ] B. Menormalisasi data dengan cara menghapus seluruh baris log yang berstatus *Error*.
- [ ] C. Mengubah log teks mentah menjadi visual grafik diagram *pie* pada Dasbor.
- [ ] D. Menyatukan IP penyerang dengan IP internal perusahaan untuk membingungkan deteksi.

### Q2
**Type:** True/False
**Question:** Pada arsitektur SIEM, fase *Correlate* (Korelasi) adalah proses di mana sistem secara otomatis menghubungkan dan mengaitkan dua atau lebih peristiwa dari sistem berbeda (misal: log kegagalan *login* VPN dan log sistem Windows) dalam satu rentang waktu untuk menemukan indikasi serangan.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat menjalankan operasi pengumpulan data log dari ribuan *server*, fase arsitektur SIEM apakah yang bertugas pertama kali menerima dan menghimpun aliran log mentah tersebut?
**Answer:** Fase Collect (Pengumpulan).

### Q4
**Type:** Short Answer
**Question:** Ketika SIEM mendeteksi hasil korelasi yang melanggar aturan (*Rules*) keamanan dan langsung mengirimkan notifikasi bahaya kepada tim SOC, proses ini terjadi pada fase SIEM apa?
**Answer:** Fase Alert (Peringatan).

### Q5
**Type:** Short Answer
**Question:** Fase arsitektur SIEM apa yang berfungsi mengarsipkan dan mengompresi log data operasional untuk jangka panjang demi memenuhi kebutuhan kepatuhan (*Compliance*) dan audit masa depan?
**Answer:** Fase Store (Penyimpanan Jangka Panjang).
