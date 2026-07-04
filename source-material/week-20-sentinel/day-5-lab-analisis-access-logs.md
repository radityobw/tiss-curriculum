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

Minggu ini, kita beralih ke area keamanan defensif (Blue Team), memahami fondasi pemantauan serta identifikasi peringatan keamanan:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Pengenalan Blue Team & SOC | Memahami struktur organisasi pemantauan terpusat serta peran Analis SOC (Tier 1-3). |
| Day 2 | Security Events vs Incidents | Mempelajari proses validasi peringatan keamanan (*Triage*) ke dalam *False/True Positives* dan mengklasifikasikan tingkat ancaman. |
| Day 3 | Log Sources & Syslog | Mengenal ragam jenis log (catatan sistem) operasional serta pemahaman protokol *Syslog* untuk sentralisasi pemantauan log. |
| Day 4 | Incident Response Lifecycle | Memahami 6 fase tahapan standar (PICERL) metodologi respons insiden keamanan siber. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Komputer dengan sistem operasi Linux atau WSL (Windows Subsystem for Linux) untuk memudahkan pengelolaan berkas log secara efisien.
- Teks editor standar (seperti VS Code atau Notepad++) guna membaca dan menelaah log.

### Misi Hari Ini: "Analisis Manual Access Log Web Server"

Sebagai penerapan materi *Blue Team* minggu ini, kamu akan berperan sebagai Analis Pemantauan (SOC Analyst). Tugasmu adalah menelaah potongan *Access Logs* dari *Web Server* untuk mendeteksi anomali keamanan (eksploitasi) dan melaporkannya.

### Step 1: Membaca File Rekaman Log
1. Simulasikan insiden: *Web server* perusahaan melaporkan penurunan kinerja (degradasi) dan ada dugaan eksfiltrasi data atau upaya eksploitasi di rute internal.
2. Salin potongan data log *Apache/Nginx* (*Common Log Format*) di bawah ini ke dalam teks editor kamu:

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
1. **Analisis IP Internal:** Periksa 2 baris log pertama dari IP `192.168.1.15`. Klasifikasikan ini sebagai *Security Event* yang wajar (kunjungan normal, merespons kode *200 OK*).
2. **Investigasi Aktivitas Mencurigakan:** Analisis lalu lintas dari IP eksternal `45.33.22.11`. Terdapat percobaan *POST* berturut-turut ke `/login.php` dari pukul `08:15:22` hingga `08:15:27`. Kegagalan (*HTTP 401 Unauthorized*) ini mengindikasikan upaya *Brute Force*. Perhatikan juga pergantian *User-Agent* dari *browser* (`Mozilla/5.0`) menjadi skrip pemrograman otomatis (`python-requests/2.25.1`).
3. **Identifikasi Eksploitasi:** Temukan anomali kritis pada pukul `08:15:27`. Terlihat penggunaan *Payload SQL Injection* (`' OR 1=1--`). Yang paling berbahaya, server merespons serangan injeksi logika kueri ini dengan kode sukses `200 OK`.

### Step 3: Perumusan Kronologi Insiden (Incident Confirmation)
1. Berdasarkan analisis manual, susun kronologi insiden (*Incident Confirmation*).
   - Penyerang (`45.33.22.11`) mencoba *brute force* secara manual lalu beralih menggunakan skrip otomatis (`python-requests`).
   - Penyerang berhasil menembus login menggunakan serangan *SQL Injection Bypass* pada pukul `08:15:27`.
   - Tak lama kemudian (`08:16:01`), penyerang mengakses panel administrator internal (`/admin/dashboard.php`). 
   - Status: Aktivitas ini terkonfirmasi mutlak sebagai eskalasi ancaman (*Security Incident - True Positive*).

---

## 🎯 Weekly Mission

### Misi: "Dokumen Prosedur Operasional Penanganan (SOP Incident Response)"

**Deskripsi:** Identifikasi rute dan bukti peretasan log spesifik sudah dicapai. Sebagai Analis SOC (*Triage Specialist*), kamu harus mendokumentasikan temuan ini ke dalam laporan eskalasi (*Incident Report*). 

**Tugas Mandiri:** Buatlah draf laporan eskalasi peringatan (Incident Report/Triage Summary) berdasarkan analisis log *SQLi Bypass Login* di atas, dan usulkan langkah mitigasi sesuai fase PICERL kepada tim *Engineering/IT*.

**Deliverables:**
1. Buat dokumen dengan format Markdown bertajuk `INCIDENT_RESPONSE_SQLI_LOGS.md`.
2. Dokumen harus memuat dua bagian utama:
   - **Executive Summary:** Berisi catatan insiden (Rentang waktu log kejadian, IP Penyerang, jenis serangan, dan indikator keberhasilan berdasarkan kode status respon HTTP).
   - **Rekomendasi Tindakan (PICERL):** Deskripsikan rekomendasi spesifik untuk fase **Containment** (Langkah isolasi jaringan, misal memblokir IP penyerang di *Firewall*) serta fase **Eradication** (Rekomendasi perbaikan *backend*, misal penerapan *Prepared Statements* untuk menambal celah injeksi SQL).

**Kriteria Sukses:**
- [ ] Tersedia dokumen pelaporan `INCIDENT_RESPONSE_SQLI_LOGS.md`.
- [ ] Terdapat ringkasan yang mencantumkan detail IP pelaku insiden (`45.33.22.11`) dan bukti *payload SQLi*.
- [ ] Mendokumentasikan **Containment** (cara mengisolasi penyerang dengan blokir akses spesifik).
- [ ] Mendokumentasikan **Eradication** (solusi perbaikan teknis seperti validasi input atau *Parameterized Queries*).

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Dalam peran Analis SOC Tier 1, apa sebutan untuk aktivitas memfilter, memvalidasi peringatan (*alerts*), dan menimbang prioritas alarm keamanan untuk menentukan apakah itu ancaman nyata atau bukan?</summary>

**Jawaban:** Triase (Triage).
</details>

<details>
<summary>❓ [MUDAH] Sumber log sistem operasional (*Log Source*) apa yang mencatat detail permintaan web (seperti URL/Endpoint), *User-Agent* peramban, dan kode respon HTTP (seperti 200 OK atau 404 Not Found)?</summary>

**Jawaban:** Web Server Logs (Access Logs dari Apache, Nginx, IIS).
</details>

<details>
<summary>❓ [SEDANG] Jika insiden pencurian data (Data Breach) terjadi namun sensor SOC tidak memberikan notifikasi bahaya sama sekali, dalam klasifikasi keamanan hal ini disebut sebagai apa?</summary>

**Jawaban:** False Negative.
</details>

<details>
<summary>❓ [SEDANG] Pada siklus kerangka kerja *Incident Response* (*PICERL*), tahapan manakah yang secara spesifik bertujuan untuk melakukan isolasi jaringan darurat (memblokir akses sementara) untuk mencegah penyebaran insiden sebelum perbaikan permanen dilakukan?</summary>

**Jawaban:** Fase Containment (Penahanan/Isolasi).
</details>

<details>
<summary>❓ [SULIT] Mengapa fase <i>Lessons Learned</i> (Evaluasi Pasca-Insiden) mutlak diperlukan setelah fase perbaikan sistem (<i>Eradication</i>)?</summary>

**Jawaban:** Fase *Eradication* hanya berfokus untuk membersihkan sistem dan menambal celah teknis yang baru saja dieksploitasi. Tanpa *Lessons Learned*, organisasi tidak akan merefleksikan kelemahan prosedur atau strategi mitigasi secara menyeluruh. Evaluasi ini penting untuk meningkatkan kebijakan keamanan, menyesuaikan prosedur konfigurasi pemantauan (mengubah operasional fase *Preparation*), dan menghindari kesalahan pencegahan yang sama di masa depan.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami struktur organisasi tim pemantauan keamanan (SOC).
- [ ] Saya mampu menjelaskan perbedaan teknis antara *Security Events* dan *Security Incidents*.
- [ ] Saya mengetahui fungsi pengumpulan log (*Log Sources*) dan protokol *Syslog*.
- [ ] Saya menguasai tahapan pemulihan dalam *Incident Response Lifecycle (PICERL)*.
- [ ] Saya mampu menganalisis *Access Log* dan merumuskan dokumen mitigasi `INCIDENT_RESPONSE_SQLI_LOGS.md` pada Weekly Mission.

---

## 💬 Diskusi Minggu Ini

1. Selamat menyelesaikan modul awal pemantauan keamanan (*Blue Team*). Dengan keterampilan menganalisis log dan menyusun prosedur mitigasi (*Containment & Eradication*), bagaimana pendapatmu tentang peran Analis SOC? Apakah tanggung jawab membaca log dan memastikan tidak terjadi *False Negative* sebanding menantangnya dengan tugas *Red Team* yang mencari celah eksploitasi? Diskusikan dengan rekan-rekan analis lainnya!

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│     🛡️ THE FIRST RESPONDER         │
│        Week 20 Complete             │
│      "To attack is human.           │
│      To defend is divine."          │
│                                     │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 21: Log Analysis & Threat Detection**

Pemahaman dasar analisis *Access Logs* secara manual telah kamu kuasai. Namun, dalam lingkungan operasional SOC nyata, sistem organisasi memproses data lalu lintas (*traffic*) dalam skala masif. Minggu depan (Week 21), kita akan mengeksplorasi penggunaan alat *command line interface* (CLI) di Linux seperti *Grep, Awk*, dan *Sed* untuk mencari pola ancaman dari ribuan baris log (*Threat Detection*). Kita juga akan menganalisis log otentikasi Linux (*auth.log*) dan log *Event Viewer* pada sistem Windows. Persiapkan terminal bash-mu!

---

*📅 TISS Null Teaming · Week 20 · Day 5 · SENTINEL Rank*
