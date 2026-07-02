# 📡 Week 7 · Day 2: File System (CLI)

> **Rank**: PACKET | **Minggu ke-7**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 7 · Day 2/5 | PACKET Rank (Minggu 3 dari 5) | Overall: 32/120 hari (27%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** hierarki File System Linux (mengapa tidak ada `C:\` dan `D:\`)
2. **Menemukan** lokasi saat ini dengan `pwd`
3. **Melihat** isi direktori dengan `ls`
4. **Berpindah** antar direktori menggunakan `cd`

---

## 📖 Materi Inti

### Pohon Kehidupan Linux: Root `/`

Di Windows, harddiskmu dibagi menjadi *drive* terpisah: `C:\`, `D:\`, `E:\`.
Di Linux, semuanya berawal dari satu titik induk yang disebut **Root**, disimbolkan dengan tanda garis miring (*Slash*): `/`

Bayangkan ini seperti pohon terbalik. `/` adalah akar utamanya.
Semua file, harddisk kedua, flashdisk, dan DVD-ROM yang dicolok akan menjadi cabang-cabang di bawah `/`. 

Beberapa cabang (direktori/folder) penting di bawah `/`:
- `/bin`: Berisi aplikasi dan perintah dasar sistem (seperti `ls`, `ping`).
- `/etc`: Berisi file konfigurasi. Kalau mau *hack* konfigurasi web server, cari di sini.
- `/var`: Berisi file yang ukurannya sering berubah-ubah (*variable*), seperti log *error* atau database.
- `/home`: Ini kamarmu! Setiap *user* punya kamar di sini. (Contoh: `/home/budi`). Kamu bebas berbuat apa pun di kamarmu tanpa merusak sistem.

---

### Tiga Perintah Suci 
Di Terminal, kamu buta. Kamu tidak punya *mouse* untuk melihat sekeliling. Kamu harus menggunakan 3 perintah (command) ini:

#### 1. `pwd` (Print Working Directory)
*Analogi: "GPS - Saya ada di mana sekarang?"*

Saat Terminal baru dibuka, ketik perintah ini untuk tahu lokasimu.
```bash
$ pwd
/home/ryo
```
Itu berarti kamu sedang berada di dalam folder `ryo` yang ada di dalam folder induk `home`.

#### 2. `ls` (List)
*Analogi: "Menyalakan Senter - Ada barang apa saja di ruangan ini?"*

Untuk melihat isi dari folder tempatmu berada, ketik `ls`.
```bash
$ ls
Desktop Documents Downloads Music
```

**Opsi/Flags tambahan (Sangat penting!):**
- `ls -l` (long format): Menampilkan detail lengkap (ukuran file, hak akses, tanggal edit).
- `ls -a` (all): Menampilkan file **tersembunyi** (file rahasia/konfigurasi yang namanya diawali dengan tanda titik, contoh: `.bashrc`).
- *Pro Tip:* Gabungkan keduanya menjadi `ls -la`. (Inilah perintah yang paling sering diketik *sysadmin*).

#### 3. `cd` (Change Directory)
*Analogi: "Berjalan/Pindah ke ruangan lain"*

- **Pindah ke dalam folder anak**: 
 `cd Documents` (Maju masuk ke folder Documents).
- **Pindah/Mundur ke folder bapak (naik 1 tingkat)**: 
 `cd..` (Titik dua kali artinya mundur 1 langkah ke atas).
- **Pulang ke rumah (Kamar awal `/home/user`)**:
 `cd ~` (Tanda cacing/tilde artinya *home directory*).
- **Pergi langsung ke ujung dunia (Absolute Path)**:
 `cd /var/log` (Pergi langsung ke folder log dari manapun kamu berada).

---

## 🧪 Mini Lab (Simulasi Otak)

**Durasi**: ~10 menit

Karena kita belum menginstal Linux, mari kita simulasikan perjalanan ini di kepalamu berdasarkan peta di atas!

**Skenario:**
Kamu baru saja membuka Terminal.
1. Ketik `pwd` -> Hasilnya: `/home/alice`
2. Ketik `cd /var/log` -> Kamu sekarang berada di folder Log.
3. Ketik `pwd` -> Hasilnya apa? (Tulis di catatanmu).
4. Di folder log ini, kamu ingin melihat SEMUA file, termasuk file *error* yang disembunyikan. Perintah apa yang harus diketik?
5. Setelah selesai ngecek, kamu ingin mundur 1 langkah agar berada di folder `/var`. Perintah apa yang kamu ketik?
6. Terakhir, kamu ingin pulang cepat ke `/home/alice`. Perintah rahasia apa yang kamu ketik?

<details>
<summary>🔑 Kunci Jawaban Simulasi</summary>

3. Hasil `pwd` adalah `/var/log`
4. Perintahnya adalah `ls -la` (atau `ls -a`)
5. Mundur 1 tingkat menggunakan `cd..`
6. Pulang instan menggunakan `cd ~`

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Di OS Windows, file sistem utama ada di C:\Windows. Di manakah folder utama awal/induk dari seluruh file pada sistem operasi Linux?</summary>

**Jawaban:** Di **Root directory**, yang hanya dilambangkan dengan simbol slash: `/`.

</details>

<details>
<summary>❓ Kamu mengetik perintah "ls" tapi tidak melihat file rahasia bernama ".env". Mengapa demikian dan bagaimana cara memunculkannya?</summary>

**Jawaban:** Di Linux, semua file atau folder yang namanya diawali dengan tanda titik (`.`) secara otomatis akan disembunyikan. Untuk melihatnya, kamu harus menambahkan *flag/opsi* all, yaitu mengetik `ls -a` atau `ls -la`.

</details>

<details>
<summary>❓ Apa yang terjadi jika kamu mengetik perintah `cd /` (dengan tanda slash)? Apakah kamu akan pulang ke Home atau ke tempat lain?</summary>

**Jawaban:** Kamu akan berpindah ke folder **Root** (induk paling atas dari sistem komputer). Ini BUKAN folder Home-mu (`~`). Di folder Root ini kamu akan melihat direktori-direktori inti sistem operasi seperti `bin`, `etc`, dan `var`.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami struktur file sistem Linux yang berakar di `/` (Root)
- [ ] Saya tahu isi folder `/home`, `/etc`, dan `/var`
- [ ] Saya hafal fungsi perintah `pwd`
- [ ] Saya hafal fungsi `ls` dan opsi `-la`
- [ ] Saya hafal fungsi `cd` beserta tanda `..` (mundur) dan `~` (pulang)
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Linux File Hierarchy Structure Explained](https://www.howtogeek.com/117435/htg-explains-the-linux-directory-structure-explained/) — Penjelasan lengkap fungsi setiap folder "aneh" yang ada di bawah `/` Linux.

---

## ➡️ Besok

**Day 3: Manipulasi File & Direktori** — sudah jago. Besok kita akan mulai **beraksi**! Kita akan belajar cara membuat folder baru, membuat file teks kosong, hingga menyalin dan menghapus file tanpa ampun menggunakan Terminal. 💥

---

*📅 TISS Null Teaming · Week 7 · Day 2 · PACKET Rank*
