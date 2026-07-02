---
type: quiz
week: 14
day: 1
title: "Quiz: OWASP Top 10 Intro & Injection"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengevaluasi tingkat kerentanan peladen data SQL ketika menerima variabel inputan masukan pengguna secara murni (tanpa disanitasi), apakah bentuk rasionalisasi logis di sebalik mekanisme eksploitasi kueri injeksi peretasan bertipe `' OR '1'='1`?
- [ ] A. Kueri tersebut mengandung parameter perintah eksekusi tersembunyi yang ditugaskan khusus untuk mereset mesin Basis Data ke konfigurasi pabrik asalnya.
- [ ] B. Perintah ini meretas infrastruktur lapisan jaringan komunikasi HTTP lantas merombaknya memaksa protokol transmisi menjadi TCP berbalut soket utuh.
- [x] C. Logika operasi kondisi *boolean* silang `'1'='1'` menyuguhkan kondisi komparasi pembuktian statis yang senantiasa dievaluasi bernilai mutlak benar (TRUE). Akibatnya, eksekutor *Database* otomatis memintas dan mengabaikan tuntutan parameter syarat *username* yang keliru, lalu secara otomatis mengekstrak serta menyerahkan seluruh akses rincian informasi pada baris pelaporan arsip tabel tersebut.
- [ ] D. Susunan sintaks skrip tersebut sejatinya adalah pengujian kata sandi universal bawaan cadangan (*backdoor default*) rilis standar peladen SQL dari pabrikan SQLite.

### Q2
**Type:** True/False
**Question:** Ketika pemrogram peladen merangkai rutinitas fungsi kueri pencegahan serangan operasi *SQLi*, praktik arsitektur penulisan parameter kueri yang sangat dilarang dan diharamkan penerapannya adalah mekanisme penyambungan langsung masukan input peramban klien secara menempel utuh ke kerangka kueri memori SQL yang murni memanfaatkan deklarasi simbol operator konkatensi manipulasi sambungan string pengikatan abjad operasi `+` (semisal konfigurasi pemanggilan sintaks dinamis `"SELECT * WHERE u='" + nama_input_pengguna + "'"`).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Apakah akronim kepanjangan identitas nama lembaga standar keamanan siber nirlaba dunia (organisasi independen parameter global pemantau kerentanan sistem web) yang masyhur mempublikasikan secara periodik berkas referensial pengelompokan panduan dokumentasi standar pemetaan perankingan posisi kelas peringkat 10 taksonomi kerentanan peladen web eksploitasi aplikasi parameter internet paling mematikan sedunia?
**Answer:** OWASP (Open Worldwide Application Security Project).

### Q4
**Type:** Short Answer
**Question:** Guna menangkis pembajakan paksa serangan kueri penyusupan memori parameter fungsi mematikan insiden operasional *SQL Injection*, taktik perumusan pengerjaan spesifikasi fungsi tameng metode perlindungan standar peladen apakah yang fardhu diimplementasikan arsitek *Backend* di kerangka integrasi perutean penulisan koneksi program (yang mengharuskan implementasi integrasi pemakaian tata bahasa deklarasi simbol penanda khusus pengikatan argumen `?` sebagai substitusi nilai dinamis parameter pelindung variabel klien di sintaks penulisan operasional parameternya)?
**Answer:** Parameterized Queries (Kueri Berparameter / Prepared Statements).

### Q5
**Type:** Short Answer
**Question:** Bilamana seorang admin *hacker/pentester* spesialis meretas jaringan web mengeksploitasi konfigurasi penulisan input lantas menyelipkan modifikasi rincian aksara dwikarakter simbol kurang bertumpuk berjejeran spesifik `--` menyambung melekat ekor pengetikan pada rute payload masukan skrip eksekusi *SQL Injection* (khusus arsitektur eksekusi peladen MySQL/SQLite), maknawi sandi gaib apakah yang diartikan/diinstruksikan kedua simbol peretas tersebut bagi eksekutor kompilator Database peladen saat menerima barisan kueri tersebut?
**Answer:** Komentar (sehingga sisa kerangka kueri operasional kode eksekusi pembanding fungsionalitas SQL pengecekan bersangkutan di belakang sisa instruksi bakal langsung dibuang/diabaikan secara utuh prosesnya oleh mesin Database peladen).
