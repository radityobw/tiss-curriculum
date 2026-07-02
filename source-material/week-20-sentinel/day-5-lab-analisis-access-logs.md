# 🛡️ Week 20 · Day 5: Lab & Weekly Mission Analisis Access Logs

> **Rank**: SENTINEL | **Minggu ke-20**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓░░░░░░░░] 20% — SENTINEL Rank (Minggu 1 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░] 83% — Hari 100 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → ✅ BREACH → 🔄 SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini, kita beralih ke area pertahanan defensif, memahami fondasi pemantauan (Blue Team) serta identifikasi peringatan keamanan:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Pengenalan Blue Team & SOC | Deskripsi struktural organisasi keamanan terpusat serta deskripsi peran Analis SOC (Tier 1-3). |
| Day 2 | Security Events vs Incidents | Proses validasi peringatan keamanan (Triage) ke dalam definisi *False/True Positives* dan klasifikasi tingkat ancamannya. |
| Day 3 | Log Sources & Syslog | Definisi ragam jenis rekam jejak aktivitas operasional serta mekanika protokol *Syslog* untuk sentralisasi arsip sistem (Logs). |
| Day 4 | Incident Response Lifecycle | 6 fase tahapan standar (PICERL) metodologi respons ancaman (Persiapan, Deteksi, hingga Restorasi Evaluatif). |

---

## 🧪 Hands-On Lab

### Prerequisites
- Komputer dengan sistem operasi Linux atau WSL (Windows Subsystem for Linux) untuk memudahkan pengelolaan berkas log secara efisien.
- Teks editor standar industri (seperti Visual Studio Code atau Notepad++) guna melakukan audit konten rekam jejak.

### Misi Hari Ini: "Analisis Manual Access Log Web Server"

Sebagai ujian penerapan ilmu pemantauan sistem, pada sesi kali ini Anda akan berperan selaku Analis Pemantauan (SOC Analyst) untuk menelaah serangkaian dataset *Web Server Access Logs* statis guna mendeteksi aktivitas eksploitasi anomali dan melaporkannya.

### Step 1: Merengkuh File Rekaman Log
1. Simulasikan insiden di mana operasional situs peladen web mendapati degradasi dan laporan potensi eksfiltrasi rute internal.
2. Periksa sampel potongan data log akses peladen web Apache (format Common Log) di bawah ini ke dalam antarmuka teks editor:

```text
192.168.1.15 - - [10/Oct/2026:08:14:02 +0700] "GET /index.php HTTP/1.1" 200 4523 "-" "Mozilla/5.0"
192.168.1.15 - - [10/Oct/2026:08:14:05 +0700] "GET /assets/style.css HTTP/1.1" 200 1200 "-" "Mozilla/5.0"
45.33.22.11 - - [10/Oct/2026:08:15:20 +0700] "GET /login.php HTTP/1.1" 200 3214 "-" "Mozilla/5.0"
45.33.22.11 - - [10/Oct/2026:08:15:22 +0700] "POST /login.php HTTP/1.1" 401 230 "-" "Mozilla/5.0"
45.33.22.11 - - [10/Oct/2026:08:15:25 +0700] "POST /login.php HTTP/1.1" 401 230 "-" "Mozilla/5.0"
45.33.22.11 - - [10/Oct/2026:08:15:26 +0700] "POST /login.php HTTP/1.1" 401 230 "-" "python-requests/2.25.1"
45.33.22.11 - - [10/Oct/2026:08:15:27 +0700] "POST /login.php HTTP/1.1" 401 230 "-" "python-requests/2.25.1"
45.33.22.11 - - [10/Oct/2026:08:15:27 +0700] "POST /login.php?user=admin' OR 1=1-- HTTP/1.1" 200 4520 "-" "python-requests/2.25.1"
45.33.22.11 - - [10/Oct/2026:08:16:01 +0700] "GET /admin/dashboard.php HTTP/1.1" 200 8920 "-" "Mozilla/5.0"
```

### Step 2: Triase Manual (Mendeteksi Anomali)
1. Periksa 2 baris log permulaan terkait rute IP `192.168.1.15`. Klasifikasikan rute tersebut sebagai rutinitas kunjungan operasional standar (*Security Event*, status resolusi *200*).
2. Investigasi lalu lintas terkait alamat IP sumber `45.33.22.11`. Analisis rangkaian percobaan metode protokol POST menuju *endpoint* autentikasi (`/login.php`) antara interval cap waktu `08:15:22` hingga `08:15:27`. Rentetan kegagalan status HTTP *401 Unauthorized* tersebut mengindikasikan serangan percobaan *Brute Force*. Perhatikan juga pergantian nilai identitas HTTP `User-Agent` dari peramban (`Mozilla/5.0`) menjadi identifikasi perpustakaan pemrograman otomatis (`python-requests/2.25.1`).
3. Temukan baris anomali kritikal tepat di detik waktu log pukul `08:15:27`. Terdapat parameter *Payload SQL Injection* (SQLi) yakni `' OR 1=1--`. Rute aplikasi merespon kueri berbahaya ini dengan kode otentikasi `200 OK`.

### Step 3: Perumusan Kronologi Insiden (Incident Confirmation)
1. Berdasarkan pengamatan anomali manual, tetapkan kronologi peretasan. Penyerang mendemonstrasikan eksploitasi di titik awal (`/login.php`). Kegagalan login iteratif di awal memicu penyerang menggunakan skrip peretasan dinamis (`python-requests`), menjejalkan bypass manipulasi logika kueri *SQLi* dan mendapatkan hak akses autentikasi internal yang memungkinkannya mengontrol aplikasi internal (`/admin/dashboard.php`). Status tersebut terklasifikasikan mutlak menjadi eskalasi ancaman (*Security Incident - True Positive*).

---

## 🎯 Weekly Mission

### Misi: "Dokumen Prosedur Operasional Penanganan (SOP Incident Response)"

**Deskripsi:** Identifikasi rute dan bukti peretasan log spesifik sudah dicapai. Sebagai Analis SOC (Triage), operasionalisasi mitigasi krisis tidak dapat dieksekusi tanpa dokumen operasional respon darurat (SOP). 

**Tugas Mandiri:** Konversi rumusan observasi dari fase analisis laboratorium (*Hands-On Lab: SQLi Bypass Login*) menjadi sebuah laporan eskalasi peringatan (Incident Report/Triage Summary) sekaligus mengusulkan rumusan pedoman fase taktis (*PICERL*) bagi teknisi infrastruktur TI.

**Deliverables:**
1. Dokumen format *Markdown* bertajuk `INCIDENT_RESPONSE_SQLI_LOGS.md`.
2. Delineasi dua sesi bagian mitigasi insiden utama:
 - **Executive Summary:** Berisi catatan insiden (Rentang temporal log kejadian, IP Penyerang/Sumber, metodologi eksploitasi spesifik, dan indikator keberhasilan log kode status respon HTTP).
 - **Rekomendasi Tindakan (PICERL):** Deskripsi implementasi rekomendasi spesifik pada prosedur siklus: **Containment** (Langkah pembatasan rute akses anomali secara segera di tingkat parameter *Firewall*/jaringan) serta fase **Eradication** (Rekomendasi tindakan guna mitigasi dasar pada parameter pengkodean *backend* yang rentan).

**Kriteria Sukses:**
- [ ] Repositori mencantumkan berkas laporan `INCIDENT_RESPONSE_SQLI_LOGS.md`.
- [ ] Ringkasan berisi rincian IP pelaku insiden (`45.33.22.11`) beserta metadata bukti muatan bypass kueri SQL.
- [ ] Dokumentasi **Containment** menyuguhkan metodologi pencegatan akses spesifik tingkat isolasi IP.
- [ ] Dokumentasi **Eradication** memuat solusi teknikal arsitektur perbaikan operasional kode (seperti penerapan parameter validasi *Input* atau *Prepared Statements*).

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Dalam struktur SOC Analyst Tier 1, istilah teknikal untuk mendeskripsikan aktivitas menyaring, memvalidasi peringatan (*alerts*), dan menimbang prioritas alarm keamanan untuk menetapkan kategori ancaman disebut sebagai proses apa?</summary>

**Jawaban:** Triase (Triage).
</details>

<details>
<summary>❓ [MUDAH] Sumber log sistem operasional apa yang menyediakan informasi pergerakan pengunjung (HTTP Requests) beserta rincian informasi parameter *User-Agent* dan rekam jejak respon operasional peladen web?</summary>

**Jawaban:** Web Server Logs (Access Logs, misalnya Apache/Nginx Logs).
</details>

<details>
<summary>❓ [SEDANG] Sebuah peristiwa esfiltrasi basis data (Data Breach) terlaksana secara sukses, namun sistem sensor peringatan tidak membunyikan alarm karena tidak mampu mengidentifikasi muatan peretasan (*payload*). Kesalahan sistematis deteksi sensor SOC tersebut diklasifikasikan sebagai kejadian apa?</summary>

**Jawaban:** False Negative.
</details>

<details>
<summary>❓ [SEDANG] Pada alur implementasi kerangka pedoman siklus *Incident Response* (*PICERL*), tahapan apa yang spesifik didelegasikan untuk mengaktifkan kebijakan pemutusan transmisi jaringan peladen atau segregasi/isolasi perangkat TI yang mengalami malfungsi dalam rangka mencegah perluasan jangkauan penyerangan?</summary>

**Jawaban:** Fase Containment (Penahanan/Isolasi).
</details>

<details>
<summary>❓ [SULIT] Jelaskan objektivitas perlunya siklus tahapan <i>Lessons Learned</i> pasca eksekusi pemulihan <i>Eradication</i>. Mengapa aktivitas penutupan lubang akses dan pembersihan perangkat eksploitasi teknis dinilai inefektif apabila tidak melalui evaluasi retrospektif <i>Lessons Learned</i>?</summary>

**Jawaban:** Fase remediasi taktis (*Eradication*) terpusat pada menanggulangi titik celah yang telah terinfeksi insiden. Tanpa dilakukan fase analitikal *Lessons Learned*, organisasi takkan merealisasikan pemicu struktural dan defisiensi organisasi, misalnya tidak adanya validasi proses arsitektur kueri *backend*. Evaluasi retrospektif ini krusial demi merumuskan kerangka panduan mitigasi komprehensif, mengeskalasi kapasitas personil operasional (pelatihan teknis arsitektur kode perlindungan berprinsip *Secure SDLC*), hingga modifikasi SOP operasional fase *Preparation* berikutnya sehingga insiden bermetodologi yang setara takkan mendisrupsi TI operasional di kemudian hari.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami struktur hierarkis organisasi pelindung keamanan (SOC).
- [ ] Saya mampu mendeskripsikan kerangka parameter evaluatif perbedaan operasional kategori *Events* dan *Incidents*.
- [ ] Saya mengenali signifikansi penerapan arsip *Syslog* pada visibilitas infrastruktur sentral *Log Sources*.
- [ ] Saya menguasai pendefinisian langkah pemulihan operasional *Incident Response Lifecycle (PICERL)*.
- [ ] Saya mampu merumuskan dokumentasi analitis mitigasi `INCIDENT_RESPONSE_SQLI_LOGS.md` (Weekly Mission).

---

## 💬 Diskusi Minggu Ini

1. Selamat menyelesaikan modul awal fase pemantauan keamanan (*Blue Team*). Dengan kapabilitas analitis serta perumusan dokumen mitigasi operasional respons *Containment* minggu ini, apakah perbedaan kompleksitas tanggung jawab *SOC Analyst* yang harus menganalisis data log mentah dan mempertanggungjawabkan pemantauan infrastruktur guna meminimalisasi insiden klasifikasi *False Negative* sebanding dengan kerumitan yang ditanggung *Red Team* di minggu-minggu eksploitasi? Kemukakan pandangan teknis operasionalnya!

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🛡️ THE FIRST RESPONDER │
│ Week 20 Complete │
│ "To attack is human. │
│ To defend is divine." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 21: Log Analysis & Threat Detection**

Pemahaman pembacaan kerangka log web telah Anda kuasai. Namun, pada ekosistem operasional sesungguhnya, infrastruktur organisasi menyuguhkan *traffic* yang heterogen dan masif. Pada modul selanjutnya di Week 21, kita akan mengeksplorasi ekstraksi baris perintah terminal (CLI) seperti *Grep*, *Awk*, dan *Sed* guna melakukan pencarian pola log otomatis (Threat Detection) yang meliputi analisis berkas keamanan *Linux* (Auth.log) maupun penelaahan aktivitas pengguna melalui antarmuka *Event Viewer* ekosistem sistem operasi. Persiapkan investigasi terminal Anda!

> 🚀 *"The truth is always in the logs. You just need to know how to read them."*

---

*📅 TISS Null Teaming · Week 20 · Day 5 · SENTINEL Rank*
