# 🔨 Week 12 · Day 5: Lab & Weekly Mission CRUD API

> **Rank**: FORGE | **Minggu ke-12**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓░░░░] 60% — FORGE Rank (Minggu 3 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░] 50% — Hari 60 dari 120 (Mencapai Titik Separuh Perjalanan 6 Bulan!)

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → 🔄 FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini kamu telah melangkah keluar dari dunia *Frontend* dan mulai mempelajari dasar-dasar *Backend*:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Konsep Backend & API | Memahami perbedaan *Frontend* dan *Backend*, serta format data JSON. |
| Day 2 | Node.js Fundamentals | Mengenal *Node.js* untuk menjalankan JavaScript di *server*, serta penggunaan *NPM* dan `package.json`. |
| Day 3 | Express.js & Routing | Membangun *server* menggunakan *Express.js*, membuat *Routing* dasar, dan memahami *Middleware*. |
| Day 4 | REST API & Status Codes | Mengenal arsitektur REST API untuk operasi *CRUD* dan arti dari berbagai *HTTP Status Codes*. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Node.js sudah terinstal di komputermu.
- VS Code dan Terminal.
- Aplikasi penguji API seperti **Postman**, **Thunder Client** (ekstensi VS Code), atau **REST Client** untuk mengetes rute `POST`, `PUT`, dan `DELETE`.

### Misi Hari Ini: Membangun Simulasi API Backend (In-Memory CRUD)

Kita belum akan menggunakan *database* asli seperti SQL (kita akan mempelajarinya minggu depan). Sebagai gantinya, hari ini kita akan menyimulasikan *database* menggunakan variabel *Array* di dalam *file* JavaScript (*In-Memory Database*). Ingat bahwa karena hanya berupa variabel, semua data akan hilang/ter-reset setiap kali kamu me-*restart* *server* Node.js.

### Step 1: Persiapan Proyek

1. Buka Terminal, buat *folder* baru (misal: `mkdir lab-crud-api`), lalu masuk ke dalamnya (`cd lab-crud-api`).
2. Inisialisasi proyek NPM: `npm init -y`
3. *Install* Express: `npm install express`
4. Buat *file* bernama `server.js`.

### Step 2: Menulis Kode API CRUD

Salin kode di bawah ini ke dalam `server.js`. Baca dan pahami alurnya lewat komentar yang tersedia di dalam kode!

```javascript
const express = require('express');
const app = express();

// Middleware agar Express bisa membaca Request Body berformat JSON
app.use(express.json());

// In-Memory Database (Simulasi menggunakan Array)
let arsipData = [
 { id: 1, target: "Optimasi Jaringan", level: "High" },
 { id: 2, target: "Audit Database", level: "Medium" }
];
let generatorID = 3; // Variabel untuk membuat ID baru secara otomatis

// =====================================
// [R] READ ALL - Mengambil semua data (GET)
// =====================================
app.get('/api/arsip', (req, res) => {
 // Mengirimkan seluruh isi array 'arsipData'
 res.status(200).json({ data: arsipData });
});

// =====================================
// [C] CREATE - Menambah data baru (POST)
// =====================================
app.post('/api/arsip', (req, res) => {
 const body = req.body; 
 
 // Validasi: Pastikan 'target' dan 'level' tidak kosong
 if (!body.target || !body.level) {
  return res.status(400).json({ pesan: "Data target dan level tidak boleh kosong!" });
 }

 // Membuat objek data baru
 const objekBaru = {
  id: generatorID++,
  target: body.target,
  level: body.level
 };

 // Memasukkan data baru ke dalam array
 arsipData.push(objekBaru);
 res.status(201).json({ pesan: "Data baru berhasil ditambahkan!", data: objekBaru });
});

// =====================================
// [D] DELETE - Menghapus data spesifik (DELETE)
// =====================================
app.delete('/api/arsip/:id', (req, res) => {
 const idHapus = parseInt(req.params.id); 
 
 // Mencari index posisi data di dalam array
 const indeks = arsipData.findIndex(item => item.id === idHapus);

 // Jika data tidak ditemukan (index bernilai -1)
 if (indeks === -1) {
  return res.status(404).json({ pesan: `Data dengan ID ${idHapus} tidak ditemukan.` });
 }

 // Menghapus 1 elemen dari array pada posisi index tersebut
 arsipData.splice(indeks, 1);
 res.status(200).json({ pesan: `Data dengan ID ${idHapus} berhasil dihapus.` });
});

// Menjalankan server di port 8080
app.listen(8080, () => console.log('Server berjalan di port 8080'));
```

### Step 3: Pengujian API (*Testing Endpoints*)

1. Jalankan *server* di Terminal: `node server.js`
2. Buka Postman atau Thunder Client.
3. Lakukan *Request* **GET** ke URL `http://localhost:8080/api/arsip`. Kamu akan melihat daftar arsip dalam format JSON.
4. Sekarang, ubah metode *Request* menjadi **POST**. Pada bagian **Body**, pilih **Raw** dan **JSON**, lalu masukkan data berikut:
 ```json
 {
  "target": "Pemeliharaan Database",
  "level": "Super High"
 }
 ```
 Klik **Send**. Kamu akan melihat balasan berstatus `201 Created` beserta pesan konfirmasi bahwa data baru telah berhasil ditambahkan!

---

## 🎯 Weekly Mission

### Misi: Menyelesaikan CRUD & Membuat Dokumentasi API (*API Documentation*)

**Deskripsi:** Sebagus apapun *API* yang kamu buat, jika tidak memiliki dokumentasi (*buku panduan*), maka tim *Frontend Developer* tidak akan tahu cara menggunakan *API* tersebut. Selain itu, *API* kita saat ini baru memiliki fitur C (Create), R (Read), dan D (Delete). Fitur U (Update) masih belum ada!

**Tugas Mandiri:**
1. Kerjakan fitur **Update (U)** dengan menambahkan *routing* untuk `app.put('/api/arsip/:id')` di dalam `server.js`.
2. Buatlah *file* `README.md` yang mendokumentasikan keseluruhan *API* yang telah kamu buat (rute URL apa saja yang tersedia, metode HTTP yang digunakan, dan contoh balasan JSON-nya).

**Kriteria Sukses:**
- [ ] Rute `app.put(...)` untuk memperbarui data berhasil ditambahkan.
- [ ] *File* `README.md` berhasil dibuat dan berisi dokumentasi rute *API* yang jelas.
- [ ] *Push* kode proyek ke *repository* GitHub.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Saat melakukan pengujian aplikasi menggunakan *browser* ke alamat `http://localhost:8080/`, mengapa sering kali kita mendapatkan peringatan `Cannot GET /`?</summary>

**Jawaban:** Hal ini terjadi jika *developer backend* belum membuat *Routing* khusus untuk *root URL* atau direktori halaman utama (yaitu `app.get('/', ...)`). Pada *Mini Lab* tadi, kita hanya mendefinisikan rute untuk `/api/arsip`.
</details>

<details>
<summary>❓ [MUDAH] *Browser* biasa hanya bisa melakukan metode *Request GET*. Aplikasi apa yang biasa digunakan *developer backend* untuk menguji metode *POST*, *PUT*, dan *DELETE*?</summary>

**Jawaban:** **Postman**, atau alternatif lain seperti **Thunder Client** dan **Insomnia**.
</details>

<details>
<summary>❓ [SEDANG] Middleware apa yang wajib ditambahkan di awal skrip Express agar *server* bisa membaca dan mengekstrak data dari *Request Body* berformat JSON?</summary>

**Jawaban:** Middleware `express.json()`. Sintaksnya ditulis sebagai `app.use(express.json());`.
</details>

<details>
<summary>❓ [SEDANG] Saat klien mengirimkan data menggunakan metode `POST`, objek Express apa yang digunakan untuk menangkap data formulir tersebut di bagian *backend*?</summary>

**Jawaban:** Properti `req.body`.
</details>

<details>
<summary>❓ [SULIT] Apa perbedaan mendasar antara `req.params` dan `req.body`?</summary>

**Jawaban:** 
- `req.params` digunakan untuk menangkap nilai dari parameter *URL* yang dinamis (misal: ID `10` dari URL `/api/user/10`).
- `req.body` digunakan untuk menangkap bongkahan data/muatan (*payload*) yang dikirim secara tersembunyi di dalam *Body Request* saat klien menggunakan metode *POST* atau *PUT* (misal mengirimkan input profil nama, umur, alamat dalam bentuk JSON).
</details>

---

## 📋 Weekly Checklist

- [ ] Saya bisa membedakan peran aplikasi *Frontend* dan peran aplikasi *Backend Server*.
- [ ] Saya memahami cara menggunakan `npm init -y` untuk menginisialisasi manajer modul proyek *Node.js*.
- [ ] Saya mampu membuat rute server HTTP menggunakan *Express.js*.
- [ ] Saya sanggup merancang operasi arsitektur *CRUD* berdasarkan standar antarmuka *REST API*.
- [ ] Saya sukses menjalankan sesi *Hands-On Lab* merancang *In-Memory CRUD API Server*.

---

## 💬 Diskusi Minggu Ini

1. Dibandingkan dengan pengembangan *Frontend* (UI/UX) yang sarat visual, pengembangan *Backend* sangat fokus pada logika, keamanan, dan pengaturan data abstrak (JSON). Dari pengalaman minggu ini, manakah area yang menurutmu lebih memancing ketertarikanmu secara karier profesional?
2. Andaikan saja kode perlindungan atau verifikasi (seperti blok `if(!req.body.target)`) pada operasi penambahan (*Create/POST*) tidak pernah kamu buat, apa dampaknya apabila pengguna iseng terus-terusan mengirim data ke *server* tanpa mengisi nama target dan level sama sekali? Bagaimana hal ini akan mengotori basis data *server*-mu di kemudian hari?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ THE SERVER ARCHITECT │
│ Week 12 Complete │
│ "You have seized control of │
│ the unseen machinery." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 13: Database & Authentication**

Di sesi *Mini Lab* hari ini, *server* kita masih menggunakan *Array In-Memory* sebagai basis data. Artinya, begitu *server* dimatikan, semua data yang kita masukkan akan lenyap tak berbekas! Ini tentu bukan cara kerja aplikasi profesional.

Oleh karena itu, minggu depan kita akan mempelajari teknologi **Database SQL** sebagai sistem penyimpanan yang statis, persisten, dan abadi. Selain itu, kamu juga akan belajar cara merancang arsitektur keamanan otentikasi (*Login Authentication & Password Hashing*) untuk melindungi data sensitif pengguna dari akses pihak yang tidak bertanggung jawab!

> 🚀 *"Data is eternal when etched in SQL."*

---

*📅 TISS Null Teaming · Week 12 · Day 5 · FORGE Rank*
