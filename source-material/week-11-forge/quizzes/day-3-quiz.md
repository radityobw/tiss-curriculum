---
type: quiz
week: 11
day: 3
title: "Quiz: DOM Manipulation"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Membedah serius celah resiko paparan serangan *Cross-Site Scripting (XSS)*, ancaman manipulasi tingkat fatal apa yang mendera apabila perancang aplikasi web mengeksekusi penulisan rentetan masukan formulir masukan kotor (*raw input*) langsung melalui pipa saluran modifikasi `innerHTML`?
- [x] A. Rentetan teks input dari pengguna yang dimasukkan melalui corong *innerHTML* dapat ditafsirkan mentah-mentah secara lugu oleh *browser* selayaknya skrip aktif; jika peretas menyisipkan kode berbahaya seperti `<script>malware();</script>`, maka skrip parasit tersebut bakal serta-merta tertanam merusak mesin peramban dan berpotensi mencuri token data penting tanpa sepengetahuan pengunjung halaman web.
- [ ] B. Sandi akan mengakibatkan atribut warna dan dimensi gambar pada layar laman tertutup penuh.
- [ ] C. Komando sisipan lewat saluran properti *innerHTML* akan seketika membongkar paksa penulisan skrip pemindahan protokol URL sehingga bermutasi memanggil transmisi rute *GET*.
- [ ] D. Skema tersebut akan langsung mencetus layar mengunci perambannya secara permanen dari jaringan luar web publik publik.

### Q2
**Type:** True/False
**Question:** Di kancah arena pembidikan struktur DOM, fungsi dan pemanggilan *querySelector* sanggup menangkap referensi elemen spesifik secara efektif dengan memakai sintaks yang sangat persis menduplikasi aturan bidikan properti pelengkap yang lumrah diaplikasikan di perancangan riasan wajah (*CSS*), misalnya penanda `#` untuk *id* maupun `.` untuk *class*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Objek absolut tunggal nan mutlak (*built-in*) apakah dari inti peladen JavaScript yang berperan selaku entri poin awal (titik gravitasi sentral/induk pohon hierarki referensi) yang ditujukan untuk menggapai struktur anatomi pilar pilar tag HTML situs ketika laman telah ditangkap rendernya oleh penelusur layar?
**Answer:** document.

### Q4
**Type:** Short Answer
**Question:** Bila dihadapkan dengan atribut eksekusi properti `innerHTML` nan rawan mengancam teras kerawanan penyusupan celah skrip (*XSS*), alternatif properti *DOM* sebaya manakah yang spesifik dikhususkan sekadar menyuntik cetakan rentetan untai data mati semata belaka dan akan sangat dijamin steril pantang meresapi tafsiran komando marka format apapun?
**Answer:** innerText (atau textContent).

### Q5
**Type:** Short Answer
**Question:** Apakah nama atribut perantara parameter sihir pemanis tata letak komponen (*properti* tambahan dengan simbol titik sesudah penargetan elemen DOM) yang sanggup merubah wujud struktur CSS (semisal pemicuan penyetelan elemen `.style.color`) melintasi intervensi bahasa perantara dinamika JavaScript?
**Answer:** style.
