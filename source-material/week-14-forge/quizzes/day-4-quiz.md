---
type: quiz
week: 14
day: 4
title: "Quiz: Security Misconfig & Data Exposure"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa *developer* sangat dilarang menuliskan data sensitif (seperti *API Key* atau *Password Database*) secara langsung (*hardcode*) di dalam *source code* (misalnya di `server.js`) dan diwajibkan menyimpannya di file `.env`?
- [x] A. Agar kredensial rahasia tersebut tidak ikut ter-upload ke repositori publik (seperti GitHub) ketika menggunakan sistem *version control*, karena file `.env` dapat diabaikan menggunakan file `.gitignore`. Hal ini mencegah *bot* peretas menemukan dan mencuri kredensial tersebut secara otomatis.
- [ ] B. Karena variabel *string* di JavaScript memiliki batasan maksimal 10 karakter sehingga tidak cukup untuk menyimpan *password* panjang.
- [ ] C. Menyimpan *password database* di dalam `server.js` akan secara otomatis memicu *error* pada *harddisk* server Node.js.
- [ ] D. Agar warna tampilan antarmuka *frontend* tidak terpengaruh oleh *API Key*.

### Q2
**Type:** True/False
**Question:** Membiarkan mode *debug* tetap aktif di tahap *production* dan menampilkan *Stack Trace* (rincian log *error* sistem, letak folder, dan versi modul) secara langsung ke layar pengguna ketika terjadi *Internal Server Error (500)* adalah praktik yang aman dan sangat direkomendasikan agar pengguna tahu apa yang salah.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Modul *middleware* Node.js apa yang digunakan untuk melindungi aplikasi Express.js dengan cara mengatur *HTTP Headers* secara otomatis (misalnya menyembunyikan header `X-Powered-By`)?
**Answer:** Helmet (Helmet.js)

### Q4
**Type:** Short Answer
**Question:** Untuk mencegah serangan *Brute-Force* atau DDoS (seperti penyerang mencoba *login* ribuan kali per detik), *middleware* apa yang sebaiknya diinstal untuk membatasi jumlah maksimal *request* dari satu IP dalam rentang waktu tertentu?
**Answer:** Rate Limiting (express-rate-limit)

### Q5
**Type:** Short Answer
**Question:** File konfigurasi khusus apa yang harus dibuat di *root* proyek agar sistem Git mengabaikan file tertentu (seperti `.env`) sehingga tidak ikut ter-*commit* dan ter-*push* ke repositori publik?
**Answer:** .gitignore
