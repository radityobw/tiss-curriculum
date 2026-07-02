---
type: quiz
week: 21
day: 5
title: "Quiz: Lab Identifikasi Serangan"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Membedah perburuan log di lautan puluhan ribu baris teks terminal, mengapa <i>Piping</i> (yakni penggunaan simbol `|`) dirayakan laksana sihir di *Linux*?
- [x] A. Lantaran fitur <i>Piping</i> memampukan penganalisis mengalirkan keluaran (Output) data mentah dari satu perintah (misal `awk`) sebagai masukan (Input) langsung ke instruksi perintah berikutnya (misal `sort | uniq | grep`), merajut serangkaian penyayat teks secara aliran berkelanjutan *(streaming)* tanpa henti.
- [ ] B. Karena *Piping* mengonversi teks menjadi format `.evtx` Windows.
- [ ] C. Fitur *Piping* bertugas mematikan *Firewall* Linux (iptables).
- [ ] D. *Piping* adalah fitur khusus perangkat *Burp Suite*.

### Q2
**Type:** True/False
**Question:** Pada pengujian analisa ekstraksi alamat Penyerang (Top Talkers) di terminal Linux, penganalisis menyatukan perintah `awk` demi mengambil kolom IP, lantas dikawinkan dengan perintah `uniq -c` guna memfilter menghitung akumulasi kemunculan beruntun alamat IP yang sama secara.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat meluncurkan analisis percobaan terminal , apa komando Linux (dua kata atau dengan argumen `-nr`) yang biasa dijodohkan setelah `uniq` guna mengurutkan data dari yang jumlahnya paling banyak/besar ke kecil?
**Answer:** `sort -nr`.

### Q4
**Type:** Short Answer
**Question:** Saat penganalisis mengeksekusi komando Linux dan menyisipkan atribut perintah `head -n 5` di ujung akhir *Piping*, apa instruksi yang diamanahkan kepada terminal Linux tersebut?
**Answer:** Hanya tampilkan/cetak 5 baris pertama (atau 5 posisi teratas) dari hasil output teks tersebut.

### Q5
**Type:** Short Answer
**Question:** Di pembacaan log, ketika Analis SOC mengisolasi hanya IP pelaku (`10.10.55.5`) menjadi `hacker_log.txt`, lantas melontarkan perintah `grep " 200 " hacker_log.txt`, ia tengah memburu insiden insiden jenis serangan kejadian apakah?
**Answer:** Memburu riwayat serangan yang *Berhasil* (di mana si Penyerang mendapati status balasan peladen *200 OK*, pertanda ia sukses masuk).
