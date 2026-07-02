---
type: quiz
week: 13
day: 4
title: "Quiz: Authentication & Password Security"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Menilik arsitektur teknikal pengelolaan sesi otentikasi menggunakan *JSON Web Token (JWT)*, pendekatan logis revolusioner apakah yang mampu membebaskan peladen *Server* dari beban krusial mencatat rekam riwayat login seluruh penggunanya secara *stateful* di *database*?
- [x] A. Arsitektur komunikasi *JWT* menganut prinsip desain nir-status (*Stateless*). Token JWT yang berisi stempel digital dititipkan sepenuhnya di sisi klien. Ketika disertakan pada permintaan, *Server* hanya perlu memvalidasi tanda tangan kriptografis dari token tersebut untuk membuktikan keabsahan klaim identitas, sehingga *Server* terbebas dari kebutuhan merawat log penyimpanan sesi secara memori.
- [ ] B. Karena eksekusi logik *Server* JWT senantiasa mewajibkan pemasangan modul duplikat database mini secara otomatis yang diselipkan membaur pada *hard disk peramban lokal* milik pihak klien penjelajah.
- [ ] C. *JWT* mentransmisikan parameter pelacakan spesifik via verifikasi retina peladen fisik jaringan.
- [ ] D. *JWT* diam-diam menduplikasi rutinitas rekam jejak pengguna melalui injeksi catatan *Log OS Linux* yang berjalan di belakang layar perangkat peladen.

### Q2
**Type:** True/False
**Question:** Pembeda esensial perlindungan sandi melalui teknik pembalutan *Enkripsi* (*Encryption*) dibandingkan pemrosesan *Hashing* terletak pada fungsi kalkulasinya; di mana sandi hasil *Enkripsi* dirancang agar bisa didekripsi (diubah kembali ke wujud aslinya/dua arah), sedangkan kalkulasi *Hashing* diformulasikan murni memproses mutasi teks secara matematis *satu arah* (sehingga nilai hasilnya mustahil dapat direkayasa balik (di-*reverse*) menjadi teks kata sandi murni orisinal asalnya).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Parameter suci berupa serpihan teks acak pengaman tambahan apakah (yang pada algoritma kriptografi modern semacam *Bcrypt* secara otomatis diracik membaur bersama kata sandi pendaftar) yang ditugaskan khusus menjamin bahwa pengacakan sandi akan tetap membuahkan dua deretan struktur nilai *hash* yang sangat berbeda kendatipun ada dua pendaftar pengguna menyetel inputan teks sandi murni ("12345") yang persis sama persis?
**Answer:** Salt (atau Kadar Garam / Salt Rounds).

### Q4
**Type:** Short Answer
**Question:** Apa wujud nama modul dependensi pustaka pelengkap spesialis arsitektur penyandian kriptografi satu arah yang masyhur dan direkomendasikan penggunaannya secara absolut oleh *developer Backend JavaScript* untuk melindungi data teks kata sandi (*hashing algorithm*)?
**Answer:** bcrypt (atau bcryptjs).

### Q5
**Type:** Short Answer
**Question:** Ketika entitas peretas meluncurkan eksekusi simulasi pelacakan algoritma tebakan perombakan kata sandi memborbardir gerbang peladen tanpa henti (rutin menyerang lewat kalkulasi metode pengujian permutasi kueri kata yang diekstraksi dari basis kamus probabilitas *wordlist*), apa identifikasi nama kategori nomenklatur log penyerbuan identifikasi sandi intensif semacam itu?
**Answer:** Brute-Force (atau Brute Force Attack / Serangan Brute-Force).
