# 🔨 Week 13 · Day 2: SQL Basics (Bagian 2)

> **Rank**: FORGE | **Minggu ke-13**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 13 · Day 2/5 | FORGE Rank (Minggu 4 dari 5) | Overall: 62/120 hari (51%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memperbarui** dan memodifikasi data serta menghapus baris dari tabel (*UPDATE* & *DELETE*).
2. **Memahami** konsep normalisasi dan pembentukan hubungan (*Relationships*) antar-tabel.
3. **Menggabungkan** pengikatan data dari pecahan dua tabel referensi yang terpisah menggunakan klausa integrasi `JOIN`.

---

## 📖 Materi Inti

### Modifikasi Data Lanjutan: UPDATE & DELETE

Melengkapi rentetan siklus pengoperasian *CRUD* (sebagai kelanjutan babak inisialisasi basis data kemarin), kini saatnya mendalami fungsi rombakan basis data permanen.

**1. Mengganti atau Memperbarui Data (UPDATE)**
```sql
UPDATE pengguna 
SET umur = 26 
WHERE username = 'ZeroCool';
```
> ⚠️ **IMPORTANT:** Jika pengembang sistem urung atau lupa menyematkan filter kondisi klausa `WHERE`, instruksi sintaks modifikasi `UPDATE pengguna SET umur = 26;` akan dieksekusi secara global (tanpa batasan kondisional) sehingga berimbas **MENGUBAH UMUR SELURUH PENGGUNA** di tabel tersebut menjadi `26` secara seragam. Kejadian ini lazim diklasifikasikan sebagai kesalahan operasional modifikasi fatal (*tragedy of missing where clause*).

**2. Memusnahkan Rekaman Baris Arsip (DELETE)**
```sql
DELETE FROM pengguna 
WHERE username = 'CrashOverride';
```
*(Serupa dengan prosedur Update, andaikata argumen penjaring klausa `WHERE` dicabut dari ekor komando kueri di atas, maka isi tabelmu akan tersapu bersih total hingga sirna dari basis datanya!)*

### Konsep Relasional pada Basis Data (Normalisasi)

Mengapa basis data klasifikasi RDBMS (seperti *MySQL, PostgreSQL, atau SQLite*) dijuluki dengan istilah *"Relational"*?
Bayangkan arsitektur operasional pencatatan pada sebuah ekosistem log transaksi situs niaga. Alih-alih memampatkan fusi data secara merangkum serampangan (menjejal parameter identitas pengguna, profil alamat, rincian produk, hingga log transaksi tanggal *order* berhimpitan) ke dalam **Satu Tabel Penampung Skala Masif**, perancang sistem data memisahkan penyusunan alokasi arsitekturnya menyebar menjadi sejumlah tabel spesifik yang lebih kecil dan terstruktur (sebuah proses pengurutan yang dikenal sebagai **Normalisasi**).

Misal: Spesifikasi Tabel `users` (dikhususkan murni menyusun hierarki atribut referensial biodata pelanggan) dan Tabel `pesanan` (dikhususkan untuk merekam log transaksional urutan aktivitas order pelanggan).
Kedua tabel spesifik ini kelak ditautkan bersilangan untuk menjahit relasi menggunakan integrasi penanda identitas jangkar sandi relasional. Kolom parameter penaut koneksi antartabel inilah yang didefinisikan secara istilah teknis sebagai **Foreign Key** (Kunci Tamu).

### Menggabungkan Data Antar Tabel (JOIN)

Ketika sajian pelaporan ekstraksi rekaman akan didisplai melintasi aplikasi berbasis antarmuka ke layar pengguna (klien), pengguna tentu menginginkan struktur laporannya sudah diolah menjadi format pembacaan utuh, dan tidak sekadar menampilkan jejeran nomor indeks abstrak parameter ID. Peladen pelaksana operasi kueri harus merangkai ulang (menyatukan) potongan referensi tabel spesifikasi `users` dan log `pesanan` tadi secara terintegrasi via deklarasi operasi integrasi **JOIN**.

```sql
SELECT users.nama, pesanan.total_harga 
FROM users
JOIN pesanan ON users.id = pesanan.user_id;
```
*(Sintaks integrasi operasional `JOIN` ini menginstruksikan modul mesin pengeksekusi SQL untuk menyatukan dan menyandingkan baris payload referensial 'users' bersama tabel 'pesanan' asalkan penempatan kunci identitas primer parameter 'id' dari pelaporan tabel klien cocok secara relasional mengait presisi dengan spesifikasi parameter kuncian 'user_id' pada log tabel rincian pesanan).*

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari bangun rancangan arsitektur tabel berelasi dan jalankan instruksi `JOIN` perdanamu!

1. Kunjungi kembali portal platform pengerjaan basis data kompilator portabel [DB Fiddle (SQLite)](https://www.db-fiddle.com/).
2. Arahkan kursor ke panel deklarasi ruang penyusunan tabel sisi **Schema (kiri)**, lantas konstruksikan spesifikasi susunan dwi tabel operasional terpisah:
```sql
CREATE TABLE divisi (
 id INTEGER PRIMARY KEY,
 nama_divisi VARCHAR(50)
);
CREATE TABLE anggota (
 id INTEGER PRIMARY KEY,
 nama VARCHAR(50),
 divisi_id INTEGER -- Penetapan Barisan Lajur Integrasi Kunci Tamu (Foreign Key)
);

INSERT INTO divisi (id, nama_divisi) VALUES (1, 'Tim Inti Backend');
INSERT INTO divisi (id, nama_divisi) VALUES (2, 'Tim Analis Data');

INSERT INTO anggota (nama, divisi_id) VALUES ('Administrator Utama', 1);
INSERT INTO anggota (nama, divisi_id) VALUES ('Teknisi Jaringan', 2);
```

3. Beralih pindah menginspeksi ruang panel operasi pengerahan **Query (kanan)**, aplikasikan komando ekstraksi kueri `JOIN` untuk menjahit pecahan pelaporan payload data tersebut:
```sql
-- Kita menyeleksi parameter payload nama staf berserta spesifikasi label organisasinya secara berpadu utuh
SELECT anggota.nama, divisi.nama_divisi
FROM anggota
JOIN divisi ON anggota.divisi_id = divisi.id;
```
4. Jalankan (tekan eksekusi tombol Run)! Periksa jendela penampang respons (*Results*) di bawah layar, penggabungan tersebut telah sukses mengaitkan referensi terpisah dan menerjemahkan pengikatan sandi angka ID `divisi_id` menjadi terjemahan format deskriptif teks utuh yang memuat laporan 'Tim Inti Backend' atau pun 'Tim Analis Data'.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Konsekuensi kerusakan fatalitas apakah yang niscaya membentur operasi struktur penahanan basis data bilamana arsitek pengelola basis data meluncurkan operasional eksekusi kueri instruksi modifikasi *SQL* penghapusan payload `DELETE FROM pengguna;` tanpa mengikutsertakan penyisipan klausa pembatas jaring saringan kondisi sintaksis `WHERE`?</summary>

**Jawaban:** Kelalaian spesifik akibat absennya pencantuman instruksi klausa kondisional pembatasan `WHERE` di buntut kueri tersebut niscaya menitahkan peladen SQL untuk membabat habis dan memusnahkan eksistensi SELURUH muatan rekam jejak barisan *record* dari rahim tabel operasional parameter `pengguna` sehingga lumbungnya kosong tak bersisa (terjadi musibah penghapusan data menyeluruh).
</details>

<details>
<summary>❓ Kenapa administrator pengembang rancangan struktur relasional arsitektur logika *Relational Database* mewajibkan praktik memecah, memisahkan, serta mengklasifikasi arsitektur data menjadi serpihan sebaran banyak fungsionalitas komponen penyusunan tabel spesifik ukuran kecil berlapis (prosedur **Normalisasi**) dibandingkan menyatukan fusi seluruh properti basis log-nya terpadu serampangan ke format struktur data tunggal (tabel makro tunggal raksasa)?</summary>

**Jawaban:** Untuk memberangus pemborosan alokasi dan anomali pengulangan perekaman parameter identitas operasional (atau istilahnya menekan repetisi duplikasi data ganda /*redundansi*). Andaikata seluruh fusi data diformulasikan bersatu berjejal dalam kerangka memori satu lapis spesifik tabel makro berhimpit saja, otomatis penamaan parameter detail pelapor *users* niscaya tercetak ganda terulang-ulang berulang ribuan kali saban entitas pelanggan yang persis sama iseng melaksanakan prosedur pembelanjaan rutin secara kontinu. Melewati proses isolasi fragmentasi pemecahan (normalisasi tabel spesifik), rekaman payload biodata profil *user* cuma butuh disimpan cukup 1 baris saja dengan format rapi dan stabil, sedangkan fungsi dokumentasi log rincian pesanan rutin bakal murni menautkan rujukannya sekadar meminjam pemanggilan integrasi sandi korelasi relasional nomor unik pengguna terkait (*ID Parameter Identifier Primary/Foreign Key*).
</details>

<details>
<summary>❓ Nama klausa operasional fungsi kueri jenis manakah pada bahasa relasional operasi SQL yang ditugaskan khusus menempelkan jalinan ikatan operasi penggabungan dua kolom antartabel terpisah (maupun lebih) untuk lantas menyajikannya beraliansi menyajikan format sintesis abstraksi penyulingan satu hasil keluaran parameter bersatu utuh yang bersesuaian dengan syarat patokan relasi silang konektor kuncian id *Foreign Key*?</summary>

**Jawaban:** Operasi pendelegasian pengikatan sintaks kueri spesifikasi `JOIN`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap betapa berbahayanya melupakan batasan penjaring klausa `WHERE` pada siklus pemanggilan fungsi operasi mutasi/pemusnahan payload `UPDATE` maupun instruksi log `DELETE`.
- [ ] Saya fasih menjabarkan fungsionalitas kegunaan logik penyematan atribut referensial pengikatan arsitektur basis data relasional *Foreign Key*.
- [ ] Saya mendemonstrasikan kelancaran merangkai pemanggilan sintaksis pengikatan ekstrak *JOIN* pada dua modul referensial penyusunan basis tabel.
- [ ] Saya sukses mengaplikasikan integrasi praktik pengerjaan *Mini Lab SQLite* secara koheren.
- [ ] Saya telah meninjau penyerapan pembelajaran harian materi evaluasi ringkas (*Quiz Kilat*).

---

## 🔗 Resources

- [SQL Joins Visualizer](https://sql-joins.leopard.in.ua/) — Referensi ilustrasi penguraian interaktif diagram logika relasional (*Venn Diagram Simulation Tool*) yang diakui secara luas selaku pedoman komprehensif nan logis untuk mengidentifikasi dan mencerna secara cepat serabut parameter kueri perbedaan klasifikasi implementasi *LEFT JOIN*, fungsi kueri *INNER JOIN*, *RIGHT JOIN* secara spesifik dan teknis.

---

## ➡️ Besok

**Day 3: Database di Node.js** — Saat ini ilmu perumusan logik *SQL*-mu secara operasional masih dikategorikan berstatus sebagai eksekusi skrip kueri komando mandiri yang dioperasikan manual semata-mata di terminal atau peladen pengujian pelabuhan uji coba tiruan (*sandbox*). Besok, perpaduan krusial integrasi operasional sejati arsitektur sistem pengolahan logik akan diformulasikan: Kita kelak mendemonstrasikan cangkok instalasi antarmuka program aplikasi arsitektur *Node.js Backend* lantas memberikan wewenang penuh agar aplikasi kerangka utusan *JavaScript API Framework Node* milikmu tersebut dilatih meluncurkan otomasi rentetan sintaks kueri modifikasi transmisi *SQL* demi berinteraksi menautkan peladen API *web* sejati jaringan dengan penyimpanan rak memori data *Database RDBMS SQL* permanen!

---

*📅 TISS Null Teaming · Week 13 · Day 2 · FORGE Rank*
