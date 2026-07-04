# 🔨 Week 12 · Day 4: REST API Design

> **Rank**: FORGE | **Minggu ke-12**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 12 · Day 4/5 | FORGE Rank (Minggu 3 dari 5) | Overall: 59/120 hari (49%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** standar arsitektur **REST API** untuk komunikasi *web*.
2. **Menghubungkan** operasi basis data (*CRUD*) dengan metode HTTP (*HTTP Methods*) yang tepat.
3. **Menganalisis** kode status balasan (*HTTP Status Codes*) yang dikirim dari *server* ke *client*.

---

## 📖 Materi Inti

### Standardisasi Arsitektur: REST API

Jika setiap *Backend Developer* membuat aturan penamaan URL sendiri secara acak (misal: `/bikin-buku`, `/hapusBukuSekarang`, atau `/Lihat_Buku`), maka *Frontend Developer* akan sangat kesulitan untuk menggunakan *API* tersebut.

Untuk menyamakan standar penamaan, industri sepakat menggunakan arsitektur **REST (REpresentational State Transfer)**.

Dalam REST API, URL (atau *Endpoint*) harus merepresentasikan objek/entitas Kata Benda (*Noun*), BUKAN berisi Kata Kerja (*Verb*) seperti "buat/lihat/ubah/hapus". Penentuan aksi yang ingin dilakukan diserahkan sepenuhnya kepada jenis **HTTP Method** yang dipanggil (seperti `GET`, `POST`, `PUT`, `DELETE`).

### Mengkaji Siklus Operasi Pilar Basis Data (CRUD)

Hampir semua aplikasi di dunia pada dasarnya hanya melakukan 4 hal terhadap data (dikenal dengan singkatan **CRUD**): **Create** (Membuat data baru), **Read** (Membaca data), **Update** (Mengubah data), dan **Delete** (Menghapus data).

Dalam arsitektur *REST API*, kita memetakan 4 operasi CRUD tersebut secara rapi menggunakan metode *HTTP (HTTP Methods)*:

| Operasi *CRUD* | *HTTP Method* | Contoh Format Rute URL (Misal entitas `buku`) | Arti Eksekusinya |
|---|---|---|---|
| **C**reate | `POST` | `/api/buku` | **Tambahkan/Buat** satu data buku baru. |
| **R**ead | `GET` | `/api/buku` | **Ambil/Tampilkan** daftar semua buku. |
| **U**pdate | `PUT` atau `PATCH` | `/api/buku/:id` (Tanda `:id` berarti ID buku spesifik) | **Perbarui** data buku dengan ID tersebut. |
| **D**elete | `DELETE` | `/api/buku/:id` | **Hapus** buku dengan ID tersebut. |

Perhatikan bahwa Rute URL-nya selalu statis dan berupa kata benda (`/api/buku`), bukan kata kerja seperti `/api/tambah-buku-baru`. Keputusan mengenai aksi apa yang dilakukan ditentukan seutuhnya oleh **HTTP Method** (`GET`, `POST`, `PUT`, `DELETE`).

### Kode Status (HTTP Status Codes)

Setelah *server* selesai memproses sebuah *Request*, ia wajib mengirimkan respons balasan beserta "Stempel Angka" yang menunjukkan status dari proses tersebut. Sandi 3 angka ini dikenal sebagai **HTTP Status Codes**.

- **Keluarga `2xx` (Sukses)**
 - `200 OK`: Permintaan berhasil diproses (umumnya untuk metode `GET`, `PUT`, atau `DELETE`).
 - `201 Created`: Data baru berhasil ditambahkan/disisipkan ke dalam *database* (umumnya balasan untuk `POST`).
- **Keluarga `4xx` (Kesalahan Klien/Frontend)**
 - `400 Bad Request`: Format data yang dikirim klien salah atau tidak valid (misalnya format JSON yang dikirim berantakan).
 - `401 Unauthorized`: Klien belum *login* atau tidak menyertakan token otentikasi.
 - `403 Forbidden`: Klien sudah *login*, tetapi tidak memiliki hak akses (privilese/jabatan) untuk mengakses rute tersebut (misal: bukan Admin).
 - `404 Not Found`: *URL endpoint* atau data yang dicari tidak ditemukan di *server*.
- **Keluarga `5xx` (Kesalahan Internal Server)**
 - `500 Internal Server Error`: Ada *bug* atau *crash* logika fatal pada kode di dalam *server backend* yang membuatnya gagal beroperasi.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang desain rute *Express* sesuai kredo arsitektur REST API!

1. Buka kembali *file* `app.js` yang ada di dalam *folder* `lab-express` pada penugasan *Mini Lab* kemarin.
2. Tambahkan kode berikut ini untuk merancang desain rute *Express* sesuai kredo arsitektur REST API:

```javascript
// Middleware bawaan Express untuk membaca data JSON yang dikirim klien
app.use(express.json()); 

// C (CREATE) - Menambah pengguna baru
app.post('/api/pengguna', (req, res) => {
 // Di simulasi ini, kita anggap data berhasil disimpan ke database.
 // Kita membalas dengan status 201 (Created) dan pesan sukses.
 res.status(201).json({ pesan: "Pengguna baru berhasil ditambahkan!" });
});

// U (UPDATE) - Memperbarui data pengguna spesifik
// ":id" adalah parameter dinamis. Jika URL-nya /api/pengguna/88, maka req.params.id = 88
app.put('/api/pengguna/:id', (req, res) => {
 const userId = req.params.id; 
 
 // Kita anggap proses pembaruan selesai.
 // Membalas dengan status 200 (OK).
 res.status(200).json({ pesan: `Data pengguna dengan ID ${userId} berhasil diperbarui!` });
});
```
3. Jangan lupa simpan kode dan jalankan ulang *server* dengan perintah `node app.js`. (Saat ini rute `POST` dan `PUT` tidak dapat diuji langsung dari peramban biasa karena menuntut aplikasi khusus seperti *Postman*. Fokuslah pada penulisan struktur dan tata cara pengkodeannya).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Jika mengacu pada standar *REST API*, apa yang salah dari penulisan URL `/api/hapus-pengguna/10`?</summary>

**Jawaban:** Standar REST melarang penggunaan *kata kerja* di dalam URL. URL harus merujuk pada kata benda entitas (contoh: `/api/pengguna/10`). Sementara penentuan aksi "menghapusnya" diserahkan pada metode permintaan pengaksesan menggunakan transmisi HTTP (yaitu metode `DELETE`).
</details>

<details>
<summary>❓ Apa perbedaan mendasar antara *Status Code* `401 Unauthorized` dengan `403 Forbidden`?</summary>

**Jawaban:** 
- `401 Unauthorized`: Klien belum *login* / tidak punya otentikasi. (*Server* menganggap tamu tersebut anonim dan menolak memprosesnya sebelum ia melakukan *login*).
- `403 Forbidden`: Klien sudah *login* dan peladen mengenalinya, namun profil klien tersebut tidak punya hak akses / otorisasi untuk mengakses rute spesifik itu (misal, *user* biasa memaksa masuk ke rute khusus *Admin*).
</details>

<details>
<summary>❓ Dalam Express.js, objek apa yang digunakan untuk mengekstrak atau mengambil nilai variabel dinamis yang disematkan langsung di ujung struktur barisan URL (misal angka 88 dari URL `/api/pengguna/88`)?</summary>

**Jawaban:** Objek `req.params` (seperti pada sintaks `req.params.id`).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya bisa mengasosiasikan 4 operasi CRUD (*Create, Read, Update, Delete*) dengan padanan HTTP *Method*-nya masing-masing.
- [ ] Saya paham bahwa standar URL pada REST API hanya merujuk pada kata benda entitas, dan bukan perintah kata kerja.
- [ ] Saya mengerti perbedaan keluarga grup *HTTP Status Codes* (2xx, 4xx, 5xx).
- [ ] Saya telah mempraktikkan susunan kode REST API *Routing* sederhana untuk metode POST dan PUT dalam sesi *Mini Lab*.
- [ ] Saya telah menjawab seluruh pertanyaan pada *Quiz Kilat*.

---

## 🔗 Resources

- [REST API Tutorial](https://restfulapi.net/) — Referensi lengkap mengenai panduan penyusunan standar arsitektur pola perutean REST API.
- [HTTP Status Dogs](https://httpstatusdogs.com/) — Alternatif referensi ilustratif komedi memori (kumpulan foto status lucu anjing) untuk membantumu lekas menghafal deretan *HTTP Status Codes*.

---

## ➡️ Besok

**Day 5: Lab & Mission: CRUD REST API** — Esok hari adalah sesi *Final Lab*! Kamu akan menyatukan semua teori mengenai *Backend API*, *Express.js*, dan standar arsitektur REST, untuk membuat sebuah simulasi utuh arsitektur fungsionalitas aplikasi 'Sistem Catatan' (*To-Do List REST API*) secara mandiri dari awal!

---

*📅 TISS Null Teaming · Week 12 · Day 4 · FORGE Rank*
