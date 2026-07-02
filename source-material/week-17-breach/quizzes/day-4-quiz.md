---
type: quiz
week: 17
day: 4
title: "Quiz: Chaining Vulnerabilities"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di ekosistem *Bug Bounty*, apa alasan utama seorang pentester profesional menolak untuk menyerah pada temuan kerentanan berisiko rendah (seperti *Open Redirect* atau *Self-XSS*) dan memilih untuk menerapkan teknik *Chaining Vulnerabilities*?
- [ ] A. Karena panduan OWASP Top 10 secara tegas melarang pentester melaporkan temuan celah tunggal.
- [x] B. Celah kerentanan yang terisolasi (seperti *Self-XSS*) seringkali langsung ditolak oleh program *Bug Bounty* karena tidak memiliki vektor ancaman yang nyata. Namun, ketika celah tersebut digabungkan (*Chaining*) dengan kerentanan lain (misal *SSRF*), rentetannya dapat memicu eksploitasi fatal (seperti *RCE/Account Takeover*) yang langsung mendongkrak tingkat keparahan (*Severity*) menjadi *High/Critical*.
- [ ] C. Metode *Chaining* mewajibkan penggunaan alat otomatis *SQLMap* untuk membongkar kerentanan CSRF.
- [ ] D. Metode *Chaining Vulnerabilities* adalah satu-satunya cara untuk membypass Web Application Firewall (WAF).

### Q2
**Type:** True/False
**Question:** Kerentanan *Self-XSS* (injeksi skrip yang hanya bisa menyerang browser milik pengirimnya sendiri) mustahil membahayakan pengguna lain di luar sana, KECUALI jika kerentanan tersebut berhasil digabungkan (*Chained*) dengan serangan seperti *CSRF* atau *SSRF* untuk menjebak dan memaksa korban merender halaman yang berisi *Self-XSS* tersebut tanpa disadari.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Ketika pentester berhasil mengeksploitasi kelalaian *CSRF* pada elemen formulir "Ubah Email", sehingga alamat email korban terganti menjadi email milik peretas, serangan puncak apakah yang dapat langsung dieksekusi peretas selanjutnya dengan mengeklik fitur *Forgot Password*?
**Answer:** Pengambilalihan akun (Account Takeover / ATO).

### Q4
**Type:** Short Answer
**Question:** Apa sebutan terminologi (dalam bahasa Inggris) untuk seni atau taktik peretasan yang menggabungkan dua atau lebih celah kerentanan berskala kecil menjadi satu rentetan serangan eksploitasi yang masif dan fatal?
**Answer:** Chaining Vulnerabilities (atau Vulnerability Chaining).

### Q5
**Type:** Short Answer
**Question:** Bila pentester merantai celah *IDOR* (kemampuan membaca dokumen milik orang lain via manipulasi URL) dengan kerentanan *Stored XSS* (menanamkan skrip ke dalam dokumen tersebut), maka saat Admin membuka dokumen PDF jebakan tersebut, pentester sukses merampas data identitas rahasia apa milik sang admin?
**Answer:** Session Cookie (atau Cookie Sesi / Token Autentikasi).
