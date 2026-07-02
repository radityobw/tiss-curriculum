---
type: quiz
week: 15
day: 3
title: "Quiz: Active Reconnaissance"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Berdasarkan prinsip standar pengujian keamanan sistem, alasan logis apakah yang menyebabkan Pengintaian Aktif (*Active Recon*) secara mutlak dilarang untuk dilakukan tanpa penandatanganan dokumen legal (*Rules of Engagement*)?
- [x] A. Karena taktik *Active Recon* berwujud percobaan interaksi transmisi langsung yang bising (*Noisy*) berupa peluncuran paket pemindaian IP/Port terhadap infrastruktur sasaran; akibatnya sistem pemantauan log keamanan peladen (*firewall* atau *IDS*) akan mencatat lalu lintas IP penyerang dan mendeteksinya sebagai aktivitas intrusi ilegal.
- [ ] B. Pengoperasian Nmap mengharuskan aktivasi pembayaran premi uji lisensi operasional per detik bagi setiap serangan kueri.
- [ ] C. Operasional penugasan simulasi arsitektur peladen *Active Recon* dinyatakan 100% mustahil digarap pada landasan mesin *OS Kali Linux*.
- [ ] D. Kerangka perlindungan peladen secara otomatis sanggup memantulkan muatan pelaporan payload sisipan peretasan injeksi *SQL Injection* untuk meretas balik mesin klien penyerang.

### Q2
**Type:** True/False
**Question:** Taktik peretasan *Directory Bruteforcing/Fuzzing* diracik dan digunakan pada lingkup *Bug Bounty* untuk menelusuri penempatan direktori dan tautan arsip rahasia (*hidden link*) yang tidak memiliki referensi langsung pada antarmuka situs web publik.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Dalam inventarisasi intelijen pelacak jaringan operasi pengujian (*Red Team*), perangkat lunak dengan singkatan nama *Network Mapper* manakah yang diandalkan menggempur dan memindai spesifikasi ribuan pintu *port* komunikasi sasaran guna mendeteksi celah status layanan terbuka?
**Answer:** Nmap.

### Q4
**Type:** Short Answer
**Question:** Di samping implementasi alat *Ffuf*, apakah referensi penamaan alternatif serangan (berawalan abjad 'G') yang didapuk kepiawaiannya menandingi spesifikasi iterasi ekskavasi direktori peladen aplikasi target sasaran penugasan (*Directory Fuzzing / Bruteforcing*)?
**Answer:** Gobuster (atau Dirb/Dirbuster).

### Q5
**Type:** Short Answer
**Question:** Saat pemindai intelijen *Nmap* dipanggil lantas dilesatkan membidik pemetaan sasaran, sintaks parameter *flag* tambahan apakah (bersintaks parameter awalan `-s..`) yang niscaya dipanggil buat menginisiasi deteksi rincian identitas spesifikasi *Service Version* dari instalasi aplikasi port peladen (semisal mengekstrak temuan deteksi 'Apache versi 2.4.29' maupun *Nginx*)?
**Answer:** -sV
