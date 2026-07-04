---
type: quiz
week: 18
day: 2
title: "Quiz: Burp Suite Repeater & Intruder"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan fungsionalitas utama antara fitur *Repeater* dan *Intruder* pada Burp Suite?
- [x] A. *Repeater* adalah fitur untuk menguji celah secara manual dengan memodifikasi dan mengirimkan satu *Request* berulang-ulang dengan teliti. Sebaliknya, *Intruder* adalah alat otomatisasi (*Brute Force*) yang digunakan untuk mengirimkan ratusan hingga ribuan *Payload* secara beruntun ke titik sasaran tertentu.
- [ ] B. *Repeater* hanya bisa mengeksploitasi *XSS*, sementara *Intruder* digunakan khusus untuk kerentanan *CSRF*.
- [ ] C. *Repeater* memodifikasi dokumen HTML, sedangkan *Intruder* memodifikasi file CSS.
- [ ] D. Tidak ada perbedaan, keduanya mengharuskan pentester membeli lisensi *Professional*.

### Q2
**Type:** True/False
**Question:** Saat menggunakan *Burp Intruder*, pentester menggunakan simbol *Section Sign* (`§...§`) pada tab *Positions* untuk menandai koordinat titik sasaran (*Payload Position*) yang akan diinjeksi dengan kata dari *Wordlist*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Jika seorang pentester ingin menguji celah *SQLi* dengan mencoba berbagai modifikasi *payload* secara bertahap tanpa harus membuka *Browser* kembali, tab *Burp Suite* apa yang paling tepat digunakan?
**Answer:** Repeater.

### Q4
**Type:** Short Answer
**Question:** Setelah menembakkan ratusan *payload* di *Burp Intruder*, kolom metrik apakah (selain kolom kode *Status* HTTP) pada tabel hasil yang paling sering digunakan untuk mengidentifikasi keberhasilan eksploitasi karena menunjukkan perbedaan ukuran respons *server*?
**Answer:** Length.

### Q5
**Type:** Short Answer
**Question:** Jalan pintas pada papan ketik (*Keyboard Shortcut*) apa yang digunakan untuk melempar langsung paket *Request* yang sedang ditahan (*Intercept*) ke tab *Repeater*?
**Answer:** Ctrl+R (atau Control+R).
