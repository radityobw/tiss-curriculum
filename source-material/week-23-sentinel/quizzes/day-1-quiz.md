---
type: quiz
week: 23
day: 1
title: "Quiz: Proactive vs Reactive Security"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Terkait dengan pendekatan keamanan sistem korporasi, apa perbedaan fundamental antara paradigma operasional *Reactive Security* bila dibandingkan dengan *Proactive Security (Threat Hunting)*?
- [x] A. *Reactive Security* bersifat pasif dan bergantung pada mesin sensor (seperti SIEM) untuk menghasilkan peringatan (*Alerts*) sebelum memberikan respons. Sebaliknya, *Proactive Security* berpusat pada analis yang secara aktif dan berkala menyusuri log jaringan untuk mendeteksi ancaman canggih (*APT*) yang berhasil menghindari deteksi otomatis.
- [ ] B. *Reactive Security* menggunakan kueri *Splunk*, sementara *Proactive Security* menggunakan *Suricata*.
- [ ] C. *Threat Hunting* spesifik dikhususkan untuk mencari kata sandi *RDP* yang gagal.
- [ ] D. Tidak ada perbedaan; keduanya sama-sama beroperasi otomatis.

### Q2
**Type:** True/False
**Question:** Di dalam praktik operasional *Threat Hunting*, analis tidak melakukan penyisiran log secara acak. Mereka bekerja berdasarkan *Hypothesis-Driven Approach (Pendekatan Berbasis Hipotesis)*, yakni merumuskan dugaan taktis spesifik (misal: "Mengasumsikan peretas mengeksploitasi akses VPN") terlebih dahulu sebelum memulai analisis data.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Mengapa peran analis manusia (*Human Element*) dalam proses perburuan ancaman siber dinilai belum dapat sepenuhnya digantikan oleh kemampuan mesin kecerdasan buatan (*AI*)?
**Answer:** Karena mesin (*AI*) pada dasarnya hanya merespons aturan atau pola (Signatures/Rules) yang telah dikenalnya. Sementara itu, peretas tingkat lanjut terus menciptakan metode serangan baru (*Zero-Day*). Peran intuisi analitis dan insting logis deduktif manusia sangat diperlukan untuk mengenali dan memecahkan skenario serangan yang tidak wajar.

### Q4
**Type:** Short Answer
**Question:** Saat analis keamanan siber (*Threat Hunter*) memformulasikan perburuan, dari manakah biasanya analis memperoleh dasar argumen untuk merumuskan *Hipotesis* investigasinya? (Petunjuk: Sumber data laporan ancaman).
**Answer:** Dari platform *Threat Intelligence* (Intelijen Ancaman), publikasi kerentanan perangkat (berita CVE), atau referensi pola serangan dari *MITRE ATT&CK*.

### Q5
**Type:** Short Answer
**Question:** Dalam klasifikasi tingkatan ancaman keamanan siber, apa istilah untuk kelompok peretas terorganisasi (biasanya disponsori negara bagian) yang berfokus pada penyusupan jaringan secara tersembunyi jangka panjang tanpa memicu sistem pengawasan standar? (Berawalan huruf A).
**Answer:** APT (Advanced Persistent Threats).
