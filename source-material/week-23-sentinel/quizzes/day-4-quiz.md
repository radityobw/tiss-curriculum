---
type: quiz
week: 23
day: 4
title: "Quiz: Memory & Disk Forensics"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Saat menangani insiden siber, bagaimana spesialis forensik menetapkan prioritas akuisisi (pengumpulan bukti) antara *Disk Forensics* dan *Memory Forensics*?
- [x] A. *Memory Forensics* menjadi prioritas utama untuk diselamatkan, karena data di dalam RAM bersifat *Volatile* (mudah hilang) jika komputer dimatikan atau di-restart. Sebaliknya, *Disk Forensics* (Hard disk/SSD) bersifat permanen (*Non-Volatile*) sehingga datanya tetap aman meski komputer dimatikan.
- [ ] B. *Disk Forensics* khusus digunakan untuk sistem *Linux*, sementara *Memory Forensics* digunakan untuk *Windows*.
- [ ] C. *Disk Forensics* menganalisis log melalui *Splunk*, sementara *Memory Forensics* menganalisis jaringan menggunakan *Wireshark*.
- [ ] D. Tidak ada perbedaan prioritas, keduanya diekstraksi secara bersamaan menggunakan alat yang sama.

### Q2
**Type:** True/False
**Question:** Jika sebuah *server* sedang diserang oleh *Ransomware* yang aktif mengenkripsi *file*, prosedur mematikan *server* (*Shutdown*) sangat dilarang. Hal ini karena Kunci Dekripsi (*Decryption Key*) dari *Ransomware* tersebut saat itu sedang berada di dalam memori RAM, dan mematikan server akan menghilangkan kunci tersebut selamanya.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Apa istilah yang digunakan untuk mengklasifikasikan sifat dari penyimpanan sementara (seperti RAM) di mana datanya akan langsung lenyap seketika jika aliran listrik diputus?
**Answer:** Volatile (Atau Volatility).

### Q4
**Type:** Short Answer
**Question:** Saat analis forensik membedah isi salinan memori RAM (*Memory Dump*), program penganalisis berbasis *Command-line Interface (CLI)* Python apa yang paling sering digunakan?
**Answer:** Volatility Framework (Atau Volatility).

### Q5
**Type:** Short Answer
**Question:** Di ranah *Disk Forensics*, jika peretas telah menghapus sebuah *file* penting secara permanen menggunakan perintah *Shift+Delete*, apakah *file* tersebut langsung hilang mutlak dan tidak bisa diselamatkan sama sekali dari *Hard Disk*? (Jawab dengan Ya atau Tidak beserta alasannya secara singkat).
**Answer:** Tidak. (Sistem hanya menghapus "penanda lokasi/indeks" *file* tersebut. Data aslinya masih berada di piringan *Hard Disk* dan bisa dipulihkan menggunakan *software Data Recovery*, selama sektor disk tersebut belum ditimpa (di-`overwrite`) oleh *file* baru).
