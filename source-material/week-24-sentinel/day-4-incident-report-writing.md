# 🛡️ Week 24 · Day 4: Incident Report Writing

> **Rank**: SENTINEL | **Minggu ke-24**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 24 · Day 4/5 | SENTINEL Rank (Minggu 5 dari 5) | Overall: 119/120 hari (99%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Merangkum** tinjauan eksekutif dari keseluruhan rangkaian insiden siber ke dalam dokumen non-teknis *(Executive Summary)*.
2. **Menyusun** rekaman kronologis tahapan respons investigasi *(Incident Timeline)* secara akurat.
3. **Mengevaluasi** penanganan insiden guna merumuskan rekomendasi struktural lewat fase PICERL terakhir: *Lessons Learned*.

---

## 📖 Materi Inti

### Capstone Fase 4: Pelaporan Insiden Formal Korporasi (Report Writing)

Penanganan teknis dari sebuah insiden memang telah diselesaikan oleh tim *Blue Team*. Namun di dunia industri, pencapaian tersebut tidak akan diakui jika tidak didokumentasikan dalam laporan yang komprehensif. Menulis naskah **Laporan Insiden Siber (Cyber Incident Report)** adalah kemampuan puncak yang membedakan seorang spesialis SOC level *SENTINEL* dari analis biasa.

Dokumentasi audit ini harus dirancang agar komunikatif bagi dua spektrum pembaca: **Spektrum Non-Teknis (Manajemen Eksekutif / CEO / Direksi)** dan **Spektrum Teknis (Tim SOC dan Insinyur Keamanan)**.

### Anatomi Dokumen Laporan Insiden Standar

Susunan formal *Cyber Incident Report* berstandar industri memiliki komponen inti sebagai berikut:

1. **Executive Summary (Ringkasan Eksekutif):**
   Bagian pembuka yang dirancang eksklusif untuk jajaran C-Level manajemen korporat. Komposisi laporannya sangat singkat (satu hingga dua paragraf). Bagian ini hanya mendefinisikan inti kejadian: *Apa yang terjadi (misal: eksploitasi web), Dampak kerugian (misal: database aman, 5 dokumen terekspos), dan Status saat ini (misal: server telah pulih 100%)*. **Sangat diharamkan** menggunakan jargon teknis (seperti Hash malware atau IOC) yang dapat membingungkan pimpinan.
2. **Incident Timeline (Kronologi Eksekusi Waktu):**
   Dokumentasi kronologis respons tanggap insiden (*Time to Detect & Respond*):
   - *03:00* - Peringatan SIEM Splunk terkonfirmasi *(Detection awal SQLi)*.
   - *03:15* - Tim SOC melakukan isolasi server *(Containment)*.
   - *04:00* - Skrip malware berhasil dihapus *(Eradication)* dan blokade IP eksternal terkonfigurasi.
3. **Technical Findings & Root Cause (Detail Taktikal Investigasi Forensik):**
   Bagian teknis mendalam yang menjabarkan hasil analisis forensik. Meliputi pemetaan taksonomi **TTPs MITRE ATT&CK**, inventaris arsip **Indicators of Compromise / IOCs** (seperti *IP address* penyerang & *Hash* malware), serta penjelasan teknis tentang celah kerentanan utama (**Root Cause**) yang dieksploitasi peretas (misalnya celah injeksi SQL di halaman login).
4. **Lessons Learned (Pelajaran dan Rekomendasi):**
   Merupakan langkah terakhir dari siklus PICERL (*'L' / Lessons Learned*). Di sini, tim SOC memberikan rekomendasi evaluasi perbaikan untuk masa depan. (Contoh rekomendasi: *"Tim pengembang web direkomendasikan mengimplementasikan pedoman sanitasi input (Secure Coding) guna meminimalisasi kerentanan SQL Injection pada rilis pembaruan mendatang"*).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi penulisan laporan manajerial (*Executive Summary*)!

1. Siapkan aplikasi catatan (Notepad/VS Code).
2. Skenario: Anda memimpin tim respons insiden pasca penyelesaian kasus pembobolan dokumen HRD akibat serangan *Phishing Email*.
3. **Misi:** CEO membutuhkan laporan cepat. Tuliskan ringkasan *Executive Summary* dalam format narasi bisnis non-teknis tanpa menyebutkan *Hash*, IP Address, atau jargon teknis lainnya!
4. **Draft Laporan Jawaban Analis (Contoh Executive Summary):**
   *"Pada tanggal 25 Mei pukul 09:00 pagi, perusahaan mengalami insiden kompromi keamanan yang diinisiasi melalui serangan pengelabuan surel (Phishing) yang menargetkan staf HRD. Insiden ini berdampak pada tereksposnya 5 (lima) dokumen komunikasi internal perusahaan. Tim keamanan jaringan (SOC) telah berhasil mengambil alih akses, mengamankan seluruh sistem dari intrusi peretas, serta mengonfirmasi bahwa database informasi nasabah korporat tetap aman. Saat ini, seluruh layanan operasional infrastruktur bisnis perusahaan telah direstorasi dan beroperasi kembali 100% dengan normal."*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam format standar Laporan Insiden Siber, bagian apa yang ditempatkan di awal halaman, ditulis menggunakan narasi manajerial tanpa jargon teknis, dan ditargetkan untuk dibaca oleh pimpinan eksekutif (CEO/Direksi)?</summary>

**Jawaban:** Executive Summary (Ringkasan Eksekutif).
</details>

<details>
<summary>❓ Segmen apa dalam Laporan Insiden yang mencatatkan rentetan riwayat kejadian berdasarkan urutan waktu (mulai dari deteksi awal hingga sistem pulih beroperasi)?</summary>

**Jawaban:** Incident Timeline (Kronologi Insiden).
</details>

<details>
<summary>❓ Mengacu pada kerangka siklus respons insiden PICERL, tahap akhir di mana tim melakukan retrospeksi untuk menentukan strategi perbaikan dan pencegahan insiden di masa depan diwakili oleh huruf 'L'. Apa kepanjangan dari 'L' tersebut?</summary>

**Jawaban:** Lessons Learned.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami cara menyusun penyederhanaan terminologi laporan *Executive Summary*.
- [ ] Saya fasih merumuskan urutan kejadian ke dalam format kronologis *Timeline*.
- [ ] Saya mengetahui peran penyusunan audit mitigasi dan rekomendasi *Lessons Learned*.
- [ ] Saya paham bahwa laporan akhir adalah jembatan komunikasi antara tim teknis dan manajemen eksekutif korporat.
- [ ] Saya telah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS: Incident Report Cheat Sheet](https://www.sans.org/white-papers/34520/) — Referensi format struktural acuan penyusunan format Laporan Insiden keamanan siber di industri organisasi korporat.

---

## ➡️ Preview Besok (Tahap Kulminasi Kelulusan!)

**Day 5: Capstone Mission & Graduation** — Perjalanan panjang Anda di kurikulum TISS Null Teaming telah menginjak hari terakhir (Periode pengujian Capstone). Penugasan simulatif dari Hari 1 hingga Hari 4 minggu ini akan dilebur menjadi satu proyek akhir. Misi kelulusan Anda besok berpusat pada perumusan **Laporan Insiden Siber Komprehensif (Full Cyber Incident Report Capstone)** dari kasus eksploitasi web *SQLi*. 

Anda berkesempatan mengintegrasikan proyek portofolio akhir (*Capstone*), membuktikan kapabilitas teknikal Anda secara menyeluruh, dan mengamankan gelar spesialis SOC setingkat **SENTINEL** di penghujung perjalanan yang epik ini!

---

*📅 TISS Null Teaming · Week 24 · Day 4 · SENTINEL Rank*
