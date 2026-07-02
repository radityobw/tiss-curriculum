# 🎯 Week 13 · Day 6 (Bonus): Hands-On Learning

> **Rank**: FORGE | **Minggu ke-13** | Bonus Day

---

## 🌐 Platform Hari Ini

**[SQLBolt — Interactive SQL Tutorial](https://sqlbolt.com/)**
Tutorial SQL interaktif berbasis browser yang mengajarkan query SQL dari dasar hingga lanjutan melalui latihan langsung. Tidak perlu instalasi database.

💰 **Biaya**: Gratis (tanpa akun, tanpa registrasi, tanpa batasan)
⏱️ **Estimasi Waktu**: ~60 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Memperkuat pemahaman SQL (SELECT, WHERE, JOIN) melalui latihan interaktif
2. Mengerjakan query SQL langsung di browser tanpa setup database
3. Memahami konsep lanjutan: aggregation, subqueries, dan manipulasi data

---

## 📋 Requirement

* Peramban web modern (Chrome/Firefox)
* Pemahaman dasar SQL dari Day 1-2 minggu ini

> ⚠️ **Tidak perlu instalasi database.** SQLBolt menyediakan environment SQL langsung di browser.

---

## 📝 Prosedur

### Langkah 1: Akses SQLBolt
1. Buka [sqlbolt.com](https://sqlbolt.com/)
2. Klik **Lesson 1: SELECT queries 101**
3. Baca penjelasan singkat di bagian atas halaman

### Langkah 2: Kerjakan Lesson 1–6 (SELECT Queries)
1. **Lesson 1**: SELECT dasar — ambil data dari tabel
2. **Lesson 2**: WHERE clause — filter data dengan kondisi
3. **Lesson 3**: WHERE lanjutan — operator LIKE, BETWEEN, IN
4. **Lesson 4**: Sorting — ORDER BY, LIMIT, OFFSET
5. **Lesson 5**: Review dengan latihan
6. **Lesson 6**: Multi-table queries — JOIN

Untuk setiap lesson:
- Baca penjelasan konsep
- Kerjakan **semua latihan** di bagian bawah
- Tulis query SQL langsung di editor yang disediakan
- Klik **Run SQL** untuk melihat hasilnya

> 💡 **Tips**: Jika query-mu gagal, baca pesan error dengan teliti. Error SQL biasanya menunjukkan persis baris dan kolom yang bermasalah.

### Langkah 3: Kerjakan Lesson 7–12 (Data Manipulation)
1. **Lesson 7-9**: Aggregation — COUNT, SUM, AVG, GROUP BY
2. **Lesson 10-12**: ORDER OF EXECUTION dan subqueries
3. Selesaikan semua latihan

### Langkah 4: Kerjakan Lesson 13–18 (INSERT, UPDATE, DELETE)
1. **Lesson 13**: INSERT — menambahkan data baru
2. **Lesson 14**: UPDATE — memperbarui data
3. **Lesson 15**: DELETE — menghapus data
4. **Lesson 16-18**: CREATE TABLE, ALTER TABLE, DROP TABLE

> 💡 **Hubungkan dengan materi minggu ini**: Lesson 13-15 (INSERT/UPDATE/DELETE) berkorelasi langsung dengan operasi CRUD yang kamu pelajari di Day 3-4 saat membangun API dengan database.

---

## 🏁 Target Output

* ✅ Minimal **Lesson 1–6** selesai (SELECT + JOIN)
* ✅ Idealnya **Lesson 1–18** selesai (semua materi)
* 📸 Tangkapan layar SQLBolt yang menunjukkan lesson terakhir yang berhasil diselesaikan
* 📝 Catatan: 5 query SQL yang paling berguna/menarik dari latihan hari ini

---

## 🔄 Fallback

Jika SQLBolt tidak bisa diakses:
1. Buka [W3Schools SQL Tryit Editor](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) (gratis)
2. Gunakan editor SQL interaktif untuk mempraktikkan query:
 ```sql
 SELECT * FROM Customers WHERE Country = 'Germany';
 SELECT COUNT(*) FROM Products WHERE Price > 20;
 SELECT Customers.CustomerName, Orders.OrderID
 FROM Customers
 INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
 ```
3. Kerjakan minimal 10 query berbeda yang mencakup SELECT, WHERE, JOIN, dan aggregation
