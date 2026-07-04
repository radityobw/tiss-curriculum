---
type: quiz
week: 23
day: 1
title: "Quiz: Proactive vs Reactive Security"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan fundamental antara paradigma operasional *Reactive Security* dibandingkan dengan *Proactive Security (Threat Hunting)*?
- [x] A. *Reactive Security* bersifat pasif dan bergantung pada mesin sensor (seperti SIEM) untuk menghasilkan peringatan (*Alerts*) sebelum Analis memberikan respons. Sebaliknya, *Proactive Security* berpusat pada Analis yang secara aktif dan berkala menyusuri log jaringan untuk mencari ancaman canggih (*APT*) yang tidak memicu sensor.
- [ ] B. *Reactive Security* menggunakan *Splunk*, sementara *Proactive Security* menggunakan *Suricata*.
- [ ] C. *Threat Hunting* spesifik dikhususkan untuk mencari kata sandi *RDP* yang salah ketik.
- [ ] D. Tidak ada perbedaan; keduanya sama-sama digerakkan oleh kecerdasan buatan (AI) tanpa campur tangan manusia.

### Q2
**Type:** True/False
**Question:** Di dalam praktik operasional *Threat Hunting*, Analis tidak melakukan pencarian log secara acak. Mereka bekerja berdasarkan *Hypothesis-Driven Approach (Pendekatan Berbasis Hipotesis)*, yakni merumuskan dugaan spesifik (misal: "Saya menduga peretas sedang mengeksploitasi akses VPN lama") terlebih dahulu sebelum memulai analisis data.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Mengapa peran insting dan analitis manusia (*Human Element*) dalam proses perburuan ancaman siber dinilai belum dapat digantikan oleh mesin otomatis atau kecerdasan buatan (*AI*)?
**Answer:** Karena mesin dan AI beroperasi secara kaku menggunakan pola (*Rules/Signatures*) yang sudah dikenalnya. Sementara itu, kelompok peretas canggih (*APT*) sering menggunakan metode baru (*Zero-Day*) atau menyamarkan serangannya sebagai aktivitas normal, sehingga membutuhkan intuisi dan penalaran manusia untuk mendeteksi kejanggalan tersebut.

### Q4
**Type:** Short Answer
**Question:** Saat Analis (*Threat Hunter*) merumuskan skenario perburuan, dari manakah biasanya ia memperoleh dasar informasi untuk menyusun *Hipotesis* investigasinya?
**Answer:** Dari laporan *Threat Intelligence* (Intelijen Ancaman), berita kerentanan (*CVE*), atau mempelajari pola peretasan dari referensi industri seperti *MITRE ATT&CK*.

### Q5
**Type:** Short Answer
**Question:** Dalam tingkatan ancaman siber, apa sebutan untuk kelompok peretas terorganisasi (biasanya disponsori oleh negara) yang memiliki taktik sangat canggih dan bertujuan menyusup secara diam-diam dalam jangka waktu panjang tanpa terdeteksi?
**Answer:** APT (Advanced Persistent Threats).
