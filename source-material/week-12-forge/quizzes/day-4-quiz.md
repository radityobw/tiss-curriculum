---
type: quiz
week: 12
day: 4
title: "Quiz: REST API Design"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Bila seorang *client* melontarkan pengiriman *request* menggunakan perbekalan metode operasi HTTP `POST` guna mencetuskan penciptaan (*create*) rekaman (*record*) data profil entitas pengguna baru di lambung *database server*, kode standar persandian sinyal status *HTTP* bernomor keberhasilan berapakah (yang spesifik sesuai desain *REST*) yang idealnya dikembalikan oleh peladen?
- [x] A. Sinyal nomor kode *201 Created*.
- [ ] B. Sandi balasan status *200 OK* umum biasa.
- [ ] C. Sandi pelaporan balasan status error *500 Internal Server Error*.
- [ ] D. Sandi pelaporan gagal pencarian lokasi galat status *404 Not Found*.

### Q2
**Type:** True/False
**Question:** Mengikuti kaidah ketat arsitektur standar pilar fundamental *REST API*, kita diwajibkan memberikan pelabelan (*naming*) instruksional aksi fungsi pada desain *URL* rute serangan *endpoint*-nya secara agresif dengan eksplisit menyertakan sisipan kata-kata kerja (berwujud aksi penugasan layaknya *`/api/hapus-entitas-ini`* atau *`/api/ubah-data-buku`*) guna menggantikan kedudukan perantara tugas penugasan Metode HTTP.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Pada kredo rancang *REST API* modifikasi pengelola manipulasi rekaman data basis pengingat peladen, 4 (empat) tipe pengelompokan eksekusi aksi standar modifikasi operasi database (Penciptaan, Pembacaan, Pemutakhiran/Penggantian, Penyingkiran) disatukan populer di bawah bayang identitas penyebutan akronim singkatan 4 abjad apakah?
**Answer:** CRUD (Create, Read, Update, Delete).

### Q4
**Type:** Short Answer
**Question:** Jika dibandingkan komparasinya dengan balasan galat kegagalan parameter respons berlabel *400 Bad Request*, informasi krusial apakah (pesan indikator kendala penolakan spesifik) yang sejatinya dikomunikasikan secara lugas oleh kode galat absolut pengiriman respons server bersandi *HTTP 404 Not Found*?
**Answer:** Target rute *URL endpoint* entitas objek data (*resource*) yang dimaksud atau dicarinya tidak tersedia di sistem peladen atau tidak terpetakan keberadaannya.

### Q5
**Type:** Short Answer
**Question:** Bila dicermati dari spektrum kategori variasi metode aksi rute eksekusi fungsionalitas HTTP kembara komunikasi, rincikan sepasang komando pemanggilan standar (keduanya bertulis awalan abjad huruf `P`) yang berstatus dipadankan mewakili tugas mutasi parameter rombakan penyuntingan (*Update*/merubah atribut utuh sebagian data) *resource*!
**Answer:** PUT dan PATCH.
