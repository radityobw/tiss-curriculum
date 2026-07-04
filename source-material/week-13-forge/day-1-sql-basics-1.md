# 🔨 Week 13 · Day 1: SQL Basics (Bagian 1)

> **Rank**: FORGE | **Minggu ke-13**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 13 · Day 1/5 | FORGE Rank (Minggu 4 dari 5) | Overall: 61/120 hari (50%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep Relational Database (Basis Data Relasional) dan posisinya di Backend.
2. **Menulis** kueri SQL dasar untuk merakit tulang tabel (`CREATE TABLE`).
3. **Mengekstrak** dan **Menyisipkan** data spesifik menggunakan `SELECT`, `INSERT`, `WHERE`, dan `ORDER BY`.

---

## 📖 Materi Inti

### Mengakhiri Era Amnesia: Mengapa Butuh Database?

Minggu lalu, API buatanmu terserang amnesia. Begitu server Node.js di-restart, semua catatan hilang karena kita menyimpannya di memori sementara (RAM/Array). Untuk keabadian data, kita butuh **Database (Basis Data)**.

Database ibarat lemari arsip baja super besar. Salah satu jenis terkuat dan paling tua di dunia pemrograman adalah **RDBMS (Relational Database Management System)**, contohnya MySQL, PostgreSQL, dan SQLite. Di RDBMS, data disimpan dalam bentuk **Tabel** (seperti Microsoft Excel), bersusun rapi dalam baris (*rows*) dan kolom (*columns*).

### Berkomunikasi dengan Lemari Arsip: Bahasa SQL

Untuk memerintah lemari ini, kita tidak menggunakan JavaScript. Kita harus memakai bahasa purba bernama **SQL (Structured Query Language)**.
SQL adalah bahasa standar untuk menguasai basis data. Bagi *hacker*, menguasai SQL adalah jalan ninja untuk melancarkan serangan mematikan: **SQL Injection**.

#### 1. Menciptakan Kerangka Tabel (CREATE)
```sql
CREATE TABLE pengguna (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 username VARCHAR(50) NOT NULL,
 umur INTEGER
);
```
*(Membuat cetakan tabel bernama `pengguna`. `id` akan terisi otomatis, `username` teks maksimal 50 huruf tak boleh kosong).*

#### 2. Menyisipkan Data (INSERT)
```sql
INSERT INTO pengguna (username, umur) 
VALUES ('ZeroCool', 25), ('CrashOverride', 22);
```

#### 3. Membaca dan Mengekstrak (SELECT)
Ini adalah mantra yang paling sering kamu ketik! Tanda bintang `*` artinya "Pilih SEMUA kolom".
```sql
-- Minta daftar semua pengguna tanpa filter
SELECT * FROM pengguna;

-- Minta cuma nama dari pengguna yang umurnya di atas 20
SELECT username FROM pengguna WHERE umur > 20;

-- Mengurutkan berdasarkan umur dari tertua ke termuda (Descending)
SELECT * FROM pengguna ORDER BY umur DESC;
```

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari praktekkan SQL tanpa instalasi berat! Kita akan pakai web SQL *sandbox*.

1. Buka peramban, kunjungi alat tes SQL interaktif: [DB Fiddle (SQLite)](https://www.db-fiddle.com/)
2. Pastikan mesin di kiri atas terpilih "SQLite".
3. Di panel **Schema SQL** (kiri), ketikkan kodingan pembangunan kerangka:
```sql
CREATE TABLE intel (
 id INTEGER PRIMARY KEY,
 kode_agen VARCHAR(10),
 status VARCHAR(20)
);

INSERT INTO intel (kode_agen, status) VALUES ('007', 'Aktif');
INSERT INTO intel (kode_agen, status) VALUES ('006', 'MIA');
INSERT INTO intel (kode_agen, status) VALUES ('47', 'Aktif');
```
4. Di panel **Query SQL** (kanan), perintahkan ekstraksi:
```sql
-- Mari melacak daftar agen yang masih bernapas
SELECT kode_agen FROM intel WHERE status = 'Aktif';
```
5. Tekan tombol **Run** (Pojok kiri atas). 
6. Lihat balasan tabel di kolom bawah! Agen 007 dan 47 sukses diekstrak.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa ekosistem data <i>Relational</i> menduduki peringkat sangat vital untuk kelangsungan daya ingat abadi sistem <i>Backend</i> API ketimbang mengandalkan array memori JavaScript?</summary>

**Jawaban:** memori variabel Array di JavaScript berwatak amnesia statis sesaat (In-Memory). Begitu denyut *server Node* macet atau di-restart, segenap tampungan payload menguap raib ditelan kekosongan. Sebaliknya, Database (data) membekukan memahat payload secara permanen merasuk fisik kepingan penyimpanan harddisk (*Storage*).
</details>

<details>
<summary>❓ Atribut mantra krusial kueri simbol karakter apakah yang disisipkan lekat bersampingan `SELECT` guna mendaulat permintaan ekstraksi brutal menyedot SEMUA kolom utuh tanpa pengecualian?</summary>

**Jawaban:** Karakter tanda Bintang (Asterisk) alias `*` (misal `SELECT * FROM`).
</details>

<details>
<summary>❓ Tuas operasi klausa sandi perintah kueri manakah di lintasan pembacaan `SELECT` yang dipercaya spesifik mengeksekusi penyaringan (*filtering*) kondisi seperti *"Cuma comot data jika umurnya melebihi 20"*?</summary>

**Jawaban:** Titah kondisi `WHERE` (contohnya `WHERE umur > 20`).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap urgensi data demi keabadian payload API
- [ ] Saya kuasa meracik sintaks pembangunan lemari tabel `CREATE TABLE`
- [ ] Saya sukses mengekstrak, memfilter `WHERE`, dan menyusun urutan data `ORDER BY` 
- [ ] Saya menuntaskan pembedahan kueri agen intel di Mini Lab SQLite
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/) — Kitab referensi andalan lintas masa untuk sandi kamus mantra *SQL*.

---

## ➡️ Besok

**Day 2: SQL Basics (Bagian 2)** — Esok harinya dirimu bakal memperdalam sisa mutasi data: *UPDATE* dan *DELETE*. Tak sekadar itu, kita bakal menyingkap rahasia mengapa *Database* ini dinobatkan kasta **"Relational"** dengan merantai koneksi bersilangan tabel memakai mantra mahaguru: `JOIN`!

---

*📅 TISS Null Teaming · Week 13 · Day 1 · FORGE Rank*
