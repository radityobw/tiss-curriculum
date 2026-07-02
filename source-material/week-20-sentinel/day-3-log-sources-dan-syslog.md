# 🛡️ Week 20 · Day 3: Log Sources & Syslog

> **Rank**: SENTINEL | **Minggu ke-20**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 20 · Day 3/5 | SENTINEL Rank (Minggu 1 dari 5) | Overall: 98/120 hari (82%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** fungsi log (catatan aktivitas sistem) sebagai komponen dasar visibilitas *Blue Team*.
2. **Mengidentifikasi** tipe-tipe sumber log sistem dan perangkat keamanan (*Log Sources*).
3. **Menjelaskan** konsep pemusatan data aktivitas jaringan menggunakan protokol pengiriman *Syslog*.

---

## 📖 Materi Inti

### Rekam Jejak Visibilitas: Pentingnya Logs

Untuk merespons ancaman, tim analis harus memiliki visibilitas atas semua interaksi data di dalam jaringan dan infrastruktur. **Log** (catatan rekam jejak) adalah kumpulan entri baris teks atau data terstruktur yang mendokumentasikan kejadian operasional atau parameter keamanan dalam sistem komputer.

Log merekam metadata mendetail tentang setiap aktivitas, meliputi identitas pengguna, cap waktu (timestamp), asal alamat IP, tujuan rute eksekusi, serta tingkat status eksekusi. Analisis log merupakan wajib (mandatory) dalam setiap proses deteksi ancaman dan investigasi forensik.

### Kategori Sumber Log (Log Sources)

Infrastruktur teknologi modern menghasilkan log dari ribuan sumber secara terus-menerus. Berikut ini beberapa klasifikasi jenis sumber log:

1. **Web Server Logs:**
 Mencatat seluruh lalu lintas permintaan *HTTP/HTTPS* (Access Logs) dan ralat internal (Error Logs) yang dihasilkan dari platform peladen web (seperti Apache, Nginx, IIS). Parameter penting termasuk IP klien, Uniform Resource Identifier (URI) yang diakses, Status Code, dan User-Agent. Sumber log ini digunakan untuk deteksi ancaman seperti Injeksi SQL atau *Cross-Site Scripting*.
2. **Operating System (OS) Logs:**
 Dicatat oleh sistem kernel maupun *daemon* tingkat OS. Pada Windows, log dikelola di dalam *Event Viewer*, sedangkan di sistem Linux, arsip log dapat dijumpai pada `/var/log` (contoh: syslog, auth.log). Log OS vital untuk memverifikasi autentikasi login pengguna, perubahan konfigurasi administrator, atau inisiasi *service* anomali.
3. **Application Logs:**
 Kumpulan aktivitas spesifik yang dicatat oleh perangkat lunak layanan independen, misalnya sistem *database* relasional, proksi server, atau perangkat lunak perusahaan.
4. **Network & Security Logs:**
 Data yang diproduksi perangkat jaringan dan alat keamanan (seperti Router, Switch, Firewall, IDS/IPS). Berisikan rekaman terkait penerimaan atau penolakan koneksi lalu lintas jaringan, alamat port sumber/tujuan, dan blokir sesi TCP.

### Sentralisasi Log dengan Protokol Syslog

Mengakses ribuan file log pada setiap host secara manual merupakan hal yang mustahil secara operasional. Oleh karenanya, log perlu dipusatkan dalam satu server (Log Management Server atau SIEM). 

Standar protokol pengiriman log yang paling luas digunakan adalah **Syslog**. 
Syslog menggunakan standar pemformatan pesan khusus dan pada implementasi klasiknya berjalan melalui port transport jaringan UDP 514, untuk mengirim pesan log kejadian secara instan dari puluhan host *(clients)* ke satu repositori pemantauan pusat *(Syslog Server)*. Dengan sentralisasi ini, tim keamanan dapat memvalidasi log dari seluruh infrastruktur di satu panel dasbor.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melakukan analisis rincian struktur log akses aplikasi web.

1. Perhatikan sampel (snippet) data akses web server berformat Nginx/Apache standar berikut ini:
 `192.168.1.50 - - [15/May/2026:10:15:20 +0700] "GET /admin/dashboard.php HTTP/1.1" 200 4523 "-" "Mozilla/5.0"`
 `10.0.0.99 - - [15/May/2026:10:16:01 +0700] "GET /produk.php?id=1' OR 1=1-- HTTP/1.1" 403 120 "-" "sqlmap/1.4.2"`

2. **Analisis Ekstraksi Baris Pertama (Lalu Lintas Rutin):** 
 - IP Klien Sumber: `192.168.1.50`
 - Cap Waktu: `15/May/2026 10:15:20`
 - Metode & Titik Akhir: `GET /admin/dashboard.php`
 - Kode Status: `200` (Permintaan berhasil).

3. **Analisis Ekstraksi Baris Kedua (Indikasi Keamanan):**
 - IP Klien Sumber: `10.0.0.99`
 - Metode & Titik Akhir: Permintaan kueri ini mengindikasikan struktur muatan (payload) ancaman injeksi SQL dengan parameter `' OR 1=1--`.
 - Kode Status: `403` (Proses permintaan berhasil diblokir/Forbidden, kemungkinan besar oleh Firewall Aplikasi Web/WAF).
 - Identitas Otomatis (User-Agent): `sqlmap/1.4.2`. String karakter spesifik ini merupakan bukti keberadaan eksekusi alat pemindaian otomatis, bukan aktivitas peramban standar (seperti Mozilla).

*Kesimpulan Pemeriksaan*: Baris log kedua merupakan bukti indikasi upaya serangan *True Positive*, namun dampak ancamannya telah dimitigasi sebagaimana terverifikasi oleh status respons `403`.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa arsip log (Logs) merupakan krusial dalam operasional keamanan siber (Blue Team)?</summary>

**Jawaban:** Log adalah sumber informasi primer (faktual) mengenai visibilitas keadaan sistem. Ia menyimpan bukti historis lengkap yang memuat informasi identitas pelaku, metode akses, cap waktu (timestamp), dan status suatu aktivitas. Log adalah tulang punggung deteksi peringatan SIEM serta analisis validitas pasca-insiden (forensik).
</details>

<details>
<summary>❓ Kategori (Log Source) manakah yang menyediakan data spesifik tentang aktivitas identitas peramban internet pengguna (User-Agent) serta kode respon HTTP yang dihasilkan peladen?</summary>

**Jawaban:** Web Server Logs.
</details>

<details>
<summary>❓ Apa terminologi teknis untuk protokol standar jaringan yang mengumpulkan dan memancarkan catatan dari beragam host/node menuju satu server repositori tersentralisasi?</summary>

**Jawaban:** Protokol Syslog.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami definisi dan peran teknis dari visibilitas *Logs*.
- [ ] Saya mampu mendeskripsikan varian log spesifik seperti *OS Logs*, *Web Logs*, dan *Network Logs*.
- [ ] Saya mengetahui fungsi dan operasional dasar dari protokol *Syslog*.
- [ ] Saya mampu membedah informasi terstruktur (metadata) dari format akses log server web.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [CrowdStrike: Log Management Explained](https://www.crowdstrike.com/cybersecurity-101/log-management/) — Pemahaman dasar mengenai tata kelola manajemen log dan pentingnya sentralisasi data sistem keamanan.

---

## ➡️ Besok

**Day 4: Incident Response Lifecycle** — Kini Anda memahami cara menganalisis log dan melakukan klasifikasi triase keamanan. Langkah berikutnya adalah memahami metodologi terstruktur untuk menangani dan merespons ancaman terkonfirmasi (insiden). Besok, kita akan membahas siklus tahapan *Incident Response (PICERL)* dari proses preparasi hingga fase pemulihan insiden keamanan siber.

---

*📅 TISS Null Teaming · Week 20 · Day 3 · SENTINEL Rank*
