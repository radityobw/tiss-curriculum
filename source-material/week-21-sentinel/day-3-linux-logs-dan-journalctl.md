# 🛡️ Week 21 · Day 3: Linux Logs & Journalctl

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 21 · Day 3/5 | SENTINEL Rank (Minggu 2 dari 5) | Overall: 103/120 hari (86%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengeksplorasi** arsitektur hirarki penempatan penyimpanan standar rekam jejak (*Logs*) di OS Linux (`/var/log/`).
2. **Menganalisis** struktur file otentikasi sentral (berkas `auth.log` atau `secure`).
3. **Mengekstrak** serta memanipulasi rentetan data peringatan sistem menggunakan perintah modern `journalctl`.

---

## 📖 Materi Inti

### Arsitektur Penyimpanan Log Standar: Direktori `/var/log/`

Sementara infrastruktur Windows mengelola catatannya dalam arsip *database* berbasis aplikasi GUI grafis, sistem operasi **Linux** (yang secara dominan menyokong ekosistem peladen Cloud dan infrastruktur perusahaan) menganut konsep di mana semua entitas diklasifikasikan sebagai *plain text* (berkas file teks biasa). 

Keseluruhan arsip dan peringatan aktivitas jaringan di Linux bermuara secara terpusat pada partisi direktori: `/var/log/`.
Di dalam kumpulan direktori tersebut, sistem mendokumentasikan bermacam klasifikasi catatan, di antaranya:

1. **`syslog` (atau `messages` di distro turunan RedHat/CentOS):** Dokumentasi kronologi sistem secara umum (*Global System Log*). Merekam berbagai indikasi malfungsi sistem operasi tingkat dasar, aktivitas modul perangkat *hardware*, dan perangkat lunak yang tidak dialokasikan di fail log spesifik mereka sendiri.
2. **`auth.log` (atau `secure` di distro turunan RedHat/CentOS):** Berkas log otentikasi utama. Merupakan destinasi investigasi (Triage) pertama Analis keamanan, sebab log ini merekam keberhasilan verifikasi login, penolakan kredensial (kegagalan otentikasi kata sandi), sesi protokol transfer enkripsi tinggi seperti *SSH (Secure Shell)*, serta pelacakan eskalasi perizinan hak tingkat administrator oleh instruksi terminal perintah `sudo`.
3. **`dmesg`:** Merangkum peringatan perangkat keras spesifik selama sesi peladen dihidupkan (booting sequence) guna melacak diagnostik galat pada kernel peladen.

### Dekripsi Audit Metadata Log `auth.log`

Ketika spesialis *Blue Team* menganalisis `auth.log`, mereka menerapkan parameter pelacakan tekstual.
Contoh baris dokumentasi indikasi aktivitas gagal (*Brute Force* login via protokol SSH):
`Oct 22 14:30:15 server1 sshd[1234]: Failed password for invalid user admin from 10.5.5.5 port 45212 ssh2`

Contoh baris dokumentasi bukti eskalasi privilese (Peretas berhasil mengklaim otoritas sistem dengan mengeksekusi komando *Sudo* tingkat administrator):
`Oct 22 14:35:10 server1 sudo: hacker_user: TTY=pts/0; PWD=/home/hacker_user; USER=root; COMMAND=/bin/bash`
Baris di atas memvalidasi *True Positive* peretasan, mengonfirmasi eksistensi pengguna standar `hacker_user` beralih posisi mengeksekusi wewenang absolut administrator puncak (user `root`) dan membuka akses lingkungan antarmuka peretasan interaktif persisten.

### Modernisasi Ekstraksi Catatan: `journalctl`

Pada ekosistem OS Linux generasi terbaru yang diatur melalui *Systemd*, metode pendokumentasian log telah diotomatisasi secara struktural dan dikoordinasikan secara biner. Repositori komprehensif log *systemd* ini dapat diinterogasi melalui komponen terminal tunggal, yakni instruksi perintah: **`journalctl`**.

Kapasitas tertinggi dari `journalctl` terletak pada keleluasaan fungsi pemfilteran dan pencarian variabel kueri terstruktur (mirip fungsi bahasa SQL)!
- `journalctl -u ssh.service`: Menyaring (*Filter*) pencarian dan hanya menampilkan entitas rekam jejak untuk unit layanan *SSH/daemon* (membedah interaksi otentikasi khusus SSH).
- `journalctl --since "1 hour ago"`: Mencari rekam jejak spesifik kejadian terpusat secara eksklusif hanya untuk jangka rentang waktu 60 menit mundur dari waktu eksekusi saat ini.
- `journalctl -p err`: Parameter penyeleksian diaktifkan untuk menampilkan secara spesifik hanya kejadian krisis teknis atau pelaporan kesalahan sistem (Status: Error).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melakukan validasi pelacakan berbasis fungsi instruksi terminal Linux sederhana!

1. Siapkan instalasi distribusi Linux Anda di ekosistem (Linux Virtual Machine/WSL) jika Anda ingin memanifestasikannya. (Dapat dilaksanakan melalui praktik simulasi visual berikut).
2. Anda bertugas menginvestigasi log kegagalan koneksi di atas server Ubuntu. Sasaran analisis difokuskan pada identifikasi *Brute Force* dan otentikasi anomali eskalasi (*Sudo*).
3. Anda diminta mencari ekstraksi fungsi spesifik ke dalam data taktis dengan memanfaatkan parameter `grep` guna mengekstrak kata kunci log di direktori `/var/log/auth.log`.
4. Anda merumuskan kueri ekstraksi:
 `grep "Failed password" /var/log/auth.log`
5. Terminal CLI menampilkan (Output) lebih dari seratus baris dokumentasi gagal (penolakan) parameter eksekusi kredensial otentikasi yang mayoritas diinisiasi dari lokasi rute statis (IP Asal `45.33.22.11`).
6. Selanjutnya, Anda menguji indikator eksistensi komando `sudo` dari perintah: 
 `grep "sudo" /var/log/auth.log | grep "COMMAND="`
7. Teridentifikasi eksekusi baris komando eksternal tak lazim, menegaskan aktivitas entitas tamu sukses memanfaatkan komando *root* secara paksa (Privilege Escalation). *Evaluasi Triase: Indikator Serangan True Positive (Eskalasi ke Tier 2 secara seketika)*.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah infrastruktur log Linux secara spesifik, direktori (rute folder) absolut utama manakah yang berfungsi mendokumentasikan serta memusatkan hampir seluruh rekam jejak log OS dan layanan aplikasi di ekosistem standar Linux?</summary>

**Jawaban:** `/var/log/`.
</details>

<details>
<summary>❓ Apabila penganalisis merumuskan investigasi pencarian bukti rentetan log <i>Brute Force</i> dan upaya otentikasi (seperti eskalasi <i>ssh</i> atau perampasan privilese <i>sudo</i>) pada OS turunan keluarga Debian/Ubuntu, dokumen log sentral spesifik manakah yang akan diperiksa (dikueri) pertama kali?</summary>

**Jawaban:** `auth.log` (atau `/var/log/auth.log`).
</details>

<details>
<summary>❓ Di ekosistem Linux termutakhir berbasis konfigurasi manajemen *Systemd*, fitur komando terminal spesifik apa (dengan awalan nama 'j') yang berfungsi selaku fasilitas analitikal untuk melakukan ekstraksi filter data binari peringatan serta log peladen Linux yang sangat kompleks secara dinamis?</summary>

**Jawaban:** perintah `journalctl`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menguasai struktur penyimpanan arsip pada parameter hierarki folder `/var/log/`.
- [ ] Saya mengetahui dan pemahaman dokumentasi otentikasi pada *auth.log*.
- [ ] Saya mendemonstrasikan metode validasi deteksi otentikasi penyusupan melalui pengawasan lalu-lintas aktivitas *SSH*.
- [ ] Saya sanggup menyederhanakan data pemantauan kueri *Systemd* melalui pengerahan parameter *journalctl*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [DigitalOcean: How To View and Configure Linux Logs](https://www.digitalocean.com/community/tutorials/how-to-view-and-configure-linux-logs-on-ubuntu-and-centos) — Dokumen mengenai dasar penelusuran manajemen direktori dokumentasi log di distribusi Ubuntu dan CentOS.

---

## ➡️ Besok

**Day 4: Pattern Recognition** — Penguasaan komponen struktural metadata arsitektur telah ditunaikan. Kini, parameter kapabilitas *Blue Team* memindahkan kompetensi utama untuk membedah ekosistem data yang berlimpah di dunia industri yang padat (*Big Data logs*). Pembacaan kronologi baris log teks tergolong statis. Besok, kompetensi keahlian menuntut pemilahan metode pengenalan visual kognitif, yakni **Pattern Recognition** (Mengenali pola berulang). Anda akan diperkenalkan bagaimana melacak tanda ancaman peretasan *Brute Force*, aktivitas pengintaian peladen (*Vulnerability Scanner*), dan mitigasi taktis insiden indikasi pencurian transmisi data (*Data Exfiltration*).

---

*📅 TISS Null Teaming · Week 21 · Day 3 · SENTINEL Rank*
