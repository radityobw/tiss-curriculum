# 🛡️ Week 22 · Day 1: SIEM Concepts & Architecture

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 22 · Day 1/5 | SENTINEL Rank (Minggu 3 dari 5) | Overall: 106/120 hari (88%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** definisi dan arsitektur dasar sistem SIEM (Security Information and Event Management).
2. **Menjelaskan** tahapan pemrosesan data log: *Collect, Normalize, Correlate, Alert, Store*.
3. **Mengidentifikasi** alasan mengapa korporasi berskala besar wajib menggunakan SIEM.

---

## 📖 Materi Inti

### Otomatisasi Pemantauan: Pengenalan SIEM

Di laboratorium minggu lalu, kamu menganalisis riwayat log secara manual menggunakan terminal seperti `awk` dan `grep`. Pendekatan ini tidak dapat diterapkan di infrastruktur korporat berskala besar yang mungkin memiliki 500 server *Windows*, 200 server *Linux*, 50 *Firewall*, dan ribuan komputer staf (Endpoint). Melakukan penyaringan file log secara manual satu per satu akan memakan waktu berhari-hari, membuat sistem tidak responsif terhadap ancaman siber aktual.

Untuk menyelesaikan masalah pemantauan dalam skala besar ini, industri menggunakan **SIEM** (Security Information and Event Management).
SIEM adalah platform terpusat yang mengumpulkan log data dari seluruh perangkat di jaringan, menstandarkannya, melakukan analisis berkorelasi, dan membangkitkan peringatan otomatis ketika mendeteksi anomali keamanan. Contoh platform SIEM komersial yang populer adalah *Splunk, IBM QRadar, Microsoft Sentinel*, dan *ELK Stack*.

### Arsitektur Pemrosesan SIEM (The 5 Pillars)

Sistem SIEM memproses data mentah menjadi intelijen keamanan melalui 5 tahapan arsitektur utama:

1. **Collect (Pengumpulan):**
 Agen perangkat lunak (*Forwarders*) dipasang di setiap peladen untuk menyalin dan meneruskan catatan aktivitas (Events) ke peladen pusat (*SIEM Indexer*).
2. **Normalize (Normalisasi/Standarisasi):**
 Setiap sistem memiliki format log yang berbeda (misalnya log OS Windows berbeda dengan log Apache). SIEM melakukan *normalisasi* dengan mengonversi berbagai format mentah tersebut menjadi satu struktur tabel atribut (*Fields*) yang seragam. Contoh: Kolom "IP Pengirim" di Windows dan "Source IP" di Linux akan diseragamkan dengan parameter atribut baku `src_ip`.
3. **Correlate (Korelasi):**
 Ini adalah fungsi analitikal inti dari SIEM. Korelasi merupakan proses logis untuk mengaitkan satu rekaman peristiwa dengan peristiwa di sistem lain.
 *Contoh:* SIEM menautkan rentetan kegagalan autentikasi di perangkat Firewall dengan indikasi keberhasilan masuk sistem di log Windows yang terjadi beberapa menit kemudian dari alamat IP asal yang sama, merumuskan indikator serangan.
4. **Alert (Peringatan):**
 Jika hasil korelasi peristiwa telah melampaui aturan deteksi (Rules/Threshold) yang dikonfigurasi Analis SOC, SIEM akan memicu peringatan otomatis (Alert) berupa dasbor peringatan atau notifikasi pesan.
5. **Store (Penyimpanan Data):**
 SIEM mengarsipkan kompresi jutaan data log. Penyimpanan jangka panjang ini krusial untuk memenuhi standar kepatuhan regulasi industri (Compliance) dan audit investigasi forensik di masa mendatang (Retention Policy).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari membedah logika algoritma korelasi di SIEM!

1. Posisikan dirimu sebagai arsitek pengaturan aturan korelasi (Rule). Kamu mendefinisikan kriteria aturan pendeteksi "Account Takeover" (Pengambilalihan Akun).
2. **Aturan (Rule) Deteksi SOC:**
 `JIKA (Terjadi > 10 Kegagalan Autentikasi dari IP_X)` **DIIKUTI OLEH** `JIKA (Terjadi 1 Keberhasilan Autentikasi dari IP_X dalam rentang < 2 menit)` **MAKA** `Bangkitkan Peringatan Kritis (Alert)`.
3. Sistem mendata masukan log dari peladen (Tahap *Collect*):
 `09:00:10 - Failed Login from 10.0.0.1`
 `09:00:11 - Failed Login from 10.0.0.1`
 `(... 12 baris kegagalan login lainnya dari IP 10.0.0.1)`
 `09:01:15 - Successful Login from 10.0.0.1`
4. Di fase mana SIEM membedah relasi kronologis log ini dan memicu respon peringatan?
 *Jawaban:* Pada tahap pemrosesan **Correlate (Korelasi)**. SIEM menghitung bahwa pra-syarat lebih dari 10 kegagalan yang diakhiri 1 keberhasilan telah terpenuhi secara simultan dalam kurun waktu 1 menit (sesuai aturan < 2 menit), sehingga peringatan berhasil diinisiasi.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membahas standar sistem manajemen otomasi SOC di perusahaan besar, apa kepanjangan teknis dari sistem agregasi data log korporat bernama SIEM?</summary>

**Jawaban:** Security Information and Event Management.
</details>

<details>
<summary>❓ Dalam tahapan siklus arsitektur operasional peladen SIEM, pada tahapan apakah SIEM mengolah dan merapikan ragam struktur metadata log kotor (misal dari *Linux* vs *Windows*) menjadi format struktur data (*Fields*) yang konsisten?</summary>

**Jawaban:** Tahap Normalize (Normalisasi/Standarisasi).
</details>

<details>
<summary>❓ Pada arsitektur mesin SIEM, istilah teknis apakah yang merujuk pada proses analisis sistem dalam menyatukan dan menghubungkan rangkaian rekaman log dari satu perangkat (seperti Firewall) dengan log perangkat lain (seperti Windows) ke dalam satu kronologi analisis indikator serangan?</summary>

**Jawaban:** Correlate (Korelasi Insiden).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami keterbatasan log analisis manual dibandingkan arsitektur *SIEM*.
- [ ] Saya fasih membedakan fungsi tahapan pemrosesan SIEM: *Collect, Normalize, Correlate*.
- [ ] Saya mengerti fungsionalitas otomasi dari korelasi sistem berantai.
- [ ] Saya memahami kepatuhan penyimpanan data jangka panjang melalui tahapan *Store*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Varonis: What is SIEM?](https://www.varonis.com/blog/what-is-siem) — Pengenalan arsitektur dan kapabilitas fundamental penerapan SIEM di skala industri.

---

## ➡️ Besok

**Day 2: Splunk Basics** — Mengetahui teori konsep SIEM saja belum mencukupi standar teknis operasional analis. Esok hari, kita akan membahas interaksi teknikal operasional dari platform SIEM terkemuka di industri, yakni **Splunk**. Kamu akan belajar memanipulasi pengolahan data agregat berkapasitas besar memanfaatkan fungsi bahasa kuerinya: **SPL (Search Processing Language)**.

---

*📅 TISS Null Teaming · Week 22 · Day 1 · SENTINEL Rank*
