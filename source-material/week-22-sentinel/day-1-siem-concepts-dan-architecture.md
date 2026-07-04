# 🛡️ Week 22 · Day 1: SIEM Concepts & Architecture

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 22 · Day 1/5 | SENTINEL Rank (Minggu 3 dari 5) | Overall: 106/120 hari (88%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep dasar dan arsitektur sistem SIEM (Security Information and Event Management).
2. **Menjelaskan** tahapan pemrosesan log: *Collect, Normalize, Correlate, Alert, Store*.
3. **Mengidentifikasi** alasan mengapa perusahaan skala besar (Enterprise) wajib menggunakan SIEM.

---

## 📖 Materi Inti

### Otomatisasi Pemantauan: Pengenalan SIEM

Di laboratorium minggu lalu, kamu memfilter log secara manual menggunakan perintah terminal seperti `awk` dan `grep`. Pendekatan ini tidak mungkin diterapkan di infrastruktur berskala besar yang memiliki ratusan *server*, puluhan *Firewall*, dan ribuan perangkat pengguna (*Endpoint*). Menganalisis file log secara manual satu per satu akan memakan waktu berhari-hari, membuat pendeteksian serangan siber menjadi sangat lambat.

Solusi industri untuk masalah ini adalah **SIEM** (Security Information and Event Management).
SIEM adalah platform terpusat yang secara otomatis mengumpulkan data log dari seluruh perangkat di jaringan, menstandarkan formatnya, mencari korelasi ancaman, dan memicu peringatan otomatis jika ada aktivitas mencurigakan. Contoh platform SIEM komersial yang populer adalah *Splunk, IBM QRadar, Microsoft Sentinel*, dan *ELK Stack*.

### Arsitektur Pemrosesan SIEM (The 5 Pillars)

Sistem SIEM memproses data mentah menjadi informasi intelijen keamanan melalui 5 tahapan utama:

1. **Collect (Pengumpulan):**
   Perangkat lunak agen (*Forwarders*) dipasang di setiap perangkat/server untuk mengumpulkan dan mengirimkan log aktivitas (*Events*) ke *server* pusat SIEM (*Indexer*).
2. **Normalize (Normalisasi/Standarisasi):**
   Setiap jenis sistem memiliki format log yang berbeda (misalnya format log Windows berbeda dengan Apache). SIEM melakukan *Normalisasi*, yaitu mengubah format data yang berbeda-beda tersebut menjadi satu struktur tabel atribut (*Fields*) yang seragam. Contoh: Atribut "IP Pengirim" di Windows dan "Source IP" di Linux akan diseragamkan namanya menjadi `src_ip`.
3. **Correlate (Korelasi):**
   Ini adalah inti analisis dari SIEM. Korelasi adalah proses menghubungkan satu *event* dengan *event* dari sistem lain untuk menemukan indikasi serangan.
   *Contoh:* SIEM mendeteksi rentetan kegagalan autentikasi di *Firewall*, lalu menghubungkannya dengan keberhasilan *login* ke *server* Windows dari IP yang sama satu menit kemudian.
4. **Alert (Peringatan):**
   Jika hasil korelasi terbukti melanggar aturan keamanan (*Rules*) yang dibuat oleh Analis SOC, SIEM akan secara otomatis memicu peringatan (*Alert*) di dasbor pemantauan atau mengirimkan notifikasi.
5. **Store (Penyimpanan Data):**
   SIEM menyimpan kompresi jutaan log secara aman. Penyimpanan jangka panjang (*Retention Policy*) ini penting untuk memenuhi standar regulasi kepatuhan (*Compliance*) dan untuk kebutuhan investigasi/audit forensik di masa mendatang.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari memahami logika korelasi data pada aturan (Rule) SIEM!

1. Anda bertugas membuat aturan pendeteksi *Account Takeover* (Pengambilalihan Akun) di SIEM.
2. **Aturan (Rule) Deteksi:**
   `JIKA (> 10 Kegagalan Login dari IP_X)` **DIIKUTI OLEH** `JIKA (1 Keberhasilan Login dari IP_X dalam waktu < 2 menit)` **MAKA** `Bangkitkan Peringatan`.
3. SIEM menerima log *real-time* berikut dari *server* (Tahap *Collect*):
   `09:00:10 - Failed Login from 10.0.0.1`
   `09:00:11 - Failed Login from 10.0.0.1`
   `(... 12 log kegagalan login lainnya dari IP 10.0.0.1)`
   `09:01:15 - Successful Login from 10.0.0.1`
4. **Evaluasi:** Di fase mana SIEM memproses relasi kejadian log ini dan membangkitkan peringatan?
   *Jawaban:* Pada tahap pemrosesan **Correlate (Korelasi)**. SIEM menghitung bahwa syarat "lebih dari 10 kegagalan lalu diikuti 1 keberhasilan" telah terpenuhi secara bersamaan dalam kurun waktu 1 menit (sesuai aturan < 2 menit), sehingga SIEM melanjutkan proses ke tahap *Alert* untuk memperingatkan SOC.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam lingkup manajemen keamanan perusahaan besar, apa kepanjangan dari SIEM?</summary>

**Jawaban:** Security Information and Event Management.
</details>

<details>
<summary>❓ Dalam arsitektur pemrosesan SIEM, tahap apakah yang bertugas merapikan berbagai format log yang berbeda-beda (misal log *Linux* vs *Windows*) agar memiliki struktur atribut kolom (*Fields*) yang seragam?</summary>

**Jawaban:** Tahap Normalize (Normalisasi/Standarisasi).
</details>

<details>
<summary>❓ Istilah teknis apakah yang digunakan SIEM untuk menjelaskan proses analisis analitik dalam menghubungkan log dari *Firewall* dengan log *Windows* untuk merumuskan satu insiden ancaman?</summary>

**Jawaban:** Correlate (Korelasi).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami mengapa metode log analisis manual tidak cocok untuk *Enterprise* besar.
- [ ] Saya mampu menjelaskan 5 tahapan pemrosesan SIEM: *Collect, Normalize, Correlate, Alert, Store*.
- [ ] Saya mengerti bagaimana logika *Correlate* bekerja menggunakan *Rules*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Varonis: What is SIEM?](https://www.varonis.com/blog/what-is-siem) — Pengenalan arsitektur dan kapabilitas fundamental penerapan SIEM di industri.

---

## ➡️ Besok

**Day 2: Splunk Basics** — Mengetahui konsep teori SIEM belum cukup untuk operasi teknikal harian. Besok, kita akan membahas cara berinteraksi langsung dengan salah satu platform SIEM terkemuka di industri, yakni **Splunk**. Kamu akan belajar mencari, memfilter, dan mengolah data keamanan berskala raksasa menggunakan bahasa kueri khusus: **SPL (Search Processing Language)**.

---

*📅 TISS Null Teaming · Week 22 · Day 1 · SENTINEL Rank*
