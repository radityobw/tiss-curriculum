# 🔨 Week 13 · Day 5: Lab & Weekly Mission Sistem Login/Register

> **Rank**: FORGE | **Minggu ke-13**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓░░] 80% — FORGE Rank (Minggu 4 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░] 54% — Hari 65 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → 🔄 FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu krusial telah tuntas. Kamu telah mempelajari cara kerja basis data permanen pada server beserta struktur perlindungan *API*:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | SQL Basics (Bagian 1) | Pijakan membangun (`CREATE`), menyuntik (`INSERT`), serta mengekstrak (`SELECT`) arsip Database relasional SQL. |
| Day 2 | SQL Basics (Bagian 2) | Modifikasi pembaruan dan penghapusan (`UPDATE/DELETE`) seraya menjahit relasi bersilangan (`JOIN`). |
| Day 3 | Database di Node.js | Pemasangan fungsi perantara operasional *Database Driver sqlite3*. |
| Day 4 | Auth & Password Security | Konsep arsitektur *Session* vs *JWT*, dilengkapi penerapan kriptografi pelindung kata sandi (*Bcrypt Hashing*). |

---

## 🧪 Hands-On Lab

### Prerequisites
- *Node.js* dan Editor kode (seperti VS Code) telah siap beroperasi.
- Modul pengujian API klien: **Postman / Thunder Client** terinstal.

### Misi Hari Ini: "Membangun API Sistem Otentikasi"

Secara teori kamu sudah siap. Hari ini, kamu akan membangun *Express Backend API* secara utuh, menghubungkannya dengan *SQLite*, dan melindunginya dengan kriptografi *Bcrypt*!

### Step 1: Inisiasi Direktori (Setup)

1. Deklarasikan ruang direktori `mkdir lab-auth-api`, kemudian akses navigasinya `cd lab-auth-api`.
2. Inisialisasi manifest proyek melalui: `npm init -y`.
3. Unduh dan instalasikan kompilasi pustaka andalan *Backend*:
```bash
npm install express sqlite3 bcrypt
```
4. Buat berkas peladen utama dengan nama `server.js`.

### Step 2: Arsitektur Persemayaman Server Komplit (The Masterpiece)

Salin struktur skrip peladen ini dan sisipkan ke perut `server.js`:

```javascript
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json()); // Penadah sandi payload bodi JSON

// ===============================================
// 1. PENYIAPAN DATABASE & TABEL (Auto-Create)
// ===============================================
const db = new sqlite3.Database('./brankas-agen.db');
db.serialize(() => {
  // Merakit kerangka tabel pengguna
  db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE,
    password_hash TEXT
  )`);
});

// ===============================================
// 2. RUTE REGISTRASI (CREATE USER)
// ===============================================
app.post('/api/register', async (req, res) => {
  const { username, password } = req.body; // Ekstraksi data sandi dari permintaan klien
  
  if(!username || !password) return res.status(400).json({pesan_status: "Error 400: Nama pengguna atau kata sandi tidak boleh kosong!"});

  try {
    // Fungsi Hashing Sandi (Tingkat salt: 10)
    const saltRounds = 10;
    const hashAbadi = await bcrypt.hash(password, saltRounds);

    // Sisipkan cincangan sandi (BUKAN teks aslinya!) ke Database
    const tembakanKueri = db.prepare("INSERT INTO users (username, password_hash) VALUES (?,?)");
    
    tembakanKueri.run([username, hashAbadi], function(err) {
      if (err) {
        return res.status(400).json({pesan_status: "Gagal, username tersebut sudah digunakan oleh pengguna lain!"});
      }
      res.status(201).json({pesan_status: "Registrasi Sukses! Akun Anda terdaftar dengan aman!"});
    });
    tembakanKueri.finalize();
  } catch (error) {
    res.status(500).json({pesan_status: "Kegagalan Peladen Internal (Internal Server Error)."});
  }
});

// ===============================================
// 3. RUTE LOGIN halaman (AUTENTIKASI)
// ===============================================
app.post('/api/login', (req, res) => {
  const { username, password } = req.body;

  // Lakukan pencarian awal di Database berdasarkan username
  db.get("SELECT * FROM users WHERE username = ?", [username], async (err, hasilData) => {
    
    // Validasi apakah pengguna tersebut eksis
    if (!hasilData) {
      return res.status(401).json({pesan_status: "Akses Ditolak! Akun pengguna belum terdaftar."});
    }

    // Apabila eksis, sinkronkan kecocokan fungsi 'password' masukan dengan 'hash' di peladen
    const tebakanCocok = await bcrypt.compare(password, hasilData.password_hash);
    
    if (tebakanCocok) {
      res.status(200).json({pesan_status: `Verifikasi Login Berhasil! Selamat datang, ${username}!`});
      // Di arsitektur produksi nyata, di titik inilah server menerbitkan token JWT untuk diserahkan ke klien.
    } else {
      res.status(401).json({pesan_status: "Akses Ditolak (401)! Kata sandi yang Anda masukkan tidak tepat."});
    }
  });
});

// Jalankan Server
app.listen(3000, () => console.log('Server API Otentikasi berjalan di Port 3000.'));
```

### Step 3: Pengecekan Daya Operasional Aplikasi Klien (Postman)

1. Jalankan server dengan perintah `node server.js`.
2. Buka *Postman* atau *Thunder Client*. Buat *request* POST ke rute API: `http://localhost:3000/api/register` (Kirimkan JSON *Body* yang berisi "username" dan "password").
3. Setelah registrasi berhasil, tes rute `/api/login` dengan memasukkan kata sandi yang salah secara sengaja (pastikan kamu mendapat respons `401 Unauthorized`).
4. Kemudian, coba lagi dengan kata sandi yang benar untuk memastikan kamu mendapatkan status `200 OK`!

---

## 🎯 Weekly Mission

### Misi: Mengevaluasi Keamanan Data Secara Visual
**Deskripsi:** Apabila kamu memperhatikan *folder* proyekmu, skrip server secara otomatis telah membuat sebuah file *Database SQLite* berformat `.db` (`brankas-agen.db`). 

**Tugas Mandiri:** Lakukanlah inspeksi manual ke dalam file *Database* tersebut secara visual menggunakan ekstensi VS Code *SQLite Viewer* atau aplikasi eksternal seperti *DB Browser for SQLite*. Buka dan lihatlah struktur tabel dari berkas `brankas-agen.db`!

**Deliverables:**
1. Tangkapan layar (*Screenshot*) tabel `users` di dalam database `brankas-agen.db`, yang menampilkan bahwa kolom `password_hash` telah tersimpan sebagai teks acak berkat perlindungan *bcrypt*.
2. Lampirkan gambar tangkapan layar tersebut di laporan misimu.

**Kriteria Sukses:**
- [ ] Mampu mengakses dan membaca *Database SQLite* secara visual menggunakan antarmuka eksternal (*GUI*).
- [ ] Memastikan bahwa data *password* tersimpan dalam bentuk algoritma *hash* acak yang aman, bukan teks murni (*plaintext*).

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Mengingat parameter pengiriman sandi otentikasi peladen API otentikasi pada gerbang *Register/Login* membungkus parameter paket *JSON* berisikan data sandi amat sensitif, rutinitas metode HTTP apa yang diwajibkan untuk mengalokasi pengiriman alurnya (dan mengapa tidak diperbolehkan menggunakan GET)?</summary>

**Jawaban:** Pengiriman kredensial wajib dikirim melalui *Body* pada metode HTTP *POST*. Metode *GET* sangat dilarang karena data yang dikirim via GET akan terekspos jelas secara transparan pada *URL Address Bar* (dan terekam di riwayat / histori browser).
</details>

<details>
<summary>❓ [MUDAH] Atribut batasan (*constraint*) tambahan apa yang wajib disematkan saat membuat kolom `username VARCHAR(50)...` agar pendaftar baru tidak bisa menggunakan *username* yang sama persis dengan yang sudah terdaftar?</summary>

**Jawaban:** Atribut pembatas `UNIQUE`.
</details>

<details>
<summary>❓ [SEDANG] Saat menjalankan API *Login*, apabila klien terbukti memasukkan tebakan kombinasi kata sandi atau *username* yang salah, kode status HTTP ras 4xx berapakah yang paling tepat dikirim oleh peladen sebagai respons penolakan?</summary>

**Jawaban:** Respons kode status HTTP 401 (*Unauthorized* / Akses Ditolak).
</details>

<details>
<summary>❓ [SEDANG] Pada fungsi hashing `bcrypt.hash(password, saltRounds)`, apa tujuan utama dan signifikansi parameter *saltRounds* (yang lazim disetel dengan nilai 10)?</summary>

**Jawaban:** *Salt rounds* menentukan tingkat kompleksitas komputasi (biaya waktu kalkulasi / *cost factor*) dari algoritma enkripsi. Semakin tinggi nilainya, semakin lambat server memprosesnya. Ini sangat krusial untuk menguras dan menyulitkan ketahanan mesin *hacker* jika mereka berniat meretas sandi secara masif dengan metode tebakan massal (*Brute-Force*).
</details>

<details>
<summary>❓ [SULIT] Saat mengeksekusi operasi API *Login*, coba jelaskan dua tahapan logis validasi backend sebelum server akhirnya secara sah merilis konfirmasi balasan *200 OK*!</summary>

**Jawaban:** Babak Pertama (Validasi Username): Server akan melakukan kueri ke database berdasar masukan nama akun (`username`). Jika datanya kosong, server merilis status penolakan 401. Babak Kedua (Pencocokan Sandi Hash): Jika *username* ditemukan, server mengambil data *password_hash* di database lalu mengadu kekuatannya dengan sandi teks inputan pengunjung yang sedang *login* (via metode *bcrypt.compare*). Hanya jika tahap pertama dan tahap kedua tuntas dengan valid, barulah server menerbitkan pengesahan logik akses berhasil *200 OK*.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya mampu merancang pembuatan tabel kueri SQL (`CREATE TABLE`) di ekosistem *SQLite*.
- [ ] Saya telah menuntaskan praktik penyatuan API server *Express Node.js* dengan sistem penyimpanan database permanen *SQL*.
- [ ] Saya memahami siklus perlindungan keamanan pencatatan sandi dengan memanfaatkan algoritma kriptografi *Bcrypt*.
- [ ] Saya berhasil mendirikan API yang solid, meliputi rute *Register* dan sistem otentikasi *Login*.
- [ ] Saya berhasil menyelesaikan Misi Mingguan dengan melakukan inspeksi database secara visual lewat antarmuka grafis *SQLite Viewer*.

---

## 💬 Diskusi Minggu Ini

1. Karena sandi *Bcrypt* mustahil diretas kembali ke bentuk aslinya (ireversibel), apakah menurutmu server masih perlu menerapkan batasan "Sandi wajib minimal 8 karakter dengan huruf dan angka"? Kenapa kita tidak membebaskan saja pengguna mendaftar dengan sandi konyol seperti "123"?
2. Evaluasi tingkat kesulitan perakitan *Backend API* minggu ini (Express + SQLite + Bcrypt Hashing) dibandingkan ketika merakit *Frontend* (CSS & Manipulasi DOM) minggu lalu. Manakah yang menurutmu terasa lebih mengasah nalar logikamu secara kritis? Mengapa?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│     🎖️ THE GATEKEEPER               │
│     Week 13 Complete                │
│     "You have built the vault       │
│      and forged the unbreakable key."│
│                                     │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 14: Secure Coding & OWASP Top 10**

Sekian pekan kamu terus belajar sebagai seorang perancang dan pembangun (*Software Developer/Blue Team*). Di minggu depan, paradigmamu akan diputar 180 derajat! Momen ini adalah masa transisi di mana kamu tidak lagi sekadar merancang sistem, namun dilatih berpikir ofensif selayaknya seorang **Penetration Tester** (Red Team). Kita akan menelaah kompilasi standardisasi celah keamanan dunia, yaitu **OWASP Top 10**, untuk membedah peringkat teknik-teknik peretasan paling masif dan mengerikan di kancah siber global!

> 🚀 *"To defend the fortress, one must learn how to burn it down."*

---

*📅 TISS Null Teaming · Week 13 · Day 5 · FORGE Rank*
