---
type: quiz
week: 21
day: 4
title: "Quiz: Pattern Recognition"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa Analis SOC dituntut untuk menguasai pengenalan pola (*Pattern Recognition*) ketimbang membaca seluruh teks log secara manual?
- [x] A. Karena *server* produksi menghasilkan ribuan hingga jutaan baris log setiap detiknya. Membacanya secara berurutan tidak efisien. Pengenalan pola memungkinkan Analis mendeteksi anomali dengan cepat melalui visualisasi lonjakan data.
- [ ] B. Karena sistem SIEM tidak dapat memuat teks log tanpa adanya pola tertentu.
- [ ] C. Ilmu *Pattern Recognition* hanya diwajibkan bagi peretas (*Red Team*).
- [ ] D. Karena membaca log secara berurutan akan menurunkan skor *CVSS v3.1*.

### Q2
**Type:** True/False
**Question:** Jika Analis menemukan rentetan log berstatus *404 Not Found* yang terus-menerus menargetkan direktori tersembunyi (seperti `/.git/`, `/.env`, `/backup/`), hal ini merupakan indikasi kuat dari serangan *Vulnerability Scanning* (pemindaian kerentanan).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada analisis log, apa sebutan untuk serangan di mana satu alamat IP secara terus-menerus melakukan percobaan *login* dan menghasilkan rentetan log berstatus *Failed* atau *401 Unauthorized*?
**Answer:** Brute Force (atau Credential Stuffing / Password Guessing).

### Q4
**Type:** Short Answer
**Question:** Jika sebuah *server database* internal yang seharusnya tertutup secara tiba-tiba mengirimkan data berukuran raksasa (misalnya: 10 Gigabytes) ke jaringan publik eksternal yang tidak dikenal, indikasi insiden apakah ini?
**Answer:** Data Exfiltration (Pencurian atau pengurasan data).

### Q5
**Type:** Short Answer
**Question:** Dalam analisis *Windows Event Log*, jika terdapat rentetan log *Event ID 4625* secara beruntun dan mendadak diakhiri dengan satu log *Event ID 4624*, insiden apa yang baru saja terjadi?
**Answer:** Serangan Brute Force yang berhasil (Penyerang sukses menebak sandi dan *Logon Success*).
