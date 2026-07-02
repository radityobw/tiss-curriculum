---
type: quiz
week: 6
day: 3
title: "Quiz: DNS, ARP, DHCP, ICMP"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Jika kita sudah memiliki alamat IP yang sanggup melacak sasaran di internet secara global, mengapa kita masih membutuhkan protokol ARP ketika mengoperasikan jaringan di tingkat rumah atau LAN yang sama?
- [ ] A. Karena ARP bekerja untuk memperkuat sinyal IP agar tak hilang ditelan dinding.
- [ ] B. Karena peramban (*browser*) menolak masuk jika ARP dimatikan.
- [x] C. Karena peranti komunikasi lokal tingkat Layer 2 (seperti Switch) tak memahami IP dan bertukar data melalui MAC Address, sehingga ARP diperlukan untuk menyepadankan nilai IP terhadap MAC Address tetangganya.
- [ ] D. Karena ARP berfungsi membagikan IP gratis ke semua orang.

### Q2
**Type:** True/False
**Question:** Protokol DHCP bertugas memastikan kelancaran jalan koneksi diagnostik dengan senantiasa menyiarkan paket permohonan "Halo" yang berjenis Echo Request ke luar jaringan.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Aplikasi pelacak diagnostik jaringan (*terminal tool*) legendaris apakah yang mengandalkan sistem sirkulasi paket protokol kesehatan ICMP?
**Answer:** ping (atau traceroute/tracert).

### Q4
**Type:** Short Answer
**Question:** Singkatan siklus percakapan 4 langkah "D-O-R-A" dalam sistem peminjaman nomor IP di server DHCP mengacu pada kata apa saja?
**Answer:** Discover, Offer, Request, Acknowledge.

### Q5
**Type:** Short Answer
**Question:** Di atas konektivitas transport UDP port berapakah peladen DNS beroperasi menanti pertanyaan nama laman?
**Answer:** Port 53.
