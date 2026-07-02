# 🛡️ Week 21 · Day 2: Windows Event Logs

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 21 · Day 2/5 | SENTINEL Rank (Minggu 2 dari 5) | Overall: 102/120 hari (85%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** infrastruktur arsitektur pengarsipan riwayat operasional di lingkungan *Windows* (*Event Viewer*).
2. **Mengidentifikasi** sandi identifikasi log krusial (*Key Event IDs*) yang merepresentasikan indikator proses otentikasi.
3. **Menganalisis** rekam jejak pembuatan presistensi (instalasi layanan baru) oleh aktivitas peretasan.

---

## 📖 Materi Inti

### Jantung Forensik Korporasi: Windows Event Viewer

Infrastruktur jaringan *backend* internal di sebagian besar korporasi dikelola menggunakan sistem operasi **Microsoft Windows Server**. Analisis tingkat lanjut (Endpoint Detection) berfokus pada pelacakan aktivitas administratif di lapisan OS ini.

Berbeda dengan keluarga sistem *Unix/Linux* yang menggunakan berkas teks ASCII datar (`.log`), OS Windows mengumpulkan, merangkum, dan menstrukturisasi rekaman aktivitas sistemnya dalam basis data biner spesifik yang dirancang untuk dibaca utuh dengan antarmuka manajemen grafis bawaan bernama **Event Viewer** (berformat berkas arsip `.evtx`).

Klasifikasi utama riwayat sistem di Windows Event Viewer terbagi menjadi tiga penampang (*Log Channels*):
1. **Application:** Dokumentasi peringatan diagnostik aplikasi dan perangkat lunak perangkat lunak mandiri pihak ketiga (seperti layanan basis data MS SQL).
2. **System:** Dokumentasi parameter kesehatan kernel, peringatan interupsi sirkuit piranti keras, dan layanan kegagalan inisialisasi boot.
3. **Security (Keamanan):** Dokumentasi sentral pemantauan analis perlindungan (*Blue Team*). Merangkum aktivitas otentikasi (logon/logoff), delegasi privilese direktori administratif (hak akses), dan manipulasi kebijakan audit *firewall*.

### Kategori Identifikasi Utama: Key Event IDs

Alih-alih menuliskan rincian narasi dalam setiap kejadian, Windows mengelompokkan dokumentasi tersebut menggunakan indeks identifikasi numerik yang disebut sebagai **Event ID**. Menghafal signifikansi ID fundamental merupakan kapabilitas wajib bagi seorang spesialis SOC:

- 🚨 **Event ID 4624 (Logon Success):** Mencatat indikasi bahwa proses otentikasi entitas pengguna (atau peretas) sukses tereksekusi sehingga sesi koneksi diberikan (Berhasil masuk). ID ini senantiasa disandingkan dengan parameter *Logon Type* (Tipe 2 menandakan interaksi fisik di depan konsol, Tipe 3 untuk akses berbagi *file* dari jaringan, dan Tipe 10 mengindikasikan konektivitas remot seperti *RDP*).
- 🚨 **Event ID 4625 (Logon Failed):** Mencatat indikasi kegagalan otentikasi (sandi/kredensial keliru). Apabila ID 4625 terekam dalam frekuensi yang sangat beruntun dan masif di dalam rentang *timestamp* hitungan detik, ini merupakan parameter indikatif aktivitas peretasan jenis *Brute Force*.
- 🚨 **Event ID 4688 (Process Creation):** Mencatat inisiasi pengeksekusian sebuah berkas aplikasi, perintah, atau program baru. Sangat krusial dalam prosedur audit (Threat Hunting) apabila peretas mengeksekusi binari administratif secara terselubung (contoh: pemanggilan CMD kueri `net user`).
- 🚨 **Event ID 7045 (New Service Installed):** Peretas persisten (seperti ancaman *APT*) sering kali mendemonstrasikan tahapan *Persistence* (agar tidak kehilangan akses bila komputer dinyalakan ulang). Mereka akan mengonfigurasi skrip eksploitasinya (Backdoor) dengan meregistrasikannya secara permanen menyamar sebagai *Service* Windows yang sah. ID ini menandakan instalasi layanan servis yang tak wajar.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyusun simulasi ekstraksi korelasi identifikasi ancaman pada peladen Windows!

1. Anda sedang melakukan observasi dasbor SIEM yang mengintegrasikan pencatatan logs keamanan dari peladen divisi finansial perusahaan (Alamat IP: `192.168.10.5`).
2. Dasbor menyajikan agregasi matriks riwayat berurutan berikut (Format Ekstraksi Data):
 - `02:10 AM | Event ID: 4625 | User: Administrator | IP Asal: 10.10.10.50`
 - `02:10 AM | Event ID: 4625 | User: Administrator | IP Asal: 10.10.10.50`
 - `02:10 AM | Event ID: 4625 | User: Administrator | IP Asal: 10.10.10.50`
 - `02:11 AM | Event ID: 4624 | User: Administrator | IP Asal: 10.10.10.50 | Logon Type: 10`
 - `02:12 AM | Event ID: 7045 | Service Name: WindowsUpdateHelper`
3. **Simpulan Triage (Korelasi Bukti):**
 Berdasarkan pengamatan sekuensial, pada pukul 02:10 AM terekam insiden *Brute Force* (anomali frekuensi *Event ID 4625*) yang membidik instansi administrator lokal dari rute koneksi eksternal yang statis. Pada pukul 02:11 AM, proses peretasan membobol parameter sandi terkonfirmasi valid melalui instalasi sesi autentikasi jarak jauh *Remote Desktop* (dibuktikan dengan eksistensi *Event ID 4624* berstatus *Logon Type 10*). Puncaknya di pukul 02:12 AM, penyerang menerapkan rutinitas penetrasi persisten dengan memicu pembuatan entitas servis parasit (*Event ID 7045*) dengan menyamarkan namanya (obfuscated) menjadi `WindowsUpdateHelper`. Eksekusi status eskalasi insiden valid untuk dilakukan taktik remediasi *Containment* segera.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Menguraikan anatomi penyimpanan sistem operasi, kategori arsitektur log utama manakah pada aplikasi <i>Windows Event Viewer</i> yang didedikasikan secara khusus untuk dokumentasi otentikasi login dan pengawasan audit hak kepemilikan privilese di tingkat administrator SOC?</summary>

**Jawaban:** Kategori log *Security* (Security Logs).
</details>

<details>
<summary>❓ Apabila SOC Analyst mendeteksi eskalasi drastis secara beruntun dari notifikasi pelaporan <i>Windows Event ID 4625</i> dalam periode sempit, indikator anomali tersebut digunakan sebagai basis penarikan bukti untuk insiden tipe apa?</summary>

**Jawaban:** Indikator peretasan berbasis *Brute Force* (atau serangan *Credential Stuffing/Password Guessing*), karena parameter Event ID 4625 merepresentasikan aktivitas *Logon Failed* (kegagalan verifikasi kata sandi yang masif).
</details>

<details>
<summary>❓ Untuk merepresentasikan persistensi *Backdoor* di sistem operasi berbasis Windows, kemunculan indikator <i>Event ID</i> nomor berapakah yang senantiasa diincar Analis sebagai notifikasi perwujudan eksekusi registrasi aktivitas servis aplikasi latar belakang (Service) di komputer korporasi?</summary>

**Jawaban:** Event ID 7045 (New Service Installed).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami struktur konseptual penyimpanan basis data biner dalam *Windows Event Viewer*.
- [ ] Saya sanggup mendeskripsikan secara diferensiasi dari nomor identifikasi *Event ID 4624* dan *4625*.
- [ ] Saya mengenal signifikansi *Event ID 7045* selaku jejak persisten peretas di ranah manajemen proses (Service).
- [ ] Saya memiliki kompetensi menarik korelasi alur kronologis pada contoh rangkaian matriks peringatan identifikasi sistem Windows (Mini Lab).
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Ultimate Windows Security: Event ID Encyclopedia](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/) — Repositori definitif basis pengetahuan untuk proses dokumentasi dekripsi fungsi puluhan ribu referensi log keamanan Windows.

---

## ➡️ Besok

**Day 3: Linux Logs & Journalctl** — Anda telah mendemonstrasikan wawasan dekripsi metadata pencatatan *Endpoint* berbasis Microsoft Windows. Esok hari, sesi fokus akan bergeser ke ranah OS peladen web, infrastruktur kontainerisasi (*Cloud*), serta arsitektur basis data relasional dominan, yaitu sistem berbasis **Linux**. Anda akan menelusuri lokasi log terstruktur di partisi khusus `/var/log/`, membedah hierarki file vital *auth.log*, serta menggunakan kemampuan sistem *query* ekstraksi sentral: log `journalctl`.

---

*📅 TISS Null Teaming · Week 21 · Day 2 · SENTINEL Rank*
