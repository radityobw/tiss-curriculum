# 🛡️ Week 21 · Day 3: Linux Logs & Journalctl

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 21 · Day 3/5 | SENTINEL Rank (Minggu 2 dari 5) | Overall: 103/120 hari (86%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengeksplorasi** arsitektur penyimpanan log standar di sistem operasi Linux (`/var/log/`).
2. **Menganalisis** struktur *file* log autentikasi utama (`auth.log` atau `secure`).
3. **Mengekstrak** dan menyaring data log sistem menggunakan perintah `journalctl`.

---

## 📖 Materi Inti

### Arsitektur Penyimpanan Log Standar: Direktori `/var/log/`

Jika infrastruktur Windows mengelola log menggunakan *Event Viewer* yang berbasis *database* biner, sistem operasi **Linux** (yang sangat dominan digunakan pada *server Cloud* dan infrastruktur perusahaan) menganut konsep teks datar (*plain text*).

Seluruh arsip log aktivitas sistem dan aplikasi di Linux dipusatkan pada direktori `/var/log/`.
Di dalam direktori tersebut, sistem mengkategorikan log ke dalam beberapa *file* penting:

1. **`syslog` (atau `messages` di distro RedHat/CentOS):** Catatan aktivitas sistem secara umum (*Global System Log*). Merekam berbagai informasi sistem operasi, aktivitas perangkat keras, dan peringatan layanan yang tidak memiliki *file* log tersendiri.
2. **`auth.log` (atau `secure` di distro RedHat/CentOS):** Log autentikasi utama. Ini adalah target utama investigasi (*Triage*) bagi Analis Keamanan karena merekam semua aktivitas login yang berhasil maupun gagal, sesi *SSH (Secure Shell)*, serta penggunaan perintah hak akses administrator (`sudo`).
3. **`dmesg`:** Merekam pesan diagnostik tingkat kernel (*kernel ring buffer*) sejak *server* pertama kali dihidupkan (*booting*), yang sering digunakan untuk melacak masalah perangkat keras.

### Analisis Log Autentikasi (`auth.log`)

Ketika Analis SOC menginvestigasi `auth.log`, mereka mencari pola anomali berbasis teks.
Contoh baris log yang mengindikasikan serangan *Brute Force* (kegagalan *login* via SSH):
`Oct 22 14:30:15 server1 sshd[1234]: Failed password for invalid user admin from 10.5.5.5 port 45212 ssh2`

Contoh baris log yang mengindikasikan eskalasi privilese (pengguna biasa beralih menjadi *administrator/root* menggunakan `sudo`):
`Oct 22 14:35:10 server1 sudo: hacker_user: TTY=pts/0; PWD=/home/hacker_user; USER=root; COMMAND=/bin/bash`
Baris di atas memvalidasi insiden nyata (*True Positive*): pengguna `hacker_user` berhasil mengeksekusi wewenang administratif tertinggi (pengguna `root`) dan membuka akses interaktif persisten (`/bin/bash`).

### Ekstraksi Log Modern: `journalctl`

Pada ekosistem Linux modern yang menggunakan manajemen layanan *Systemd*, pencatatan log dikelola secara terpusat dan berformat biner oleh `systemd-journald`. Log ini dapat diakses, difilter, dan dianalisis menggunakan satu perintah andalan: **`journalctl`**.

Kekuatan utama `journalctl` terletak pada kemampuan pemfilteran argumen (*query*):
- `journalctl -u ssh.service`: Menyaring log dan hanya menampilkan rekaman yang berkaitan dengan layanan/daemon SSH.
- `journalctl --since "1 hour ago"`: Menampilkan rentetan kejadian spesifik yang terjadi secara eksklusif dalam 60 menit terakhir.
- `journalctl -p err`: Hanya menampilkan log yang berstatus krisis teknis atau memiliki tingkat keparahan tinggi (*Error*).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari belajar mencari bukti kompromi sistem (IOCs) dengan perintah dasar Linux!

1. Anda bertugas menginvestigasi log koneksi di sebuah server Ubuntu. Fokus Anda adalah mengidentifikasi *Brute Force* dan otentikasi eskalasi privilese (*Sudo*).
2. Anda diminta untuk mengekstrak entri yang mengindikasikan *password* salah di `/var/log/auth.log` menggunakan alat bantu `grep`.
3. Anda menjalankan perintah pencarian:
   `grep "Failed password" /var/log/auth.log`
4. **Hasil (Output):** Terminal menampilkan ratusan baris log penolakan autentikasi yang secara dominan berasal dari satu alamat IP statis (`45.33.22.11`). Ini memvalidasi serangan *Brute Force*.
5. Selanjutnya, Anda mencari indikasi penyalahgunaan *sudo* dengan perintah: 
   `grep "sudo" /var/log/auth.log | grep "COMMAND="`
6. **Evaluasi (Triage):** Terdeteksi eksekusi baris komando yang tidak wajar. Ini menegaskan bahwa penyerang telah berhasil masuk dan melakukan Eskalasi Privilese (*Privilege Escalation*). Insiden berstatus *True Positive* dan harus segera ditangani.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam infrastruktur Linux standar, di direktori manakah hampir semua rekaman aktivitas (*logs*) sistem operasi dan layanan aplikasi dipusatkan?</summary>

**Jawaban:** `/var/log/`.
</details>

<details>
<summary>❓ Apabila Analis SOC ingin menyelidiki rentetan serangan <i>Brute Force SSH</i> atau upaya eskalasi privilese melalui perintah <i>sudo</i> di OS Ubuntu, <i>file</i> log manakah yang harus ia periksa pertama kali?</summary>

**Jawaban:** `auth.log` (atau `/var/log/auth.log`).
</details>

<details>
<summary>❓ Pada ekosistem Linux modern yang berbasis <i>Systemd</i>, alat (*command*) apa yang digunakan untuk mengekstrak dan memfilter log terpusat dengan kemampuan pencarian waktu (misal: <i>--since</i>)?</summary>

**Jawaban:** `journalctl`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami struktur penyimpanan direktori log di `/var/log/`.
- [ ] Saya mengerti fungsi dan pentingnya log autentikasi `auth.log` (atau `secure`).
- [ ] Saya dapat membaca dan mendeteksi anomali kegagalan autentikasi SSH.
- [ ] Saya dapat menggunakan alat bantu `journalctl` untuk memfilter riwayat *Systemd*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [DigitalOcean: How To View and Configure Linux Logs](https://www.digitalocean.com/community/tutorials/how-to-view-and-configure-linux-logs-on-ubuntu-and-centos) — Panduan teknis memahami lokasi dan cara membaca direktori log di Ubuntu dan CentOS.

---

## ➡️ Besok

**Day 4: Pattern Recognition** — Setelah memahami format struktural log dasar, saatnya melangkah lebih jauh. Dalam lingkungan *Enterprise* nyata, data log sangat berlimpah (*Big Data logs*). Membaca log baris per baris secara manual tidak lagi memungkinkan. Besok, kita akan mempelajari **Pattern Recognition** (Pengenalan Pola) untuk mendeteksi anomali. Kamu akan belajar mengidentifikasi bentuk visual atau frekuensi khas dari serangan *Brute Force*, aktivitas *Vulnerability Scanner*, dan percobaan *Data Exfiltration*.

---

*📅 TISS Null Teaming · Week 21 · Day 3 · SENTINEL Rank*
