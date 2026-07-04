---
type: quiz
week: 18
day: 4
title: "Quiz: Other Tools (ZAP, ffuf, nikto)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Alat bantu apakah buatan komunitas OWASP yang sering digunakan sebagai alternatif (100% Gratis) bagi pentester yang tidak memiliki lisensi berbayar *Burp Scanner Professional*?
- [x] A. *OWASP ZAP (Zed Attack Proxy)*, perangkat *Proxy* dan pemindai otomatis (*Automated Vulnerability Scanner*) yang mampu mendeteksi kerentanan seperti *SQLi* dan *XSS* secara gratis.
- [ ] B. *OWASP Mutillidae*.
- [ ] C. *PortSwigger Community*.
- [ ] D. *Shodan*.

### Q2
**Type:** True/False
**Question:** Pemindai berbasis terminal bernama *Nikto* digunakan khusus untuk mendeteksi kelalaian konfigurasi *server* (*Security Misconfigurations*), seperti ketiadaan *Security Headers*, direktori sensitif yang terbuka, atau penggunaan versi *software* (*Apache/PHP*) yang sudah usang.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Apa nama perangkat *Fuzzing* berbasis bahasa *Golang* (berawalan huruf f) yang terkenal dengan kemampuannya melontarkan ribuan *payload Brute-force* ke parameter web dengan kecepatan sangat tinggi?
**Answer:** Ffuf (Fuzz Faster U Fool).

### Q4
**Type:** Short Answer
**Question:** Mengapa pemindai *Nikto* sangat TIDAK disarankan untuk digunakan pada tahap *Passive Reconnaissance* (Pengintaian Pasif)?
**Answer:** Karena *Nikto* sangat bising (*Noisy*) dan agresif dalam mengirimkan *request*, sehingga akan langsung memicu peringatan pada sistem *Firewall* atau IDS target.

### Q5
**Type:** Short Answer
**Question:** Pemindai otomatis buatan OWASP apakah yang sering digabungkan penggunaannya dengan *Burp Suite*, di mana pemindai tersebut melakukan pemindaian massal awal, lalu temuan celahnya diuji secara manual menggunakan *Burp Repeater*?
**Answer:** OWASP ZAP (ZAP).
