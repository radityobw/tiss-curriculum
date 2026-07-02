# 📡 Week 7 · Day 3: Manipulasi File & Direktori

> **Rank**: PACKET | **Minggu ke-7**, Hari 3/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 7 · Day 3/5 | PACKET Rank (Minggu 3 dari 5) | Overall: 33/120 hari (28%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membuat** file dan direktori baru (`touch`, `mkdir`)
2. **Membaca** isi file langsung dari terminal (`cat`)
3. **Menyalin dan Memindahkan** file (`cp`, `mv`)
4. **Menghapus** file dan direktori (`rm`, `rmdir`)

---

## 📖 Materi Inti

### Aksi di Terminal (CRUD via CLI)

Kemarin kamu hanya "berjalan-jalan" di terminal. Sekarang kamu akan melakukan modifikasi. Hati-hati, di Linux CLI **tidak ada tong sampah (Recycle Bin)**. Sekali dihapus, hilang selamanya!

#### 1. Membuat Folder: `mkdir` (Make Directory)
Alih-alih *Klik Kanan -> New Folder*, gunakan:
```bash
$ mkdir HackingTools
```
Ini akan membuat folder bernama `HackingTools` di lokasi saat ini.

#### 2. Membuat File Kosong: `touch`
*Tool* tercepat untuk membuat file tanpa harus membuka aplikasi editor (seperti Notepad):
```bash
$ touch rahasia.txt
```
Ini akan menciptakan file kosong bernama `rahasia.txt`. (Jika file itu sudah ada sebelumnya, `touch` hanya akan memperbarui cap waktu/tanggal terakhir diakses, tanpa menghapus isinya).

#### 3. Membaca Isi File: `cat` (Concatenate)
Jika kamu mau membaca isi `rahasia.txt` tanpa menggunakan *mouse* atau membuka aplikasi baru, semburkan saja isi teksnya ke layar Terminal:
```bash
$ cat rahasia.txt
```
*Note: Jangan gunakan `cat` pada file yang sangat panjang atau file video (.mp4)! Layarmu akan dipenuhi karakter aneh tak berujung.*

#### 4. Meng-Copy File: `cp` (Copy)
Sintaks dasar: `cp [Yang mau di-copy] [Tempat tujuan]`
```bash
$ cp rahasia.txt HackingTools/
```
Ini meng-copy file `rahasia.txt` dan memasukkannya ke dalam folder `HackingTools/`. 
*(Jika ingin mengcopy FOLDER berserta seluruh isinya, tambahkan `-r` (recursive): `cp -r HackingTools/ /tmp/`)*.

#### 5. Memindahkan File (Cut / Rename): `mv` (Move)
`mv` punya 2 fungsi ganda!
- **Fungsi Cut/Pindah**: `mv rahasia.txt /home/budi/Documents/`
- **Fungsi Rename**: Jika file asal dan tujuan ada di folder yang sama, perintah ini bertindak sebagai *Rename*.
 ```bash
 $ mv rahasia.txt laporan.txt
 ```
 *(Ini mengubah nama `rahasia.txt` menjadi `laporan.txt`)*.

#### 6. Menghapus File: `rm` (Remove)
Hati-hati dengan perintah ini!
```bash
$ rm laporan.txt
```
Untuk menghapus **folder yang ada isinya**, gunakan tambahan `-r` (recursive):
```bash
$ rm -r HackingTools/
```

> ⚠️ **DOSA BESAR LINUX**: Jangan pernah sesekali mengetik `rm -rf /` di server. Itu artinya *"Hapus secara paksa (f) seluruh isinya sampai ke akar (r) dimulai dari Root (/)."* Komputermu akan bunuh diri dalam 5 detik dan sistem operasimu musnah!

---

## 🧪 Mini Lab (Simulasi Otak)

**Durasi**: ~10 menit

Mari bermain *puzzle* logika Terminal!
Saat ini kamu berada di `/home/user`. Lacak apa yang terjadi jika 4 baris perintah ini dijalankan berurutan:

```bash
1. mkdir rahasia
2. cd rahasia
3. touch password.txt
4. mv password.txt../kunci.txt
```

**Pertanyaan:**
A. Setelah baris ke-4 selesai, file bernama `password.txt` akan hilang/ganti nama. Benar atau salah?
B. Di folder manakah file `kunci.txt` sekarang berada? (Petunjuk: ingat fungsi `..`)

<details>
<summary>🔑 Kunci Jawaban</summary>

A. **Benar**. Baris ke-4 menggunakan `mv`, yang bertindak memindahkan file sekaligus merename-nya. File `password.txt` lenyap.
B. **`/home/user`**. Karena dari dalam folder `rahasia/`, tujuan pindahnya adalah `../` (mundur 1 tingkat), sehingga file dilempar kembali keluar ke `home/user` dan diberi nama baru `kunci.txt`.

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Kamu tidak sengaja menggunakan perintah `rm laporan-skripsi.docx`. Bagaimana cara mengambilnya kembali dari Recycle Bin / Trash?</summary>

**Jawaban:** **Tidak bisa (secara default)**. Perintah `rm` di Terminal akan menghancurkan pointer file secara instan dan mem-bypass keranjang sampah (Trash). Selalu berhati-hati sebelum menekan Enter pada perintah penghapusan!

</details>

<details>
<summary>❓ Mengapa kita sering menggunakan perintah `touch` padahal file-nya akan kosong?</summary>

**Jawaban:** Dalam dunia administrasi sistem atau *scripting*, kita sering membutuhkan *placeholder* (tempat file) terlebih dahulu sebelum *script* otomatis lainnya mulai mengisi data ke dalam file tersebut, atau sekadar untuk mengetes apakah kita punya hak akses (Permission) untuk membuat file di direktori tersebut.

</details>

<details>
<summary>❓ Apa fungsi bendera/flag `-r` pada perintah `cp -r` atau `rm -r`?</summary>

**Jawaban:** `-r` singkatan dari **Recursive**. Ini berarti perintah tidak hanya mengenai folder target, tapi juga *masuk masuk dan memengaruhi seluruh file dan folder anak-anak yang ada di dalamnya*. Tanpa `-r`, kamu tidak akan bisa meng-copy atau menghapus sebuah folder jika di dalamnya ada isinya.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya hafal fungsi `mkdir` (Make Directory)
- [ ] Saya hafal fungsi `touch` (Make File)
- [ ] Saya hafal fungsi `cat` (Read File)
- [ ] Saya hafal perbedaan `cp` (Copy) dan `mv` (Move/Rename)
- [ ] Saya paham bahayanya perintah `rm` dan opsi `-r`
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Linux Command Line Cheat Sheet (PDF)](https://www.stationx.net/linux-command-line-cheat-sheet/) — Simpan gambar/PDF contekan ini di HP-mu. Kamu akan sangat sering menggunakannya.

---

## ➡️ Besok

**Day 4: Membaca & Mencari File** — Jika `cat` digunakan untuk file pendek, bagaimana cara membaca file Log error server yang panjangnya 500.000 baris? Besok kita belajar ilmu pamungkas: `less`, `grep`, dan `find`.

---

*📅 TISS Null Teaming · Week 7 · Day 3 · PACKET Rank*
