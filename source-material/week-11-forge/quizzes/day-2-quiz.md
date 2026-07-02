---
type: quiz
week: 11
day: 2
title: "Quiz: Functions, Scope & Closures"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa urgensi teknis bagi pengembang perangkat lunak dalam membudayakan arsitektur penulisan blok kode berselimut fungsi (*Function*), ketimbang mencetaknya berjejeran berulang kali secara panjang dari atas skrip lurus-lurus?
- [x] A. Agar baris eksekusi tersebut patuh pada prosedur kerapian koding *DRY (Don't Repeat Yourself)*; sehingga blok kode tersebut bisa bebas diakses, dipanggil berkali-kali tanpa *copy-paste*, sekaligus mempermudah pelacakan perbaikan fitur jika kelak timbul *bug* (sentralisasi pengelolaan kode).
- [ ] B. Demi menyembunyikan arsip kodingan ke repositori awan *GitHub* milik sistem publik.
- [ ] C. Komponen fungsi diciptakan hanya demi memperkecil dimensi kapasitas penggunaan memori atom pada layar monitor pengguna.
- [ ] D. Skrip yang tidak menggunakan struktur *function* niscaya memantik respons penolakan keras oleh sistem perangkat keras server.

### Q2
**Type:** True/False
**Question:** Jika sebaris penetapan penampung variabel (contohnya `const token = "XYZ"`) sengaja ditulis dan dibiarkan bertengger bebas pada rute atas skrip di luar penguncian kerangka apa pun, maka klasifikasi variabel tersebut lazim dijuluki sebagai penganut *Local Scope*.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Pada era JavaScript sintaksis ringkas gaya ES6, apa sebutan populer bagi implementasi deklarasi fungsi peretas modern yang mengutamakan simbol tanda panah (`=>`) sehingga tidak lagi mewajibkan cantuman teks *function* secara eksplisit?
**Answer:** Arrow Function.

### Q4
**Type:** Short Answer
**Question:** Di ranah penetapan batas privasi (pembatasan *Scope*), julukan terklasifikasi apakah yang secara sakral disematkan untuk mengatur data variabel yang diam-diam hanya diisolasi tertutup eksklusif bagi perut fungsi pelingkupnya sehingga mustahil dicapai akses dari blok *script* eksternal lain?
**Answer:** Local Scope.

### Q5
**Type:** Short Answer
**Question:** Istilah baku peretas spesifik apa yang mempresentasikan muatan bahan baku (informasi eksternal murni) yang dititipkan atau dikirim menyelinap terintegrasi masuk pada celah kurungan tanda kurung saat sebuah *Function* coba dipanggil hidup?
**Answer:** Input (atau Parameter / Argumen).
