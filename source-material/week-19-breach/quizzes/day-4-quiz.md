---
type: quiz
week: 19
day: 4
title: "Quiz: Remediation & Mitigation Advice"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa saran perbaikan (*Remediation*) yang hanya berbunyi "Filter karakter input" dinilai sangat dangkal dan tidak profesional bagi seorang *Pentester*?
- [x] A. Karena saran tersebut tidak spesifik dan tidak *Actionable*. *Attacker* dapat dengan mudah mengelabui filter penyaring (*Bypass*) dengan teknik seperti *URL Encoding*. Saran yang baik harus merujuk pada standar arsitektur aman, contohnya penggunaan *Prepared Statement*.
- [ ] B. Karena kata 'Filter' melanggar hak cipta *Wappalyzer*.
- [ ] C. Karena pentester wajib menyuruh developer memakai *SQLMap* dalam *Remediation*.
- [ ] D. Saran tersebut tidak memiliki nilai *CVSS v3.1*.

### Q2
**Type:** True/False
**Question:** Saat menyusun bagian *Remediation*, seorang pentester tidak perlu repot mengarang resep perbaikan keamanan (*security best practices*) secara independen, melainkan sangat disarankan untuk mencantumkan URL referensi panduan standar industri (seperti *OWASP Cheat Sheet Series*) agar tim *Developer* bisa merujuk pada praktik koding yang tepat.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat memberikan saran perbaikan untuk mencegah serangan *SQL Injection*, teknik pengkodingan manipulasi basis data apa yang wajib disarankan kepada *Developer* untuk menggantikan penggabungan kueri dinamis?
**Answer:** Prepared Statements (atau Parameterized Queries).

### Q4
**Type:** Short Answer
**Question:** Dalam menyusun solusi mitigasi kerentanan *XSS* (*Cross-Site Scripting*), header pelindung peramban (*browser*) jenis apa yang lazim diwajibkan untuk diimplementasikan guna menangkis eksekusi skrip berbahaya?
**Answer:** Content Security Policy (CSP).

### Q5
**Type:** Short Answer
**Question:** Saat menemukan kerentanan eksekusi file berbahaya (*Web Shell*) melalui fitur *File Upload*, saran mitigasi *Backend* apa yang paling mutlak disarankan selain mengecek ekstensi nama berkas (guna mencegah manipulasi *Bypass*)?
**Answer:** Memvalidasi *MIME-Type* dan *Magic Bytes* (File Signature), serta melumpuhkan (mematikan) hak eksekusi skrip di folder direktori penyimpanan (*uploads*).
