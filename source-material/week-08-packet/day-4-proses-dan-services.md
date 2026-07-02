# 📡 Week 8 · Day 4: Proses & Services

> **Rank**: PACKET | **Minggu ke-8**, Hari 4/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 8 · Day 4/5 | PACKET Rank (Minggu 4 dari 5) | Overall: 39/120 hari (32%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Melihat** daftar program yang sedang berjalan di *background* (`ps`, `top`)
2. **Menghentikan** paksa program yang *error* atau mencurigakan (`kill`)
3. **Mengelola** jalannya layanan sistem otomatis (`systemctl`)

---

## 📖 Materi Inti

### Menjadi Dokter Sistem

Di Windows, jika komputermu tiba-tiba lemot atau ada aplikasi yang nge-hang (*Not Responding*), kamu pasti langsung menekan tombol legendaris: `CTRL + ALT + DEL` lalu membuka *Task Manager*.

Di server Linux (yang layarnya hanya hitam-putih), bagaimana cara kita mendeteksi ada program apa yang diam-diam memakan 100% RAM, atau mendeteksi ada virus rahasia (malware) yang sedang berjalan di *background*?

Selamat datang di manajemen Proses (Process Management).

### 1. `top` dan `htop` (Task Manager-nya Linux)

Jika kamu ingin melihat performa server secara **Real-Time** (Terus bergerak):
Ketik: `top` (atau `htop` jika sudah diinstal, ini versi yang lebih cantik dan berwarna).

Kamu akan melihat:
- Berapa % sisa RAM dan CPU yang dipakai.
- Daftar program yang paling berat berada di posisi paling atas.
- *Tekan huruf **`q`** untuk keluar dari mode top.*

### 2. `ps` (Process Status)

Jika `top` mirip seperti video yang terus bergerak, maka `ps` mirip seperti **Foto (Screenshot)**. Ia menangkap daftar program yang berjalan persis pada detik saat tombol Enter ditekan.

Perintah sakti yang paling sering dipakai *SysAdmin/Hacker* adalah:
```bash
$ ps aux
```
- **a**: Tampilkan proses dari *semua* user.
- **u**: Tampilkan nama user dan detail pemakaian memorinya.
- **x**: Tampilkan juga proses jahat/background yang berjalan tanpa ada jendela terminalnya (daemon).

Biasanya hasilnya akan ribuan baris! Nah, ingat pelajaran minggu lalu soal `grep` dan Pipa `|`? Mari kita gabungkan!
Untuk mencari apakah program web server *apache* sedang berjalan:
```bash
$ ps aux | grep apache
```

### 3. Eksekutor: `kill`

Setiap program yang berjalan di Linux akan diberi plat nomor unik bernama **PID (Process ID)**. Kamu bisa melihat kolom PID ini saat mengetik `top` atau `ps aux`.

Jika program macet, kamu tidak bisa menekan "X" warna merah pakai mouse. Kamu harus menjadi "Malaikat Maut" dan mengeksekusinya via nomor PID.

```bash
$ kill 1337
```
(Akan menyuruh program dengan nomor PID 1337 untuk menutup dirinya secara baik-baik).

Jika programnya bandel dan tidak mau mati juga, paksa bunuh dengan instan:
```bash
$ kill -9 1337
```
(Sinyal `-9` adalah *SIGKILL*, perintah dari Kernel yang tidak bisa ditolak oleh program apapun!).

### 4. Background Services: `systemctl`

Beberapa program penting (seperti Web Server, Database, atau SSH) harus otomatis menyala saat server baru di-*restart* tanpa disuruh manual. Program yang "menjaga" dari *background* ini disebut **Services** atau **Daemons**.

Alat untuk mengelolanya disebut **systemd**, dan perintahnya adalah **`systemctl`**.

Contoh pemakaian (mengatur service bernama `apache2`):
- `sudo systemctl status apache2` -> (Melihat apakah web server sedang nyala atau mati/error).
- `sudo systemctl start apache2` -> (Menyalakan web server sekarang).
- `sudo systemctl enable apache2` -> (Menyuruh web server otomatis menyala tiap komputer baru di-restart).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Buka Terminal WSL/Mac/Linux kamu. Mari kita berlatih menjadi Sniper Proses!

1. Buka satu tab/jendela Terminal baru. Di jendela ini, jalankan program "penidur" selama 10 menit. Ketik:
 `sleep 600` (Tekan Enter. Layarmu akan diam saja, biarkan!).
2. Buka jendela Terminal **kedua**. Kita akan memburu si penidur tadi.
3. Di jendela kedua, cari nomor punggung si penidur (PID) dengan kombinasi mematikan kita:
 `ps aux | grep sleep`
4. Di output yang muncul, kamu akan melihat kolom kedua berisi angka (Misal: `4052`). Itu adalah **PID**.
5. Bertindaklah sebagai sniper. Bunuh penidur itu!
 `kill -9 [Nomor_PID_Tadi]`
6. Buka kembali jendela Terminal pertamamu. Kamu akan melihat tu *"Killed"* (Terbunuh) dan terminalmu kembali merespons! 

Selamat, kamu baru saja mengeksekusi program pertamamu di Linux!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Jika Terminal Task Manager `top` terus bergerak-gerak dan kamu tidak bisa mengetik perintah lain, tombol apa di keyboard yang harus kamu tekan untuk kembali?</summary>

**Jawaban:** Tombol huruf **`q`** (berasal dari kata *Quit*).

</details>

<details>
<summary>❓ Apa itu PID dan mengapa ini sangat penting saat kita ingin menggunakan perintah `kill`?</summary>

**Jawaban:** **PID (Process ID)** adalah nomor urut identitas unik yang diberikan sistem operasi ke setiap program yang sedang berjalan. Perintah `kill` tidak menembak "nama aplikasi", melainkan menembak "nomor PID". Tanpa tahu nomor PID-nya, kita tidak bisa mematikan program spesifik tersebut.

</details>

<details>
<summary>❓ Temanmu me-restart (reboot) server Linux-nya, tapi tiba-tiba halaman website di server tersebut gagal dimuat/mati. Berdasarkan fungsi `systemctl`, apa kemungkinan masalahnya?</summary>

**Jawaban:** Temanmu mungkin belum melakukan `systemctl enable` pada *service* web server-nya (misal apache/nginx). Sehingga saat server menyala ulang, *service* web-nya tidak ikut menyala secara otomatis. Solusinya: `sudo systemctl start nginx` lalu diikuti dengan perintah `enable`.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya hafal fungsi `top` dan `ps aux` untuk memonitor memori/program
- [ ] Saya paham apa itu kolom nomor PID
- [ ] Saya tahu cara kerja Pipa `ps aux | grep...`
- [ ] Saya hafal fungsi perintah `kill` dan `kill -9` (paksa bunuh)
- [ ] Saya tahu guna dasar perintah `systemctl` untuk *service background*
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Linux Processes Explained](https://linuxjourney.com/lesson/monitor-processes-top) — Pelajaran visual ringkas tentang proses dan perintah *kill* dari Linux Journey.

---

## ➡️ Besok

**Day 5: Lab & Mission: Lanjut Wargame Bandit!** — Teori selama seminggu selesai! Besok saatnya kamu mendaki menara server OverTheWire kembali. Kali ini, file passwordnya tidak akan digeletakkan begitu saja. Mereka akan disembunyikan menggunakan trik file Permission (rwx) dan file tersembunyi. Siapkan otakmu!

---

*📅 TISS Null Teaming · Week 8 · Day 4 · PACKET Rank*
