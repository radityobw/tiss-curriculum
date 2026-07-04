# 📡 Week 8 · Day 2: File Permissions (rwx)

> **Rank**: PACKET | **Minggu ke-8**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 8 · Day 2/5 | PACKET Rank (Minggu 4 dari 5) | Overall: 37/120 hari (30%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membaca** dan menerjemahkan output perizinan dari `ls -l`
2. **Memahami** makna dari blok hak akses: *User*, *Group*, dan *Others*
3. **Mengerti** operasi matematika sederhana (4, 2, 1) di balik *Read, Write, Execute* (rwx)
4. **Mengubah** hak akses file menggunakan perintah `chmod`

---

## 📖 Materi Inti

### Membaca Sandi Rahasia: `ls -l`

Minggu lalu kamu belajar menggunakan perintah `ls -l` (list long-format) untuk melihat detail file.
Hasilnya biasanya terlihat seperti ini:

```bash
-rwxr-xr-- 1 alice staff 2048 Mar 12 10:00 tugas.txt
```

Bagi pemula, deretan aneh `-rwxr-xr--` di awal baris terlihat seperti teks error. Padahal, 10 karakter ini adalah **Kunci Keamanan Linux**. Ini menentukan siapa yang boleh membaca atau mengedit file tersebut.

Mari kita bedah 10 karakter tersebut menjadi 4 blok:
`[ - ] [ rwx ] [ r-x ] [ r-- ]`

#### Blok 1: Tipe File (Karakter ke-1)
- `-` : File biasa (teks/gambar/program).
- `d` : Direktori (Folder).

#### 3 Blok Hak Akses (Karakter ke-2 sampai 10)
Sisa 9 karakter dibagi menjadi 3 blok yang masing-masing terdiri dari 3 huruf.

1. **Blok 2 (rwx)**: Hak untuk si Pemilik Asli (*Owner/User*).
2. **Blok 3 (r-x)**: Hak untuk anggota Grup si Pemilik (*Group*).
3. **Blok 4 (r--)**: Hak untuk orang lain di luar sana (*Others / Everyone else*).

### Arti Huruf: R, W, X

Setiap blok diisi oleh 3 status: **Read (r)**, **Write (w)**, dan **Execute (x)**. Jika hak itu dilarang/dicabut, hurufnya diganti dengan tanda strip (`-`).

- **r (Read)**: Boleh membaca isi file (atau melihat isi folder dengan `ls`).
- **w (Write)**: Boleh memodifikasi, mengedit, atau menghapus file.
- **x (Execute)**: Boleh "menjalankan" file tersebut sebagai program/aplikasi (sangat bahaya jika diberikan sembarangan!).

**Analisis contoh kita tadi: `-rwxr-xr--`**
- File biasa (`-`)
- Pemiliknya (*alice*) boleh baca, tulis, eksekusi (`rwx`)
- Teman satu grupnya (*staff*) boleh baca & eksekusi, TAPI dilarang ngedit (`r-x`)
- Orang lain (*others*) cuma boleh baca doang (`r--`)

### Matematika Keamanan (Nilai Oktal)

Setiap huruf memiliki nilai angka ajaib agar mudah diingat oleh sistem:
- **r** = 4
- **w** = 2
- **x** = 1
- **-** = 0

Jika kamu ingin memberikan hak **Read + Write** saja, kamu cukup menjumlahkannya: 4 + 2 = **6**.
Jika kamu ingin memberikan **Full Akses (rwx)**, kamu jumlahkan: 4 + 2 + 1 = **7**.

### Mengubah Hak Akses: `chmod` (Change Mode)

Sebagai pemilik file, kamu bisa mengubah izin file dengan perintah `chmod` menggunakan format angka (Oktal) tadi. Kamu harus memasukkan 3 angka sekaligus (untuk User, Group, dan Others).

**Contoh Skenario:**
Kamu ingin membuat file `tugas.txt` punya izin: Pemilik bisa baca-tulis (6), Grup tidak bisa apa-apa (0), Orang lain tidak bisa apa-apa (0).

```bash
$ chmod 600 tugas.txt
```
Maka hak aksesnya akan berubah menjadi: `-rw-------`. Ini adalah izin standar untuk file sangat rahasia (seperti kunci privat *password*).

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Ambil selembar kertas atau buka notes, dan selesaikan translasi izin file berikut ini bolak-balik (Teks <-> Angka).

1. Ubah teks ini menjadi 3 digit angka oktal: `rwxr-xr-x`
2. Ubah teks ini menjadi 3 digit angka oktal: `rw-r--r--`
3. Apa wujud teks (rwx) dari perintah ini: `chmod 777 rahasia.txt`
4. Mengapa izin `777` dianggap sebagai "Dosa Besar" di dunia *cybersecurity*?

<details>
<summary>🔑 Kunci Jawaban & Pembahasan</summary>

1. `rwxr-xr-x` = (4+2+1) (4+0+1) (4+0+1) = **755**. (Ini izin default untuk program/aplikasi).
2. `rw-r--r--` = (4+2+0) (4+0+0) (4+0+0) = **644**. (Ini izin default untuk file teks biasa).
3. `777` = `rwxrwxrwx` (Full akses untuk semuanya).
4. Karena `777` mengizinkan **Semua orang di dunia (Others)** untuk Membaca, Mengedit, bahkan Mengeksekusi file tersebut layaknya program. Jika itu file server web, *hacker* tamu manapun bisa menimpa (*write*) file tersebut dengan virus lalu menjalankannya (*execute*).

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Kamu menemukan sebuah program dengan izin `-rwxr-xr--`. Apakah anggota "Others" (orang luar) bisa menjalankan program tersebut?</summary>

**Jawaban:** **Tidak bisa**. Karena di blok terakhir (Others) hanya berisi `r--`. Hak eksekusinya (`x`) dicabut (ditandai dengan strip `-`).

</details>

<details>
<summary>❓ Perintah apa yang akan kamu gunakan untuk memberikan izin "rwx" HANYA kepada si pemilik file, dan mematikan semua izin untuk grup dan orang lain (menjadikannya 0)?</summary>

**Jawaban:** `chmod 700 namafile.txt`

</details>

<details>
<summary>❓ Apa arti huruf "d" di ujung paling kiri sebuah output `ls -l`, misalnya `drwxr-xr-x`?</summary>

**Jawaban:** Huruf "d" menandakan bahwa item tersebut bukanlah file biasa, melainkan sebuah **Directory (Folder)**.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya paham membedah 10 karakter awal output `ls -l`
- [ ] Saya hafal pembagian 3 blok: User, Group, Others
- [ ] Saya hafal nilai matematika r=4, w=2, x=1
- [ ] Saya tahu bahayanya izin 777 (Dilarang keras dipakai sembarangan!)
- [ ] Saya bisa mempraktikkan pengubahan izin file menggunakan perintah `chmod`
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Chmod Calculator (Web)](https://chmod-calculator.com/) — Alat bantu visual interaktif untuk melihat perubahan `rwx` saat kamu memasukkan angka `chmod`.

---

## ➡️ Besok

**Day 3: Ownership & Privilege Escalation** — Hak akses (`rwx`) tidak ada gunanya jika kamu bukan "Pemilik" (Owner) dari file tersebut. Besok kita akan belajar perintah yang bisa meng-override semua aturan hak akses: `sudo`. Bersiaplah meminjam kekuatan Root!

---

*📅 TISS Null Teaming · Week 8 · Day 2 · PACKET Rank*
