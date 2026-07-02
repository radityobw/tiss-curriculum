# 📡 Week 7 · Day 4: Membaca & Mencari File

> **Rank**: PACKET | **Minggu ke-7**, Hari 4/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 7 · Day 4/5 | PACKET Rank (Minggu 3 dari 5) | Overall: 34/120 hari (28%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membaca** file berukuran dengan aman menggunakan `less`, `head`, dan `tail`
2. **Mencari** letak lokasi file yang hilang dengan `find`
3. **Mengekstrak** kata/informasi spesifik dari tumpukan teks menggunakan CLI: `grep`

---

## 📖 Materi Inti

### Membaca File Raksasa Tanpa Lag

Kemarin kita memakai `cat` untuk membaca isi file. Tapi jika kamu men-`cat` file log server yang panjangnya jutaan baris, layar terminalmu akan macet. Gunakan alat yang lebih cerdas:

#### 1. `less` (Membaca Halaman per Halaman)
```bash
$ less log_error_server.txt
```
Ini akan memuat layar halaman pertama saja. 
- Tekan **Spasi** untuk turun 1 layar (halaman selanjutnya).
- Tekan tombol panah atas/bawah untuk geser per baris.
- Tekan **q** untuk (Quit/Keluar) dan kembali ke terminal.

#### 2. `head` dan `tail` (Mengintip Ujung File)
Jika kamu hanya ingin tahu secara singkat format file tersebut tanpa harus membacanya:
- `head -n 10 namafile.txt` -> Hanya memunculkan **10 baris pertama** (Bagian atas file).
- `tail -n 10 namafile.txt` -> Hanya memunculkan **10 baris terakhir** (Sangat berguna untuk melihat *error* yang paling baru saja terjadi di server!).

---

### Perintah "Dewa": `grep`

Pernahkah kamu mencari kata "password" dari sebuah laporan Word yang panjang pakai `CTRL + F`?
Di Terminal, perintah itu disebut **`grep`** (Global Regular Expression Print).
Ini adalah salah satu tool paling mematikan dan sering dipakai oleh *hacker*.

Sintaks dasar: `grep "KataYangDicari" nama_file.txt`

**Contoh Kasus:**
Ada file laporan jaringan bernama `laporan.txt` dengan 5.000 baris teks. Kamu hanya butuh mencari kalimat yang mengandung kata "error".
```bash
$ grep "error" laporan.txt
```
Hasil: Terminal HANYA akan mencetak baris-baris spesifik yang di dalamnya ada kata "error", menghemat waktumu berjam-jam!

**Opsi canggih (sering ditanya saat interview kerja!):**
- `grep -i "error"` : Huruf besar/kecil tidak peduli (Case **i**nsensitive).
- `grep -r "password" /home/` : Mencari kata "password" di **semua file** dan **semua folder** yang ada di dalam direktori `/home`. (Ini jurus jitu mencari celah).

---

### Mencari Lokasi File: `find`

Terkadang kita tahu nama file-nya, tapi lupa menyimpannya di folder mana. (Kalau di Windows, ini fitur *Search Bar* di pojok atas).
Sintaks: `find [Lokasi_Mulai_Cari] -name "Nama_File"`

**Contoh Kasus:**
Kamu lupa di mana menyimpan file `rahasia.txt`.
```bash
$ find / -name "rahasia.txt"
```
Artinya: "Hai Linux, tolong periksa mulai dari akar sistem (`/`), dan temukan semua file yang persis bernama `rahasia.txt`." Linux akan menyisir ribuan folder dan menampilkan *path/lokasi* pastinya.

---

## 🧪 Mini Lab (Pipa / Piping)

**Durasi**: ~10 menit

Di Linux, ada sebuah keajaiban bernama **Pipe** yang disimbolkan dengan karakter garis lurus vertikal: `|` (Biasanya ada di atas tombol Enter, pakai tombol Shift).

Fungsi Pipe `|` adalah: **Mengambil hasil (output) dari perintah pertama, dan melemparnya sebagai bahan baku (input) untuk perintah kedua.**

Contoh penggabungan sakti yang sering dipakai:
```bash
$ ls -la /etc | grep "network"
```
**Apa yang terjadi?**
1. Perintah `ls -la /etc` menjebretkan ribuan baris nama file ke layar.
2. TAPI, bukannya dicetak ke layar, hasil ribuan nama itu ditangkap oleh simbol `|` (pipa), lalu dilempar masuk ke perut si `grep`.
3. `grep` akan menyaring ribuan nama itu dan **hanya mencetak ke layar** nama file yang ada kata "network"-nya.

*Pipe `|` adalah bukti kehebatan filosofi UNIX: Gabungkan alat-alat kecil untuk membuat mantra sakti!*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa seorang System Administrator lebih suka menggunakan perintah "tail" daripada "head" saat memeriksa file log kerusakan server web?</summary>

**Jawaban:** Karena file Log (*catatan histori server*) selalu menulis kejadian terbaru (paling *update*) di **baris paling bawah/akhir**. Dengan menggunakan `tail`, mereka langsung bisa melihat error spesifik yang menyebabkan server down 5 menit yang lalu, tanpa harus me-scroll file dari atas.

</details>

<details>
<summary>❓ Kamu mengetik perintah `grep "Admin" users.txt` tapi tidak ada hasil yang muncul. Padahal kamu yakin ada tu "admin" (dengan a kecil) di dalam file tersebut. Apa solusi perintahnya?</summary>

**Jawaban:** Gunakan flag `-i` (Case Insensitive) agar pencarian tidak memperdulikan huruf besar/kecil. Perintah yang benar adalah: `grep -i "Admin" users.txt`

</details>

<details>
<summary>❓ Apa fungsi dari simbol Pipa vertikal `|` di Linux Terminal?</summary>

**Jawaban:** Untuk meneruskan *output* (hasil) dari perintah di sebelah kiri Pipa, untuk digunakan langsung sebagai *input* (bahan bacaan) bagi perintah di sebelah kanan Pipa.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya hafal fungsi `less` (membaca dengan kursor)
- [ ] Saya hafal fungsi `head` dan `tail` (melihat ujung file)
- [ ] Saya paham kehebatan `grep` (mencari teks DI DALAM file)
- [ ] Saya hafal fungsi `find` (mencari LOKASI file)
- [ ] Saya mengerti logika penggabungan Pipa `|`
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Ryans Tutorials: Grep & Regular Expressions](https://ryanstutorials.net/linuxtutorial/grep.php) — Latihan dan penjelasan lebih mendalam soal `grep`.

---

## ➡️ Besok

**Day 5: Lab & Mission: Treasure Hunt di Terminal** — Saatnya terjun ke medan tempur! Besok kita akan melakukan instalasi *environment* Linux di komputermu, dan kamu akan memainkan permainan "Bandit" — tantangan *hacking* nyata di terminal Linux internasional!

---

*📅 TISS Null Teaming · Week 7 · Day 4 · PACKET Rank*
