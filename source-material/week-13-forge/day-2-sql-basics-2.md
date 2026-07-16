# 🔨 Week 13 · Day 2: SQL Basics (Bagian 2)

> **Rank**: FORGE | **Minggu ke-13**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 13 · Day 2/5 | FORGE Rank (Minggu 4 dari 5) | Overall: 62/120 hari (51%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memperbarui** dan memodifikasi data serta menghapus baris dari tabel (*UPDATE* & *DELETE*).
2. **Memahami** konsep normalisasi dan pembentukan hubungan (*Relationships*) antar-tabel.
3. **Menggabungkan** data dari dua tabel terpisah menggunakan klausa `JOIN`.

---

## 📖 Materi Inti

### Modifikasi Data Lanjutan: UPDATE & DELETE

Melengkapi siklus *CRUD* dari materi sebelumnya, kini saatnya kita mendalami cara memodifikasi data.

**1. Mengganti atau Memperbarui Data (UPDATE)**
```sql
UPDATE pengguna 
SET umur = 26 
WHERE username = 'ryocantsleep';
```
> ⚠️ **IMPORTANT:** Jika kamu lupa menyematkan kondisi `WHERE`, instruksi `UPDATE pengguna SET umur = 26;` akan dieksekusi ke **SELURUH PENGGUNA**. Akibatnya, umur semua pengguna di tabel tersebut akan berubah menjadi `26`. Ini adalah kesalahan fatal yang sering disebut *tragedy of missing where clause*.

**2. Menghapus Data (DELETE)**
```sql
DELETE FROM pengguna 
WHERE username = 'ryocantsleep_v2';
```
*(Sama seperti operasi Update, jika kamu tidak menyertakan klausa `WHERE`, maka seluruh data di dalam tabel akan terhapus bersih!)*

### Konsep Relasional pada Basis Data (Normalisasi)

Mengapa basis data RDBMS (seperti *MySQL, PostgreSQL, atau SQLite*) dijuluki dengan istilah *"Relational"*?

Bayangkan sistem pencatatan pada sebuah situs e-commerce. Alih-alih menggabungkan semua data (identitas pengguna, alamat, rincian produk, transaksi) ke dalam **Satu Tabel Raksasa**, perancang database memecahnya menjadi beberapa tabel yang lebih kecil dan terstruktur. Proses ini dikenal sebagai **Normalisasi**.

Misalnya, kita memisahkan Tabel `users` (khusus untuk data pelanggan) dan Tabel `pesanan` (khusus untuk data transaksi).
Kedua tabel ini dihubungkan menggunakan sebuah kolom referensi. Kolom penaut antar-tabel ini disebut sebagai **Foreign Key** (Kunci Tamu).

### Menggabungkan Data Antar Tabel (JOIN)

Ketika data akan ditampilkan ke pengguna, kita perlu menggabungkannya agar mudah dibaca, bukan sekadar menampilkan deretan angka ID. Database harus merangkai ulang data dari tabel `users` dan `pesanan` menggunakan perintah **JOIN**.

```sql
SELECT users.nama, pesanan.total_harga 
FROM users
JOIN pesanan ON users.id = pesanan.user_id;
```
*(Sintaks `JOIN` ini menginstruksikan SQL untuk menyatukan baris dari tabel 'users' dan 'pesanan' asalkan nilai `id` pada tabel users cocok dengan nilai `user_id` pada tabel pesanan).*

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari buat arsitektur tabel berelasi dan jalankan instruksi `JOIN` pertamamu!

1. Kunjungi kembali platform [DB Fiddle (SQLite)](https://www.db-fiddle.com/).
2. Di panel **Schema (kiri)**, buat dua tabel yang saling berelasi:
```sql
CREATE TABLE divisi (
 id INTEGER PRIMARY KEY,
 nama_divisi VARCHAR(50)
);

CREATE TABLE anggota (
 id INTEGER PRIMARY KEY,
 nama VARCHAR(50),
 divisi_id INTEGER -- Sebagai Foreign Key
);

INSERT INTO divisi (id, nama_divisi) VALUES (1, 'Tim Inti Backend');
INSERT INTO divisi (id, nama_divisi) VALUES (2, 'Tim Analis Data');

INSERT INTO anggota (nama, divisi_id) VALUES ('Administrator Utama', 1);
INSERT INTO anggota (nama, divisi_id) VALUES ('Teknisi Jaringan', 2);
```

3. Beralih ke panel **Query (kanan)**, jalankan kueri `JOIN` untuk menggabungkan data tersebut:
```sql
-- Menggabungkan nama staf dengan nama divisinya
SELECT anggota.nama, divisi.nama_divisi
FROM anggota
JOIN divisi ON anggota.divisi_id = divisi.id;
```
4. Tekan tombol **Run**! Periksa panel *Results* di bagian bawah. Kueri `JOIN` sukses mengubah angka ID `divisi_id` menjadi nama divisi yang bisa dibaca.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Konsekuensi fatal apa yang terjadi jika kita menjalankan perintah SQL `DELETE FROM pengguna;` tanpa menyertakan klausa kondisi `WHERE`?</summary>

**Jawaban:** Tanpa klausa `WHERE`, SQL akan mengeksekusi perintah penghapusan pada **SELURUH** baris di tabel `pengguna`, yang berakibat hilangnya semua data di dalam tabel tersebut.
</details>

<details>
<summary>❓ Mengapa kita harus memecah data menjadi tabel-tabel kecil (Normalisasi) dibanding menyimpannya dalam satu tabel raksasa?</summary>

**Jawaban:** Untuk mencegah pengulangan data yang tidak perlu (reduplikasi/redundansi). Jika semua data digabung dalam satu tabel besar, informasi seperti profil pengguna akan dicatat berulang kali setiap kali ia berbelanja. Dengan memisahkan tabel (normalisasi), data profil *user* cukup disimpan satu kali saja, sementara tabel pesanan hanya perlu merujuk pada nomor ID pengguna tersebut (*Foreign Key*).
</details>

<details>
<summary>❓ Perintah SQL apa yang digunakan untuk menggabungkan data dari dua tabel terpisah berdasarkan kecocokan kolom Foreign Key?</summary>

**Jawaban:** Klausa `JOIN`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya paham bahayanya menjalankan perintah `UPDATE` atau `DELETE` tanpa klausa `WHERE`.
- [ ] Saya mampu menjelaskan kegunaan *Foreign Key* pada basis data relasional.
- [ ] Saya telah mempraktikkan penggabungan dua tabel menggunakan klausa `JOIN`.
- [ ] Saya sukses menyelesaikan *Mini Lab SQLite*.
- [ ] Saya telah meninjau *Quiz Kilat*.

---

## 🔗 Resources

- [SQL Joins Visualizer](https://sql-joins.leopard.in.ua/) — Tool interaktif berbasis Venn Diagram yang sangat berguna untuk memahami perbedaan fungsi `LEFT JOIN`, `INNER JOIN`, dan `RIGHT JOIN`.

---

## ➡️ Besok

**Day 3: Database di Node.js** — Sejauh ini, kamu baru menjalankan kueri SQL secara manual di sandbox. Besok, kita akan mengintegrasikan database ini dengan aplikasi *Node.js Backend*. Kamu akan belajar bagaimana membuat kode JavaScript yang secara otomatis mengirimkan perintah SQL untuk berinteraksi dengan database sungguhan!

---

*📅 TISS Null Teaming · Week 13 · Day 2 · FORGE Rank*
