---
type: quiz
week: 6
day: 5
title: "Quiz: Lab Analisis Trafik Wireshark"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa kredensial (*credentials*) kata sandimu terlihat secara jelas (*plaintext*) di log Wireshark saat kamu melakukan proses login pada *testphp.vulnweb.com* dalam *Lab Mission*?
- [ ] A. Karena pengetikan dilakukan dengan lambat.
- [ ] B. Karena situs web tersebut diam-diam memasang *keylogger*.
- [x] C. Karena formulir login pada situs percobaan tersebut tidak menggunakan enkripsi (berbasis HTTP biasa), bukan protokol HTTPS yang aman (berbasis TLS).
- [ ] D. Karena Wireshark selalu berhasil mendeskripsi (*decrypt*) HTTPS secara kilat.

### Q2
**Type:** True/False
**Question:** Jika kita menggunakan filter `tcp` di Wireshark, maka lalu lintas yang ditampilkan hanya mencakup protokol tak berenkripsi (seperti HTTP) dan akan mengabaikan lalu lintas TCP lainnya seperti FTP atau SSH.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Berada di layer (Lapisan OSI) manakah rincian parameter *HTTP request* yang ditampilkan pada jendela *Packet Details* di Wireshark?
**Answer:** Layer 7 (Application Layer).

### Q4
**Type:** Short Answer
**Question:** Di jendela Wireshark manakah analis dapat mengobservasi nilai heksadesimal (*Hex*) beserta representasi karakter mentahnya (*ASCII*) dari sebuah paket?
**Answer:** Packet Bytes.

### Q5
**Type:** Short Answer
**Question:** Apa istilah teknis untuk metode peretasan di mana penyerang secara diam-diam menyadap dan membaca paket jaringan yang melintas?
**Answer:** Packet Sniffer (atau Man-in-the-Middle / Sniffing).
