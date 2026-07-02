---
type: quiz
week: 12
day: 3
title: "Quiz: Express.js, Routing & Middleware"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa *developer backend* secara luas lebih memilih menggunakan *framework Express.js* ketimbang mengandalkan modul HTTP bawaan asli (Native) *Node.js* dalam membangun sebuah arsitektur peladen (*web server*)?
- [x] A. Kodingan *Node.js Native* dalam mengatur perutean (*routing*) *HTTP* sangatlah kompleks dan mengharuskan *developer* merangkai alur percabangan (*boilerplate*) mentah yang panjang, sementara bingkai *Express.js* menyajikan abstraksi sehingga perumusan rute serta implementasi *Middleware* teringkas menjadi struktur logik deklaratif rapi yang elok secara sintaksis.
- [ ] B. Skrip kerangka kerja *Node.js Native* senantiasa rentan mengalami kemacetan *error* internal sistem apabila tidak dilindungi penyamaran *proxy HTTP* perantara yang cuma eksklusif diciptakan pada ekosistem *Express*.
- [ ] C. Arsitektur modul bawaan *Express* mendatangkan efek ganda dalam mereplikasi pengalokasian kapasitas memori RAM *server* fisik, membuat kinerja mesin server *HTTP* seratus kali lipat lebih melesat laju daripada keterbatasan kemampuan *hardware* aslinya.
- [ ] D. *Express* difungsikan sebab modul asli kodingan eksekutor fungsi Node tidak didesain mengenali format tulisan standar ekstensi *file HTML* untuk dikonversi menjadi barisan interaksi *database SQL*.

### Q2
**Type:** True/False
**Question:** Komando pamungkas fungsi turunan `next()` pada eksekusi rantai pos penjagaan *Middleware Express.js* dirancang spesifik dengan mandat mematikan lalu lintas sirkuit jembatan koneksi (*Request*) klien secara paksa (langsung dihentikan putus siklusnya) sehingga rute selanjutnya gagal memproses atau tidak merespons payload pemanggilan intervensinya.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Identitas konsep pengelompokan yang mengurus manajemen tata kelola arah pemetaan titik alamat parameter tautan *URL Request* pengguna untuk diselaraskan dan diarahkan menuju blok peranti pemrosesan kode respons spesifik pada *web server* disebut?
**Answer:** Routing (atau Rute / Rute URL).

### Q4
**Type:** Short Answer
**Question:** Entitas komponen kode pemrograman penengah (*interceptor*) yang ditancapkan melintang di dalam sirkulasi pemrosesan perutean, guna mencegat, membedah modifikasi lalu lintas payload *HTTP Request*, serta melaksanakan tugas validasi pemeriksaan keamanan tambahan sebelum paket diserahkan mendarat ke modul eksekusi spesifik *handler* disebut apa?
**Answer:** Middleware.

### Q5
**Type:** Short Answer
**Question:** Ketika perakit aplikasi menghidupkan eksekusi pantauan soket radar penyadap komunikasi *port server* di dalam konstruksi *Express.js*, fungsi inisialisasi apa yang dipanggil di ujung baris akhir pengerjaan aplikasinya untuk memicu operasional radar penyadap lalu lintas rute komunikasi (umumnya membutuhkan umpan pelimpahan nomor port)?
**Answer:** listen (atau app.listen).
