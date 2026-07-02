---
type: quiz
week: 13
day: 3
title: "Quiz: Database di Node.js"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Guna memfasilitasi integrasi kueri basis data agar perintah *SQL* sukses dieksekusi dari lingkungan peladen *Node.js* ke sistem Database sejati (seperti SQLite atau MySQL), implementasi pihak ketiga apakah yang mutlak dipasang dari repositori NPM?
- [x] A. Sebuah perangkat jembatan penghubung yang disebut *Database Driver* (misal paket `sqlite3` atau `mysql2`), yang bertugas mengonversi interaksi dari lingkungan *Node.js* menjadi instruksi spesifik yang dimengerti oleh peladen *SQL* yang dituju.
- [ ] B. Instalasi paket pengamanan *middleware* bawaan `express.json` untuk mencerna ekstrak kerangka pemodelan API.
- [ ] C. Sebuah fail ekstensi *frontend* HTML khusus peladen enkripsi bernama `database.html`.
- [ ] D. Paket eksekutor antarmuka pelacak IP *Router* (berkode `ip-sql-tracer-module`).

### Q2
**Type:** True/False
**Question:** Pasca instruksi pemanggilan `SELECT` dikerahkan oleh peladen *Node.js* untuk menyadap *SQL Database*, muatan balasan data dari peladen akan otomatis diterjemahkan menjadi format fail *Microsoft Excel (.xlsx)* siap cetak sebelum masuk ke variabel *JavaScript*.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Apa akronim populer (*Object-Relational Mapping*) dari arsitektur *Backend* yang fungsinya mengabstraksi penulisan sintaks kotor kueri *SQL* secara manual, guna dikonversi menjadi barisan pemanggilan *JavaScript Object Methods* yang ringkas dan mematuhi kaidah pemrograman orientasi objek?
**Answer:** ORM.

### Q4
**Type:** Short Answer
**Question:** Saat modul fungsi eksekutor *Driver Database* Node mengeksekusi sintaks perintah `.all("SELECT * FROM...", (err, data) => {...})` pada *SQLite3*, tipe struktur data JavaScript bawaan apakah (yang dilambangkan dengan pengapit kurung siku `[]`) yang didelegasikan untuk menampung seluruh himpunan parameter baris data balasan (`data`) tersebut?
**Answer:** Array (berwujud *Array of Objects*).

### Q5
**Type:** Short Answer
**Question:** Apa kepanjangan resmi dari singkatan 3 huruf *NPM*, yang merujuk pada manajemen distribusi sentral penyedia unduhan pustaka (termasuk *driver database*) bagi infrastruktur *Node.js* global?
**Answer:** Node Package Manager.
