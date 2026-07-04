---
type: quiz
week: 17
day: 4
title: "Quiz: Chaining Vulnerabilities"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di ekosistem *Bug Bounty*, apa alasan utama seorang pentester profesional tidak mengabaikan temuan kerentanan berisiko rendah (seperti *Open Redirect* atau *Self-XSS*) dan memilih untuk menerapkan teknik *Chaining Vulnerabilities*?
- [ ] A. Karena panduan OWASP Top 10 melarang pentester melaporkan temuan celah tunggal.
- [x] B. Kerentanan yang terisolasi (seperti *Self-XSS*) seringkali ditolak karena tidak memiliki dampak yang nyata. Namun, jika celah tersebut digabungkan (*Chaining*) dengan kerentanan lain (misal *SSRF*), rentetannya dapat memicu eksploitasi fatal (seperti *RCE* atau *Account Takeover*) yang langsung mendongkrak tingkat keparahan (*Severity*) menjadi *High/Critical*.
- [ ] C. Metode *Chaining* mewajibkan penggunaan alat otomatis *SQLMap* untuk membongkar kerentanan CSRF.
- [ ] D. Metode *Chaining Vulnerabilities* adalah satu-satunya cara untuk membypass Web Application Firewall (WAF).

### Q2
**Type:** True/False
**Question:** Kerentanan *Self-XSS* (injeksi skrip yang hanya bisa menyerang browser milik penyerang sendiri) tidak akan membahayakan pengguna lain di luar sana, KECUALI jika kerentanan tersebut berhasil digabungkan (*Chained*) dengan serangan seperti *CSRF* atau *SSRF* untuk memaksa korban membuka halaman yang memuat skrip tersebut.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Ketika pentester berhasil mengeksploitasi celah *CSRF* pada elemen formulir "Ubah Email", sehingga alamat email korban terganti menjadi email milik peretas, serangan puncak apakah yang dapat langsung dieksekusi peretas selanjutnya dengan mengeklik fitur *Forgot Password*?
**Answer:** Pengambilalihan akun (Account Takeover / ATO).

### Q4
**Type:** Short Answer
**Question:** Apa terminologi untuk teknik peretasan yang menggabungkan dua atau lebih celah kerentanan berskala kecil menjadi satu rentetan serangan eksploitasi yang masif dan berdampak besar?
**Answer:** Chaining Vulnerabilities (atau Vulnerability Chaining).

### Q5
**Type:** Short Answer
**Question:** Bila pentester merantai celah *IDOR* (kemampuan membaca dokumen milik orang lain via manipulasi URL) dengan kerentanan *Stored XSS* (menanamkan skrip ke dalam dokumen tersebut), maka saat Admin membuka dokumen PDF jebakan tersebut, pentester berhasil mencuri data rahasia apa milik sang admin?
**Answer:** Session Cookie (atau Cookie Sesi / Token Autentikasi).
