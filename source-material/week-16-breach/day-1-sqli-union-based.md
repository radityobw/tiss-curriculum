# 💀 Week 16 · Day 1: SQL Injection UNION-based

> **Rank**: BREACH | **Minggu ke-16**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 16 · Day 1/5 | BREACH Rank (Minggu 2 dari 5) | Overall: 76/120 hari (63%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** cara kerja serangan *SQL Injection* tingkat lanjut yang menggunakan perintah `UNION`.
2. **Mengekstraksi** data rahasia dari *database* menggunakan teknik *Column Enumeration*.
3. **Mensimulasikan** serangan *UNION-based SQLi* secara manual tanpa menggunakan *tools* otomatis.

---

## 📖 Materi Inti

### Memasuki Ruang Eksploitasi (Web Exploitation)

Di minggu sebelumnya, kamu telah menyelesaikan tahapan pengumpulan informasi (*Reconnaissance*). Mulai tahap ini, kita akan melakukan eksploitasi! Kita akan mulai dengan salah satu kerentanan web paling fundamental dan berbahaya: **SQL Injection (SQLi)**.

Pada Rank *Forge*, kamu telah belajar melakukan *bypass login* menggunakan *payload* sederhana seperti `' OR 1=1 --`. Hari ini, kita akan mempelajari teknik eksploitasi yang lebih mematikan, yang dapat digunakan untuk mencuri seluruh isi *database*: **UNION-based SQL Injection**. 

### Menggabungkan Tabel (UNION SELECT)

Bayangkan kamu sedang mengunjungi sebuah toko *online*. Saat kamu memilih kategori "Kemeja", URL aplikasi mungkin terlihat seperti ini:
`https://toko.com/produk?kategori=kemeja`

Di belakang layar, *database* akan menjalankan kueri (perintah SQL) pencarian seperti ini:
`SELECT nama, harga FROM tabel_produk WHERE kategori = 'kemeja'`

Jika parameter input (*user input*) tersebut tidak disaring dengan benar (*sanitization*), seorang penyerang dapat menyisipkan perintah SQL tambahan bernama `UNION`. Perintah `UNION` dalam SQL digunakan untuk menggabungkan hasil dari dua perintah `SELECT` yang berbeda ke dalam satu tabel hasil.

Bagaimana jika kita menggabungkan hasil pencarian produk kemeja dengan hasil pencarian dari tabel *users* (yang berisi *username* dan *password*)?

Penyerang dapat memasukkan *payload* ke dalam URL:
`https://toko.com/produk?kategori=kemeja' UNION SELECT username, password FROM users --`

Kueri yang dieksekusi oleh *database* akan menjadi:
`SELECT nama, harga FROM tabel_produk WHERE kategori = 'kemeja' UNION SELECT username, password FROM users --'`

Hasilnya? Halaman web tersebut tidak hanya akan menampilkan daftar kemeja, tetapi juga akan membocorkan daftar *username* dan *password* dari tabel `users` ke layar!

### Syarat Struktural UNION (Column Enumeration)

Metode serangan ini memiliki satu syarat mutlak: **Kueri `UNION SELECT` yang disisipkan harus memiliki jumlah kolom yang SAMA PERSIS dengan kueri aslinya!**

Jika kueri aslinya memanggil 2 kolom (`nama`, `harga`), maka *payload* injeksi kita juga harus memanggil tepat 2 kolom.

Jika kita tidak tahu berapa jumlah kolom aslinya, kita harus menebaknya. Proses menebak jumlah kolom ini disebut **Column Enumeration**. Ada dua cara umum: menggunakan `ORDER BY` atau `NULL`.

Contoh menggunakan `ORDER BY`:
- `' ORDER BY 1 --` (Web merespons normal)
- `' ORDER BY 2 --` (Web merespons normal)
- `' ORDER BY 3 --` (Web menampilkan pesan galat *Error*! Ini berarti tabel aslinya hanya memiliki 2 kolom).

Setelah mengetahui bahwa ada 2 kolom, penyerang bisa langsung melakukan pencurian data:
- `' UNION SELECT null, database() --` (Untuk mengetahui nama *database* yang sedang digunakan).
- `' UNION SELECT username, password FROM users --` (Untuk mencuri data *user*).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan analisis kerentanan pemetaan jumlah dimensi tabel peladen kueri secara manual!

1. Kunjungi pelataran lingkungan lab kompetisi *Bug Bounty*: [PortSwigger Academy: SQL Injection](https://portswigger.net/web-security/sql-injection).
2. Temukan modul *SQL Injection* dasar yang memiliki kerentanan pada URL (misalnya pada parameter kategori produk).
3. Cobalah mencari jumlah kolom menggunakan teknik *NULL Enumeration*:
 - `kategori=Gifts' UNION SELECT NULL--` (Situs error)
 - `kategori=Gifts' UNION SELECT NULL,NULL--` (Situs error)
 - `kategori=Gifts' UNION SELECT NULL,NULL,NULL--` (Situs tampil normal tanpa *error*!)
4. Dari percobaan tersebut, kamu mengetahui bahwa tabel aslinya memiliki **3 kolom**.
5. Langkah selanjutnya, kamu bisa mengekstrak data dari tabel lain dengan *payload* seperti: `kategori=Gifts' UNION SELECT username, password, email FROM users--`!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam bahasa SQL, apa fungsi dari perintah <i>UNION</i>?</summary>

**Jawaban:** Fungsi `UNION` digunakan untuk menggabungkan hasil dari dua perintah `SELECT` (atau lebih) ke dalam satu hasil tampilan tabel (*Result Set*).
</details>

<details>
<summary>❓ Apa syarat mutlak yang harus dipenuhi agar serangan <i>UNION-based SQL Injection</i> bisa berhasil dan tidak memicu pesan galat (<i>Error</i>)?</summary>

**Jawaban:** Jumlah kolom pada kueri `UNION SELECT` yang disisipkan oleh penyerang harus **sama persis** dengan jumlah kolom pada kueri aslinya.
</details>

<details>
<summary>❓ Teknik apa yang digunakan oleh penyerang dengan cara menginjeksi perintah seperti <code>' ORDER BY 1 --</code>, <code>' ORDER BY 2 --</code>, secara berurutan hingga menemukan <i>error</i>, untuk menebak jumlah kolom pada tabel target?</summary>

**Jawaban:** *Column Enumeration* (menggunakan *ORDER BY*).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami cara kerja serangan *UNION-based SQLi*.
- [ ] Saya mengerti syarat jumlah kolom yang harus sama saat menggunakan *UNION*.
- [ ] Saya paham cara melakukan *Column Enumeration* (menggunakan *ORDER BY* atau *NULL*).
- [ ] Saya telah membaca dan memahami skenario eksekusi *UNION SQLi* di *Mini Lab*.
- [ ] Saya telah menjawab pertanyaan di *Quiz Kilat* dengan benar.

---

## 🔗 Resources

- [PortSwigger UNION Attacks](https://portswigger.net/web-security/sql-injection/union-attacks) — Panduan teori dan praktik (Lab) komprehensif mengenai peretasan aplikasi web menggunakan *SQL UNION*.

---

## ➡️ Besok

**Day 2: SQL Injection Blind (Boolean & Time)** — Apa yang terjadi jika situs target memiliki kerentanan SQLi, tetapi **tidak pernah menampilkan hasil** dari kueri *database* ke layar halaman web? Apakah kita masih bisa mencuri datanya? Jawabannya: BISA! Teknik ini disebut **Injeksi Buta (Blind SQLi)**. Besok, kamu akan mempelajari cara mencuri data *database* walaupun layar tidak menampilkan hasil kueri apa pun, yaitu dengan memanfaatkan respons *True/False* (*Boolean-based*) dan jeda waktu (*Time-based*).

---

*📅 TISS Null Teaming · Week 16 · Day 1 · BREACH Rank*
