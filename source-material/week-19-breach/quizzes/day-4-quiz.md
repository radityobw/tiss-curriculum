---
type: quiz
week: 19
day: 4
title: "Quiz: Remediation & Mitigation Advice"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengurai taktik, mengapa saran perbaikan *Remediation* yang berbunyi "Filter karakter input" dinilai sangat amatiran dan diharamkan bagi *Pentester*?
- [x] A. Lantaran saran tersebut berstatus "Mengambang" (Tidak *Actionable*). Peretas hitam (Attacker) masih leluasa masuk tameng filter penyaring bermodalkan taktik manipulasi *Bypass* (seperti *URL Encoding*). Saran haruslah merujuk arsitektur, contoh: *Prepared Statement*.
- [ ] B. Karena kata 'Filter' melanggar hak cipta *Wappalyzer*.
- [ ] C. Karena peretas wajib memakai *SQLMap* dalam *Remediation*.
- [ ] D. Saran tersebut tidak mencakup *CVSS v3.1*.

### Q2
**Type:** True/False
**Question:** Di penu *Remediation*, penganalisis tak perlu repot mengarang resep perbaikan secara independen lantaran cukup mencantumkan URL referensi (seperti <i>OWASP Cheat Sheet Series</i>) agar *Developer* korporasi bisa menyalin resep obat Koding langsung dari.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Ketika meluncurkan saran perbaikan *SQLi*, taktik koding (bawaan PHP PDO) apakah yang wajib dianut Developer menggantikan kueri dinamis?
**Answer:** Prepared Statements (atau Parameterized Queries).

### Q4
**Type:** Short Answer
**Question:** Di peracikan resep mitigasi *XSS*, fitur tajuk (header) pelindung peramban jenis apa yang lumrah diwajibkan agar diimplementasikan menangkis eksekusi racun skrip?
**Answer:** Content Security Policy (CSP).

### Q5
**Type:** Short Answer
**Question:** Ketika menyusupkan cangkang *Web Shell PHP* lewat lubang *File Upload*, saran mitigasi di *Backend* apa yang paling telak mencegah unggahan gambar dimanipulasi ekstensi palsu?
**Answer:** Memvalidasi berdasarkan isi berkas yakni *MIME-Type* dan *Magic Bytes* (File Signature), serta mematikan hak eksekusi skrip di folder penyimpanan.
