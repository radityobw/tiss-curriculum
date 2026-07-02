---
type: quiz
week: 21
day: 4
title: "Quiz: Pattern Recognition"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di filosofi keilmuan <i>Pattern Recognition</i> korporasi, mengapa Analis SOC dituntut wajib mengenali gelagat serangan (Pola visual) ketimbang membaca seluruh teks log kata demi kata?
- [x] A. Lantaran satu peladen server korporasi dapat memuntahkan ribuan hingga jutaan baris log per menit. Membacanya secara berurutan sangat tidak efisien. Pengenalan pola memampukan Analis seketika memilah "jejak kaki serigala di lautan jejak kelinci" hanya lewat sekilas tatapan data anomali visual.
- [ ] B. Karena sistem SIEM menolak memuat teks log tanpa pola.
- [ ] C. Ilmu pola hanya dituntut bagi peretas eksploitasi (Red Team).
- [ ] D. Lantaran membaca log menurunkan *CVSS v3.1*.

### Q2
**Type:** True/False
**Question:** Saat penganalisis mendapati log web yang mencetak rentetan balasan <i>404 Not Found</i> secara gencar pada permintaan alamat direktori aneh (contoh: `/.git/`, `/.env`, `/backup/`), fenomena ini merupakan ciri pola serangan <i>Vulnerability Scanning</i> (pemindaian kerentanan).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada pengintaian log, apa sebutan serangan ketika satu alamat IP mengeksekusi ratusan tebakan log otentikasi yang menghasilkan deretan panjang log berstatus *Failed/401 Unauthorized*?
**Answer:** Brute Force (atau Credential Stuffing / Password Guessing).

### Q4
**Type:** Short Answer
**Question:** Saat sebuah server internal yang seharusnya pasif, secara tiba-tiba memuntahkan aliran lalu-lintas data (Misal: 10 Gigabytes transfer keluar jaringan menuju IP asing), indikasi insiden serangan apa yang sedang terjadi ini?
**Answer:** Data Exfiltration (Pencurian atau pengurasan Data).

### Q5
**Type:** Short Answer
**Question:** Di analisa *Windows Event Log*, pola beruntun sandi angka <i>Event ID 4625</i> yang bermuara lantas ditutup oleh satu baris kemunculan angka <i>Event ID 4624</i>, menyuguhkan indikasi peretasan insiden apa?
**Answer:** Serangan Brute Force yang berhasil (Peretas sukses menebak sandi dan <i>Logon Success</i>).
