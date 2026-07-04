# 🛡️ Week 24 · Day 4: Incident Report Writing

> **Rank**: SENTINEL | **Minggu ke-24**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 24 · Day 4/5 | SENTINEL Rank (Minggu 5 dari 5) | Overall: 119/120 hari (99%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Merangkum** tinjauan eksekutif dari keseluruhan insiden siber ke dalam dokumen non-teknis *(Executive Summary)*.
2. **Menyusun** rekaman kronologis tahapan respons investigasi *(Incident Timeline)* secara akurat.
3. **Mengevaluasi** penanganan insiden dan memberikan rekomendasi perbaikan (Fase PICERL terakhir: *Lessons Learned*).

---

## 📖 Materi Inti

### Capstone Fase 4: Pelaporan Insiden (Report Writing)

Penanganan teknis dari sebuah insiden memang telah diselesaikan oleh *Blue Team*. Namun di dunia profesional, penyelesaian tersebut tidak akan diakui jika tidak didokumentasikan dalam laporan yang jelas. Menulis **Laporan Insiden Siber (Cyber Incident Report)** adalah kemampuan puncak yang membedakan spesialis SOC tingkat lanjut (*SENTINEL*) dari analis biasa.

Dokumentasi ini harus bisa dipahami oleh dua tipe pembaca: **Spektrum Non-Teknis (Manajemen Eksekutif / CEO / Direksi)** dan **Spektrum Teknis (Tim SOC dan Insinyur Keamanan)**.

### Anatomi Dokumen Laporan Insiden Standar

Susunan *Cyber Incident Report* berstandar industri memiliki komponen inti sebagai berikut:

1. **Executive Summary (Ringkasan Eksekutif):**
   Bagian pembuka yang dirancang eksklusif untuk jajaran manajemen eksekutif (C-Level). Laporannya sangat ringkas (1-2 paragraf) dan hanya memuat: *Apa yang terjadi (misal: kebocoran web), Dampak kerugian (misal: database aman, 5 dokumen terekspos), dan Status saat ini (misal: server telah pulih 100%)*. **Dilarang keras** menggunakan jargon teknis (seperti nilai Hash atau IOC) yang dapat membingungkan pimpinan.
2. **Incident Timeline (Kronologi Insiden):**
   Dokumentasi kronologis kejadian berdasarkan waktu (*Time to Detect & Respond*):
   - *03:00* - Peringatan SIEM Splunk muncul *(Deteksi serangan SQLi)*.
   - *03:15* - Tim SOC melakukan isolasi server *(Containment)*.
   - *04:00* - Skrip malware dihapus *(Eradication)* dan blokade IP peretas diterapkan.
3. **Technical Findings & Root Cause (Detail Taktikal Investigasi Forensik):**
   Bagian teknis mendalam yang menjabarkan hasil analisis forensik (Untuk konsumsi Tim SOC/IT). Meliputi pemetaan **TTPs MITRE ATT&CK**, daftar **Indicators of Compromise / IOCs** (seperti *IP Address* penyerang & *Hash malware*), serta penjelasan teknis tentang kerentanan utama (**Root Cause**) yang dieksploitasi peretas (contoh: celah *SQL Injection* di halaman *login*).
4. **Lessons Learned (Pelajaran dan Rekomendasi):**
   Ini adalah langkah terakhir dari siklus PICERL (huruf 'L'). Di tahap ini, tim SOC memberikan rekomendasi evaluasi perbaikan untuk masa depan. (Contoh rekomendasi: *"Tim pengembang web disarankan untuk segera menerapkan sanitasi input (Secure Coding) guna mencegah kerentanan SQL Injection di masa mendatang"*).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi penulisan laporan manajerial (*Executive Summary*)!

1. Siapkan aplikasi pengolah teks (Notepad/VS Code).
2. **Skenario:** Anda memimpin tim *Incident Response* yang baru saja menyelesaikan penanganan kasus pembobolan dokumen HRD akibat serangan email jebakan (*Phishing*).
3. **Misi:** CEO membutuhkan laporan cepat. Tuliskan *Executive Summary* dalam format narasi bisnis non-teknis tanpa menyebutkan *Hash*, IP Address, atau jargon teknis lainnya!
4. **Draft Laporan Jawaban Analis (Contoh Executive Summary):**
   *"Pada tanggal 25 Mei pukul 09:00 pagi, perusahaan mengalami insiden keamanan yang diawali dari email penipuan (Phishing) yang menargetkan staf HRD. Insiden ini menyebabkan 5 (lima) dokumen internal perusahaan terekspos. Tim keamanan (SOC) telah berhasil memutus akses peretas, mengamankan seluruh sistem, dan memastikan bahwa database nasabah tetap aman. Saat ini, seluruh sistem dan layanan operasional perusahaan telah pulih 100% dan berjalan normal."*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam format standar Laporan Insiden Siber, bagian apa yang ditempatkan di awal halaman, ditulis menggunakan bahasa bisnis (tanpa jargon teknis), dan ditargetkan untuk pimpinan eksekutif (CEO/Direksi)?</summary>

**Jawaban:** Executive Summary (Ringkasan Eksekutif).
</details>

<details>
<summary>❓ Bagian apa di dalam Laporan Insiden yang berfungsi untuk mencatat rentetan kejadian secara berurutan berdasarkan waktu (mulai dari deteksi awal hingga sistem pulih)?</summary>

**Jawaban:** Incident Timeline (Kronologi Insiden).
</details>

<details>
<summary>❓ Dalam siklus respons insiden PICERL, tahap paling akhir di mana tim melakukan retrospeksi dan merumuskan rekomendasi perbaikan untuk masa depan diwakili oleh huruf 'L'. Apa kepanjangan dari 'L' tersebut?</summary>

**Jawaban:** Lessons Learned.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami cara menyusun *Executive Summary* tanpa jargon teknis.
- [ ] Saya fasih merumuskan urutan kejadian ke dalam format *Incident Timeline*.
- [ ] Saya mengetahui peran bagian *Lessons Learned* dalam memberikan rekomendasi.
- [ ] Saya paham bahwa laporan akhir adalah jembatan komunikasi antara tim teknis dan manajemen.
- [ ] Saya telah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS: Incident Report Cheat Sheet](https://www.sans.org/white-papers/34520/) — Referensi format struktural untuk menyusun Laporan Insiden Keamanan Siber di dunia industri.

---

## ➡️ Preview Besok (Tahap Kulminasi Kelulusan!)

**Day 5: Capstone Mission & Graduation** — Perjalanan panjang Anda di kurikulum TISS Null Teaming telah menginjak hari terakhir! Penugasan dari Hari 1 hingga Hari 4 pada minggu ini akan dilebur menjadi satu proyek akhir. Misi kelulusan Anda besok adalah menyusun **Laporan Insiden Siber Komprehensif (Full Cyber Incident Report)** dari skenario eksploitasi web *SQLi*. 

Anda berkesempatan untuk mengintegrasikan semua ilmu yang telah Anda pelajari, membuktikan kapabilitas teknis Anda, dan mengamankan gelar spesialis SOC tingkat **SENTINEL** di penghujung perjalanan epik ini!

---

*📅 TISS Null Teaming · Week 24 · Day 4 · SENTINEL Rank*
