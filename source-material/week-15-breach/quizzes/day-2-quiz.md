---
type: quiz
week: 15
day: 2
title: "Quiz: Passive Reconnaissance"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan operasional yang paling mendasar antara *Passive Reconnaissance* (Pengintaian Pasif) dan *Active Reconnaissance* (Pengintaian Aktif)?
- [ ] A. *Active Recon* menghabiskan RAM hingga 100%, sementara *Passive Recon* hanya menggunakan CPU.
- [ ] B. *Passive Recon* digunakan khusus untuk mencari file PDF, sedangkan *Active Recon* untuk mencari file Excel.
- [x] C. *Passive Recon* mengumpulkan informasi melalui pihak ketiga (seperti Google, Shodan, WHOIS) tanpa mengirimkan paket/request langsung ke server target, sehingga tidak memicu alarm keamanan. Sebaliknya, *Active Recon* mengirimkan koneksi langsung ke server target yang berisiko tercatat di *log* sistem keamanan mereka.
- [ ] D. *Passive Recon* digunakan untuk serangan SQLi, sedangkan *Active Recon* digunakan untuk serangan XSS.

### Q2
**Type:** True/False
**Question:** *theHarvester* adalah alat (tool) yang dirancang secara khusus untuk melakukan pemindaian (scanning) port SSH yang terbuka di server target.
**Answer:** False

*(Penjelasan: theHarvester digunakan untuk mengumpulkan alamat email, subdomain, dan profil dari sumber terbuka (OSINT) seperti LinkedIn atau Google, bukan untuk pemindaian port).*

### Q3
**Type:** Short Answer
**Question:** Operator *Google Dorking* apa yang digunakan untuk membatasi pencarian hanya pada satu domain tertentu (misalnya, hanya mencari di `tiss.or.id`)?
**Answer:** site:

### Q4
**Type:** Short Answer
**Question:** Mesin pencari khusus apa (sering disebut mesin pencari hacker) yang digunakan untuk mendeteksi perangkat IoT, router, dan kamera CCTV yang terhubung secara bebas ke internet publik?
**Answer:** Shodan

### Q5
**Type:** Short Answer
**Question:** Perintah terminal Linux apa yang digunakan untuk melacak informasi registrasi (nama pemilik, kontak email) dari sebuah domain?
**Answer:** whois
