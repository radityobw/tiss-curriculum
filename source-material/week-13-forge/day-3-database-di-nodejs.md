# 🔨 Week 13 · Day 3: Database di Node.js

> **Rank**: FORGE | **Minggu ke-13**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 13 · Day 3/5 | FORGE Rank (Minggu 4 dari 5) | Overall: 63/120 hari (52%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengkoneksikan** aplikasi *Node.js/Express* milikmu secara langsung ke *Database*.
2. **Mengeksekusi** kueri SQL melalui kode *backend*.
3. **Mengenal** sekilas konsep *ORM (Object-Relational Mapping)*.

---

## 📖 Materi Inti

### Komunikasi Lintas Sistem: Driver Database

Node.js dan Database SQL (seperti MySQL, PostgreSQL, atau SQLite) adalah dua program yang beroperasi secara terpisah. Secara bawaan, Node.js tidak bisa langsung membaca atau mengeksekusi perintah *SQL*.

Agar server API berbasis *Node.js* bisa mengirimkan perintah SQL ke *Database*, kita membutuhkan sebuah modul penghubung perantara yang disebut **Database Driver** (atau *Database Client Library*).

Untuk menghubungkan Node.js dengan database *SQLite*, kita akan menggunakan pustaka *Driver* populer dari *NPM* yang bernama `sqlite3`.

Alur kerja mekanismenya adalah sebagai berikut:
1. Kode *Node.js* menggunakan *Driver* untuk membuka koneksi ke file database.
2. Kode merakit perintah SQL dalam format teks (contoh: `SELECT * FROM arsip_data`).
3. Teks kueri SQL tersebut dikirimkan ke database melalui *Driver*.
4. *Database Engine* memproses kueri tersebut, lalu mengirimkan hasilnya kembali. *Driver* akan otomatis menerjemahkan hasil ini menjadi format data JavaScript (*Array of Objects*), yang kemudian bisa dikirim oleh server Node sebagai respon JSON ke klien.

### Sintaks Eksekusi Kueri di Node.js

Berikut adalah cara menggunakan *Driver sqlite3* di *Node.js* untuk menginisialisasi database:

```javascript
// 1. Memanggil modul Driver dari NPM
const sqlite3 = require('sqlite3').verbose();

// 2. Membuat koneksi ke file database
const db = new sqlite3.Database('./fitur.db');

// 3. Mengeksekusi pencarian SQL menggunakan metode `.all`
db.all("SELECT * FROM arsip_data", [], (error, hasilTarikData) => {
  if (error) {
    throw error;
  }
  // Variabel 'hasilTarikData' (array) akan berisi sekumpulan objek JavaScript yang siap diolah!
  console.log(hasilTarikData); 
});
```

### Lapisan Abstraksi Database: Pengenalan ORM (Object-Relational Mapping)

Di industri pengembangan perangkat lunak sesungguhnya, menulis kueri SQL mentah berulang kali di dalam kode Node.js sangat rawan *typo* (salah ketik) dan sulit untuk di-maintain (dipelihara) pada aplikasi skala besar.

Untuk mengatasinya, para *developer* sering menggunakan lapisan abstraksi yang dikenal sebagai **ORM (Object-Relational Mapping)** (contoh *framework ORM* populer di NPM: *Prisma*, *Sequelize*, dan *TypeORM*).

Dibandingkan menulis fungsi pencarian SQL mentah secara manual:
`SELECT * FROM staf WHERE divisi_id > 20`

*ORM* memungkinkan pemrogram untuk mengambil data secara elegan melalui pemanggilan metode objek JavaScript, semisal:
`Staf.findMany({ where: { divisi_id: { gt: 20 } } })`

*ORM* akan bekerja di balik layar (*under the hood*) untuk secara otomatis menerjemahkan kode JavaScript yang elegan tersebut menjadi perintah SQL murni (*raw SQL queries*).

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari kita buat koneksi database lokal pertamamu di skrip *Node.js*!

1. Buka Terminal, buat folder baru `mkdir lab-node-sql`, lalu masuk ke folder tersebut `cd lab-node-sql`.
2. Inisialisasi proyek Node.js dengan perintah `npm init -y`.
3. Instal *Driver* database SQLite:
```bash
npm install sqlite3
```
4. Buat file `induk.js`, lalu masukkan kode berikut:

```javascript
const sqlite3 = require('sqlite3').verbose();

// Tahapan memanggil dan merancang database (Sistem akan membuat file 'rahasiatiss.db' jika belum ada)
const db = new sqlite3.Database('./rahasiatiss.db');

// Rangkaian perintah SQL yang dijalankan berurutan (serialize)
db.serialize(() => {
  // Bangun Tabel (jika belum ada)
  db.run("CREATE TABLE IF NOT EXISTS pasukan (info TEXT)");

  // Menyiapkan operasi INSERT menggunakan statement (Parameterized Query)
  const pelatukInsersi = db.prepare("INSERT INTO pasukan VALUES (?)");
  pelatukInsersi.run("Anggota Tim Validasi");
  pelatukInsersi.run("Anggota Tim Auditor Jaringan");
  pelatukInsersi.finalize(); // Mengakhiri statement

  // Mengeksekusi kueri SELECT dan menampilkan hasilnya ke konsol
  db.each("SELECT rowid AS id, info FROM pasukan", (err, hasilData) => {
    console.log(`[LAPORAN SQLITE] ID: ${hasilData.id} -> ${hasilData.info}`);
  });
});

// Menutup koneksi database agar efisiensi terjaga
db.close();
```
5. Jalankan skrip di terminal: `node induk.js`
6. Terminalmu akan menampilkan hasil ekstraksi data dari tabel di dalam database SQLite lokal (file `rahasiatiss.db` telah sukses diproduksi, diisi data, dan dikueri melalui Node)!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Modul perantara apa (yang biasanya diinstal dari NPM) yang berfungsi untuk menjembatani komunikasi antara kode Node.js dengan sistem Database SQL?</summary>

**Jawaban:** *Database Driver* (contoh: `sqlite3`, `pg` untuk PostgreSQL, atau `mysql2` untuk MySQL).
</details>

<details>
<summary>❓ Dalam bentuk format tipe data apakah struktur kembalian (hasil respons) dari database SQL akan diterjemahkan oleh *Driver* saat ditangkap oleh variabel di dalam JavaScript Node.js?</summary>

**Jawaban:** ***Array of Objects*** (Di mana setiap satu *object* merepresentasikan satu baris / *record* hasil dari tabel SQL).
</details>

<details>
<summary>❓ Apa kepanjangan dari akronim *ORM*, yaitu lapisan abstraksi yang memungkinkan pengembang menulis kueri SQL menggunakan kode JavaScript berorientasi objek yang lebih rapi?</summary>

**Jawaban:** **Object-Relational Mapping (ORM)**.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami peran dari *Database Driver* untuk menjembatani Node.js dan SQL. 
- [ ] Saya sukses menjalankan koneksi *sqlite3* melalui skrip Node.js di terminal.
- [ ] Saya memahami konsep lapisan abstraksi *ORM (Object-Relational Mapping)*.
- [ ] Saya telah menuntaskan praktik *Mini Lab Node-SQL*.
- [ ] Saya telah meninjau ulasan materi di *Quiz Kilat*.

---

## 🔗 Resources

- [NPM: sqlite3 Documentation](https://www.npmjs.com/package/sqlite3) — Dokumentasi resmi penggunaan *Driver* `sqlite3` untuk Node.js.
- [Prisma ORM Intro](https://www.prisma.io/) — (Opsional) Tinjauan dokumentasi *Prisma*, salah satu framework *ORM* modern yang sangat populer di industri saat ini.

---

## ➡️ Besok

**Day 4: Authentication & Password Security** — Kemampuan menghubungkan Node.js dengan database sudah kamu kuasai. Besok, kita akan menyelami sistem keamanan login. Kita akan membedah konsep *Session-based Authentication* versus *Stateless JWT (JSON Web Token)*, serta menerapkan teknik kriptografi *Hashing* menggunakan modul `bcrypt` agar kata sandi pengguna tidak disimpan secara telanjang (*plaintext*) di dalam database.

---

*📅 TISS Null Teaming · Week 13 · Day 3 · FORGE Rank*
