---
type: quiz
week: 13
day: 5
title: "Quiz: Lab Sistem Login/Register"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Menakar siklus kelemahan pada rutinitas transmisi *Otentikasi Kredensial Login* antara antarmuka *Frontend* dan *API Peladen*, alasan teknikal mutlak apakah yang melarang keras eksploitasi parameter rute peramban via metode `GET` (sehingga mewajibkannya dilewatkan ke bodi tersembunyi `POST`)?
- [x] A. Dilarang mendelegasikan pengiriman pengikatan formulir login via rute metode `GET` dikarenakan sandi sensitif dan parameter *username* pendaftar akan terekspos telanjang di lintasan terbuka parameter baris *Query String URL (Address Bar)* peramban web. Ini memicu risiko fatal kerentanan sadap, bahaya perekaman pengintip, atau pembajakan lewat *History log* peramban publik.
- [ ] B. Dilarang mendelegasikan siklus sandi mengandalkan pengiriman metode *JSON POST* lantaran merusak jaringan *API* basis relasi global .
- [ ] C. Sandi metode jaringan peramban *PUT* diharamkan karena akan memusnahkan eksistensi logik tabel basis data tamu tanpa sisa.
- [ ] D. Sandi tak boleh diinjeksi ke peramban *Node.js* melainkan mesti diarahkan ke skrip lokal Python OS peladen lokal klien jaringan.

### Q2
**Type:** True/False
**Question:** Ketika perancang sistem Basis Data (*Database*) membidani pendirian deklarasi kerangka cetakan parameter kolom otentikasi memuat aturan penegasan kondisi `username VARCHAR(50) UNIQUE`, maka konstrain atau tameng perisai batasan `UNIQUE` tersebut mendikte eksekutor *Database Engine* guna menjegal pencatatan/akun ganda ketika ada tamu baru yang bermaksud meniru/mengklaim *username* murni yang 100% sama dengan catatan profil entitas pengenal referensial payload pendaftar lama.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada tahapan verifikasi eksekusi otentikasi data login, ketika peramban API peladen mengidentifikasi kegagalan otentikasi dari tamu (misal ketika klien melampirkan tebakan varian parameter payload nilai sandi teks acak yang setelah dikomparasi ternyata tak cocok bersilangan dengan catatan sandi *hash* di Database), stempel kode penolakan akses jaringan (*HTTP Error Status Code seri 4xx*) manakah yang mesti dihantarkan guna merespons laporan galat identifikasi tak berizin (*unauthorized*) ke muka perambannya?
**Answer:** 401 (Unauthorized).

### Q4
**Type:** Short Answer
**Question:** Di bentangan rentetan fase pengerjaan arsitektur implementasi validasi pengikatan fungsi *Backend Login API*, bilamana peladen sukses memetakan validitas kecocokan *username* tamu di data SQL, metode instruksional pusaka apakah turunan modul kriptografi `bcrypt` (bukan fungsi metode `hash`) yang diletuskan spesifik untuk membandingkan kecocokan antara tebakan teks sandi murni tamu dengan hasil rekam rentetan cincangan sandi di bodi database?
**Answer:** compare (atau bcrypt.compare / compareSync).

### Q5
**Type:** Short Answer
**Question:** Menelaah perihal eksekusi sistem API peladen *Express*, sebutkan deklarasi pemanggilan penjaring eksekutor lapis penengah (*Middleware *) yang wajib dicangkokkan merentang mencegat instruksi lajur *HTTP Request* sebelum baris operasi *Routing* disematkan; dengan spesialisasi tugas membedah serapan konfigurasi teks pelaporan JSON kiriman dari antarmuka bodi muatan *Request Payload Body JSON* (lazim memonitor serangan muatan `POST/PUT`)!
**Answer:** express.json()
