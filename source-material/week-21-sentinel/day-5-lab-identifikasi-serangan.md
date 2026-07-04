# 🛡️ Week 21 · Day 5: Lab & Weekly Mission Identifikasi Serangan

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓░░░░░░] 40% — SENTINEL Rank (Minggu 2 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░] 88% — Hari 105 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → ✅ BREACH → 🔄 SENTINEL

---

## 📝 Rekap Minggu Ini

Modul minggu ini berfokus pada kapabilitas deteksi ancaman dan pembacaan log sistem:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Apache/Nginx Log Format | Membedah 7 atribut akses web (IP, Timestamp, Method, URI, Status Code, Size, User-Agent) dari format standar *Combined*. |
| Day 2 | Windows Event Logs | Analisis identifikasi kunci sistem operasi (Event ID 4624 Logon, 4625 Failed, 7045 Service Creation) untuk audit keamanan. |
| Day 3 | Linux Logs & Journalctl | Analisis penempatan repositori log sentral di Linux (`/var/log/auth.log`) dan pemanfaatan perintah kueri modern `journalctl`. |
| Day 4 | Pattern Recognition | Mengenali indikasi ancaman siber melalui pola repetitif (*Brute Force*, *Vulnerability Scanning*) dan *Data Exfiltration*. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Komputer dengan sistem operasi Linux atau WSL (Windows Subsystem for Linux).
- Pemahaman dasar terminal CLI untuk pengolahan teks (`grep`, `awk`, `sort`, `uniq`, `head`).

### Misi Hari Ini: "Audit Investigasi Log Sentral (Log Analysis Data Processing)"

Praktikum kali ini tidak menggunakan log ringkas, melainkan menuntut Anda menggunakan terminal untuk mengekstrak informasi dari puluhan ribu baris log web server mentah (`access.log`).

### Step 1: Ekstraksi IP Penyerang (Top Talkers Extraction)
1. Buka terminal Linux/WSL. Asumsikan Anda memiliki *dataset* bernama `access.log`.
2. Langkah awal investigasi adalah mencari IP mana yang paling mendominasi permintaan (*Most frequent request IPs / Top Talkers*). Kita akan menggunakan teknik *Piping* (`|`):
   `awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 5`
3. *Penjelasan Perintah:* 
   - `awk '{print $1}'`: Mengambil hanya kolom pertama (Alamat IP).
   - `sort`: Mengurutkan teks agar IP yang sama berdekatan.
   - `uniq -c`: Menghitung frekuensi kemunculan setiap IP.
   - `sort -nr`: Mengurutkan hasil perhitungan dari yang terbesar ke terkecil (*numeric reverse*).
   - `head -n 5`: Menampilkan hanya 5 IP teratas.
4. *Hasil (Output):* Terminal melaporkan bahwa `IP 10.10.55.5` mendominasi dengan lebih dari 15.000 *Requests*. Ini adalah indikator awal serangan.

### Step 2: Menyelidiki Pola Serangan (Filtrasi Spesifik)
1. Berdasarkan temuan di atas, IP penyerang diduga adalah `10.10.55.5`.
2. Buat *file* baru khusus untuk log dari IP tersebut agar lebih mudah dianalisis:
   `grep "10.10.55.5" access.log > hacker_log.txt`
3. Cari tahu apakah ini merupakan serangan pemindaian direktori (*Directory Enumeration/Vulnerability Scanning*) dengan menghitung jumlah status kode `404 Not Found`:
   `grep "404" hacker_log.txt | wc -l`
   *(Hasil Hipotetis: 14.500 baris)*. 
   **Kesimpulan:** Penyerang melakukan eksploitasi pencarian kerentanan web.

### Step 3: Mencari Titik Kebobolan (Identifikasi Insiden / True Positive)
1. Setelah peretas memindai kueri secara sistematis dan mendapatkan error 404, apakah mereka berhasil menemukan halaman admin yang sah?
2. Ekstrak rekaman yang memiliki status sukses (`200 OK`) dari *file* penyerang tersebut:
   `grep " 200 " hacker_log.txt`
3. *Simpulan Analisis:* Terminal menampilkan rekaman `GET /admin_dashboard.php` dengan status `200`. 
   **Kesimpulan Triage:** Sistem telah berhasil dibobol (*True Positive*). Pelaku berhasil menemukan dan mengakses halaman administrasi rahasia.

---

## 🎯 Weekly Mission

### Misi: "Laporan Perburuan Insiden Siber (Threat Hunting Report)"

**Deskripsi:** Memanfaatkan keahlian teknikal seperti kombinasi perintah `awk` dan `grep` di Linux sudah kamu kuasai. Tanggung jawab tingkat pelaksana Analis SOC juga mencakup dokumentasi analisis forensik untuk diserahkan ke tingkat manajemen.

**Tugas Mandiri:** Berdasarkan pemahaman investigasi log di atas, susunlah draf pelaporan ringkas hasil perburuan jejak (*Summary Report Threat Hunting*).

**Deliverables:**
1. Hasilkan laporan dalam format *Markdown* dengan nama *file* `THREAT_HUNT_LOGS.md`.
2. Struktur dokumen wajib mencakup komponen berikut:
   - **Tipe Analitik Serangan:** (Contoh: Vulnerability Scanning, Directory Enumeration).
   - **IP Pelaku & Rekam Cap Waktu (Timestamp):** (Kapan serangan mulai memuncak).
   - **Bukti Log Mentah (Raw Log Evidence):** (Lampirkan *copy-paste* baris log asli yang membuktikan serangan sukses).
   - **Komentar Analisis Forensik (Threat Analyst Rationale):** (Jelaskan secara ringkas mengapa barisan log tersebut dinyatakan sebagai insiden *True Positive*).

**Kriteria Sukses:**
- [ ] Berhasil membuat *file* laporan `THREAT_HUNT_LOGS.md`.
- [ ] Dokumen memuat 4 struktur pelaporan forensik dengan jelas.
- [ ] Menyertakan komando Linux (seperti *grep/awk/uniq*) yang digunakan untuk menarik kesimpulan investigasi.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Perintah dasar Linux apa yang sering digunakan SOC Analyst untuk mengambil data kolom pertama saja (misal: kolom IP address) dari sebuah file log yang panjang?</summary>

**Jawaban:** perintah `awk` (contoh penggunaan: `awk '{print $1}'`).
</details>

<details>
<summary>❓ [MUDAH] Perintah dasar Linux apa yang digunakan untuk memfilter dan hanya mencetak baris log yang mengandung kata/karakter tertentu (contoh: hanya menampilkan baris yang memiliki string "404")?</summary>

**Jawaban:** Perintah `grep`.
</details>

<details>
<summary>❓ [SEDANG] Berdasarkan praktik <i>Pattern Recognition</i>, jika Analis mendapati ratusan log <i>HTTP 401 Unauthorized</i> yang mengincar rute `/login.php` dari satu IP secara cepat, dan tiba-tiba diakhiri dengan satu log <i>200 OK</i> dari IP yang sama, apa kesimpulannya?</summary>

**Jawaban:** Keberhasilan serangan *Brute Force*. Indikator *200 OK* membuktikan bahwa peretas akhirnya sukses menebak kata sandi yang valid setelah serangkaian percobaan gagal.
</details>

<details>
<summary>❓ [SEDANG] Dalam hierarki teknik <i>Piping</i> Linux, perintah lanjutan apa yang wajib dijalankan bersamaan setelah perintah pengurutan (`sort`) jika kita ingin menghapus baris duplikat sekaligus menghitung jumlah frekuensi kemunculannya?</summary>

**Jawaban:** Instruksi `uniq` (khususnya dengan argumen hitung: `uniq -c`).
</details>

<details>
<summary>❓ [SULIT] Dalam ranah <i>Big Data Log Monitoring</i>, mengapa Analis SOC lebih disarankan menggunakan teknik rantai <i>Piping</i> Linux CLI (menggunakan karakter `|`) untuk memproses file log berukuran 10 GB dibandingkan membukanya di Text Editor grafis konvensional (seperti Notepad/Sublime Text)?</summary>

**Jawaban:** Membuka *file* log 10 GB di *Text Editor* GUI akan memaksa sistem operasi memuat keseluruhan *file* tersebut ke dalam *RAM*. Ini sangat menguras sumber daya *server* dan bisa memicu sistem *crash/hang* (kehabisan memori). Sebaliknya, teknik *Piping* pada CLI Linux (*Streaming Data Pipeline*) mengeksekusi data baris per baris secara berurutan, sehingga penggunaan *RAM* tetap kecil dan stabil tanpa membebani sistem secara keseluruhan.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami penggunaan *utilities* ekstraktif Linux seperti `awk` dan `grep`.
- [ ] Saya sukses mempraktikkan penggabungan komando berantai (teknik *Piping*) untuk memproses data log berukuran besar.
- [ ] Saya mengerti cara mengidentifikasi IP penyerang dominan (*Top Talkers*) dari file log.
- [ ] Saya mampu mendeteksi indikasi log `200 OK` yang merepresentasikan peretasan berhasil.
- [ ] Saya mampu menghimpun dan menulis draf *Threat Hunting Report*.

---

## 💬 Diskusi Minggu Ini

1. Anda telah belajar cara menganalisis *Access Logs*, meninjau OS log (Windows *Event ID* dan Linux *journalctl*), hingga memfilter teks manual dengan Linux CLI (`grep/awk/uniq`). Dari sudut pandang seorang Analis, menurut Anda, kapan analisis teks *Command Line* manual sangat berguna dan kapan perusahaan sebaiknya berinvestasi menggunakan sistem dasbor log grafis interaktif (seperti *SIEM*)? Diskusikan pro dan kontra dari metode analisis manual CLI vs dasbor log interaktif!

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│     👁️ THE PATTERN SEEKER          │
│       Week 21 Complete              │
│      "Numbers don't lie.            │
│  They just hide in plain sight."    │
│                                     │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 22: SIEM & Monitoring Tools**

Kemampuan melakukan perburuan log secara manual (*parsing* dengan `grep/awk`) adalah *skill* bertahan hidup yang fundamental. Namun, dalam lingkungan *Enterprise* kelas dunia yang memproses ratusan Gigabyte data per hari, metode manual semata tidaklah efisien. 

Minggu depan, kita akan masuk ke pengenalan sistem *Security Information and Event Management* (SIEM). Di Week 22, kamu akan belajar mengoperasikan dasbor **Splunk**, menguasai Search Processing Language (SPL), mempelajari modifikasi visualisasi peringatan keamanan, dan memahami perlindungan otomatis dari arsitektur *Intrusion Detection Systems* (seperti Suricata & Snort).

> 🚀 *"Manual parsing is for the trenches. Splunk is the command center."*

---

*📅 TISS Null Teaming · Week 21 · Day 5 · SENTINEL Rank*
