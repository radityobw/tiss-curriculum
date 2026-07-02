# 🎯 Week 7 · Day 6 (Bonus): Hands-On Learning

> **Rank**: PACKET | **Minggu ke-7** | Bonus Day

---

## 🌐 Platform Hari Ini

**[Linux Journey — Grasshopper](https://linuxjourney.com/)**
Platform interaktif untuk belajar Linux dari nol. Modul *Grasshopper* mencakup command line, text manipulation, dan filesystem — cocok untuk memperkuat fondasi yang dipelajari minggu ini.

💰 **Biaya**: Gratis (tanpa akun, tanpa registrasi, tanpa batasan)
⏱️ **Estimasi Waktu**: ~60 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menyelesaikan modul *Command Line* dan *Text-Fu* di Linux Journey
2. Mempraktikkan perintah Linux tambahan yang belum dicakup di materi harian
3. Menjawab kuis evaluasi di akhir setiap modul

---

## 📋 Requirement

* Peramban web modern (Chrome/Firefox)
* Terminal Linux (VM/WSL yang sudah disetup di Day 2 minggu ini)

> ⚠️ **Tidak perlu membuat akun.** Linux Journey sepenuhnya terbuka tanpa registrasi.

---

## 📝 Prosedur

### Langkah 1: Akses Linux Journey
1. Buka [linuxjourney.com](https://linuxjourney.com/)
2. Klik **Grasshopper** (level pemula)
3. Pilih modul **"Command Line"**

### Langkah 2: Kerjakan Modul Command Line
1. Baca setiap halaman materi tentang perintah dasar CLI
2. Di setiap halaman, ada bagian **"Exercises"** — kerjakan di terminal Linux-mu (VM/WSL)
3. Jawab kuis di akhir setiap sub-topik
4. Perintah yang harus kamu praktikkan langsung di terminal:
 ```bash
 echo "Hello TISS"
 pwd
 cd /tmp
 ls -la
 mkdir latihan-linux-journey
 touch file1.txt file2.txt
 cp file1.txt file1-backup.txt
 mv file2.txt latihan-linux-journey/
 rm file1-backup.txt
 ```

> 💡 **Tips**: Jangan hanya membaca — **ketik sendiri** setiap perintah di terminal. Muscle memory sangat penting untuk CLI.

### Langkah 3: Kerjakan Modul Text-Fu
1. Kembali ke halaman Grasshopper
2. Pilih modul **"Text-Fu"**
3. Pelajari perintah manipulasi teks:
 ```bash
 cat /etc/hostname
 head -5 /etc/passwd
 tail -5 /etc/passwd
 grep "root" /etc/passwd
 wc -l /etc/passwd
 ```
4. Kerjakan exercises dan kuis

### Langkah 4: Tantangan Mandiri
1. Buat file baru bernama `catatan-linux.txt`
2. Isi dengan 5 perintah Linux favorit-mu beserta fungsinya
3. Gunakan perintah `cat` untuk menampilkan isi file tersebut
 ```bash
 nano catatan-linux.txt # tulis isi file
 cat catatan-linux.txt # tampilkan isi
 ```

---

## 🏁 Target Output

* ✅ Modul **Command Line** di Linux Journey selesai (kuis terjawab)
* ✅ Modul **Text-Fu** di Linux Journey selesai (kuis terjawab)
* 📸 Tangkapan layar terminal yang menunjukkan eksekusi perintah dari exercises
* 📝 File `catatan-linux.txt` berisi 5 perintah Linux favorit + fungsinya

---

## 🔄 Fallback

Jika Linux Journey tidak bisa diakses:
1. Buka [LinuxSurvival.com](https://linuxsurvival.com/) (gratis, browser-based)
2. Kerjakan 4 modul tutorial interaktif yang tersedia
3. Tetap praktikkan perintah di terminal lokal (VM/WSL)
