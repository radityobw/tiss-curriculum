---
type: quiz
week: 8
day: 3
title: "Quiz: Ownership & Privilege Escalation"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Jika kita membincangkan prinsip *best practice* keamanan tertinggi administrasi Linux, mengapa OS mewajibkan eksekusi `sudo` dan berupaya melarang login mentah-mentah ke dalam wujud akun tunggal *Root*?
- [x] A. Sudo meredam amukan destruktif sistem keliru dengan meminta persetujuan sadar tiap kali, menyulitkan pendobrakan tipe paksa pelacak (*brute-force*), serta mempuni memetakan jejak *log* individual akuntabilitas identitas asli petugasnya saat server mengalami kecelakaan.
- [ ] B. Karena akun Root memang tidak pernah ditanamkan dan tak nyata tertulis dari sananya semenjak OS diluncurkan, hanya fiktif.
- [ ] C. Lantaran Microsoft melarang peretasan dengan OS Linux.
- [ ] D. Supaya kecepatan rotasi RAM (*Read-Access Memory*) server lebih stabil.

### Q2
**Type:** True/False
**Question:** Siapapun bebas kapan pun meneriakkan komando penggeser haluan `chown` supaya berkuasa merebut dan merombak akta kepemilikan dokumen tugas penting punya kolega kampusnya.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Sindikat peretas acapkali berusaha menggandakan atau meningkatkan tingkatan hirarki otonomi cengkeramannya yang sebatas strata murahan (*www-data*) buat meroket menapaki status "Tuhan Sistem" (Root). Apakah padanan istilah bagi teknik peninggian hak otonomi spesifik ini?
**Answer:** Privilege Escalation (Eskalasi Hak Istimewa).

### Q4
**Type:** Short Answer
**Question:** Apa mantra pendobrak (kata komando ajaib peminjam kekuatan *Superuser*) yang ditambahkan ke awal kalimat agar membebaskan eksekusi operasi khusus yang semula dipasung notifikasi *Permission Denied*?
**Answer:** sudo (Superuser Do).

### Q5
**Type:** Short Answer
**Question:** Selain kepemilikan perorangan (*User Owner*), properti data kepemilikan apakah (yang diampu atribut ke-2) pada setiap fail dalam Linux?
**Answer:** Group Owner (Grup atau Kelompok).
