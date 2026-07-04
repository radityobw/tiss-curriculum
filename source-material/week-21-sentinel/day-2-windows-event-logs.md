# 🛡️ Week 21 · Day 2: Windows Event Logs

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 21 · Day 2/5 | SENTINEL Rank (Minggu 2 dari 5) | Overall: 102/120 hari (85%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** infrastruktur pencatatan (*logging*) di lingkungan Windows menggunakan *Event Viewer*.
2. **Mengidentifikasi** *Event IDs* krusial yang berkaitan dengan proses autentikasi.
3. **Menganalisis** indikasi peretasan dan pembuatan mekanisme akses jarak jauh yang menetap (*Persistence*).

---

## 📖 Materi Inti

### Jantung Forensik Korporasi: Windows Event Viewer

Sebagian besar infrastruktur internal perusahaan dikelola menggunakan sistem operasi **Microsoft Windows Server**. Oleh karena itu, analisis keamanan tingkat lanjut (*Endpoint Detection*) sangat bergantung pada pelacakan aktivitas di sistem operasi ini.

Berbeda dengan keluarga Linux yang mencatat log dalam bentuk teks datar (`.log`), OS Windows menyimpan rekaman aktivitas sistem dalam basis data biner khusus (berformat `.evtx`). Log ini dirancang untuk dibaca menggunakan antarmuka grafis bawaan bernama **Event Viewer**.

Log utama pada *Windows Event Viewer* terbagi menjadi tiga kategori:
1. **Application:** Mencatat aktivitas dan pesan peringatan dari aplikasi pihak ketiga (seperti basis data MS SQL atau antivirus).
2. **System:** Mencatat aktivitas komponen inti Windows, masalah *driver* perangkat keras, dan status layanan sistem saat proses *booting*.
3. **Security (Keamanan):** Pusat perhatian bagi Analis SOC (*Blue Team*). Kategori ini merangkum aktivitas autentikasi (*logon/logoff*), perubahan hak akses administrator, dan modifikasi kebijakan keamanan.

### Kategori Identifikasi Utama: Key Event IDs

Alih-alih menuliskan rincian teks secara panjang lebar, Windows mengelompokkan kejadian menggunakan nomor identifikasi yang disebut **Event ID**. Mengetahui *Event ID* yang fundamental adalah kompetensi wajib bagi seorang analis SOC:

- 🚨 **Event ID 4624 (Logon Success):** Menandakan bahwa proses autentikasi pengguna (atau peretas) berhasil. ID ini juga mencatat *Logon Type* (contoh: Tipe 2 untuk akses langsung di depan komputer, Tipe 3 untuk akses jaringan/folder *sharing*, dan Tipe 10 untuk akses jarak jauh seperti *Remote Desktop* / RDP).
- 🚨 **Event ID 4625 (Logon Failed):** Menandakan kegagalan autentikasi (salah *password*). Jika ID 4625 muncul berulang kali secara masif dalam waktu singkat, ini adalah indikator kuat adanya serangan *Brute Force*.
- 🚨 **Event ID 4688 (Process Creation):** Mencatat setiap kali sebuah program atau perintah baru dijalankan. ID ini sangat krusial saat melakukan *Threat Hunting* untuk melihat apakah ada *file* mencurigakan atau perintah administrator yang dieksekusi diam-diam (contoh: perintah CMD `net user`).
- 🚨 **Event ID 7045 (New Service Installed):** Peretas persisten (seperti *Advanced Persistent Threat* / APT) sering melakukan *Persistence* agar tetap memiliki akses meskipun server di-*restart*. Mereka sering kali menyembunyikan *Backdoor* dengan mendaftarkannya sebagai layanan (*Service*) sistem Windows yang sah. ID ini menandakan instalasi layanan baru yang perlu diawasi.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari belajar mengkorelasikan log Windows untuk mendeteksi ancaman!

1. Anda sedang memantau dasbor SIEM yang merekam log dari server departemen keuangan (`192.168.10.5`).
2. Dasbor menunjukkan riwayat peringatan berikut secara berurutan:
   - `02:10 AM | Event ID: 4625 | User: Administrator | IP Asal: 10.10.10.50`
   - `02:10 AM | Event ID: 4625 | User: Administrator | IP Asal: 10.10.10.50`
   - `02:10 AM | Event ID: 4625 | User: Administrator | IP Asal: 10.10.10.50`
   - `02:11 AM | Event ID: 4624 | User: Administrator | IP Asal: 10.10.10.50 | Logon Type: 10`
   - `02:12 AM | Event ID: 7045 | Service Name: WindowsUpdateHelper`
3. **Analisis Insiden (Triage):**
   - Pada pukul `02:10 AM`, terjadi serangan *Brute Force* (ditandai dengan munculnya rentetan *Event ID 4625*) yang menargetkan akun Administrator lokal dari IP eksternal `10.10.10.50`.
   - Pada pukul `02:11 AM`, serangan berhasil membobol sandi, dibuktikan dengan munculnya *Event ID 4624* melalui akses *Remote Desktop* (*Logon Type 10*).
   - Pada pukul `02:12 AM`, penyerang mempertahankan aksennya (*Persistence*) dengan menanamkan program berbahaya yang disamarkan sebagai layanan Windows baru bernama `WindowsUpdateHelper` (*Event ID 7045*).
   - **Tindakan:** Ini adalah insiden *True Positive* yang harus segera diisolasi (*Containment*).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Kategori log utama apa pada <i>Windows Event Viewer</i> yang mencatat aktivitas autentikasi login dan pengawasan hak akses administratif?</summary>

**Jawaban:** Kategori log *Security* (Security Logs).
</details>

<details>
<summary>❓ Jika Analis SOC mendeteksi rentetan <i>Windows Event ID 4625</i> dalam waktu yang sangat singkat, ini adalah indikator dari serangan tipe apa?</summary>

**Jawaban:** Serangan *Brute Force* (atau *Credential Stuffing*), karena *Event ID 4625* menandakan kegagalan verifikasi kata sandi (*Logon Failed*).
</details>

<details>
<summary>❓ <i>Event ID</i> berapakah yang sering kali dicari Analis untuk mendeteksi tindakan <i>Persistence</i> (pemasangan layanan otomatis/<i>Backdoor</i>) di sistem Windows?</summary>

**Jawaban:** Event ID 7045 (New Service Installed).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami fungsi dan struktur penyimpanan *Windows Event Viewer*.
- [ ] Saya mampu membedakan makna dari *Event ID 4624* dan *4625*.
- [ ] Saya mengetahui bahwa *Event ID 7045* dapat menandakan adanya jejak instalasi *backdoor* (*Persistence*).
- [ ] Saya mampu menarik kesimpulan insiden berdasarkan urutan kronologis *Event ID* (seperti pada Mini Lab).
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Ultimate Windows Security: Event ID Encyclopedia](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/) — Referensi lengkap dan tepercaya untuk mendeskripsi makna dari setiap Windows Event ID.

---

## ➡️ Besok

**Day 3: Linux Logs & Journalctl** — Setelah memahami pemantauan *Endpoint* berbasis Windows, besok kita akan beralih ke lingkungan peladen yang sering digunakan untuk infrastruktur web dan *cloud*, yaitu **Linux**. Kita akan menelusuri lokasi log di direktori `/var/log/`, membedah hierarki *file* seperti `auth.log`, dan menggunakan perintah ekstraksi log terpusat: `journalctl`.

---

*📅 TISS Null Teaming · Week 21 · Day 2 · SENTINEL Rank*
