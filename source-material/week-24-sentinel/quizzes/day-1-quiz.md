---
type: quiz
week: 24
day: 1
title: "Quiz: Incident Briefing & Triage"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Terkait implementasi penanganan insiden korporasi, apa fungsi utama dari taktik mitigasi *Triage (Pemilahan)* saat analis SOC dihadapkan dengan ribuan peringatan *SIEM Splunk*?
- [x] A. Karena tim SOC memiliki keterbatasan waktu investigasi, *Triage* difungsikan untuk memilah dan menetapkan tingkat keparahan (*Severity*) guna memprioritaskan penyaringan peringatan (*Alerts*) mana yang paling kritis (Misalnya deteksi pergerakan *Lateral Movement*) untuk diselidiki terlebih dahulu.
- [ ] B. *Triage* difungsikan untuk mengeksekusi penghapusan log secara otomatis agar batas ambang kapasitas penyimpanan data *SIEM* tidak melampaui limit.
- [ ] C. *Triage* dikhususkan semata-mata untuk merancang mitigasi isolasi infeksi penyebaran *Ransomware*.
- [ ] D. Tidak terdapat kegunaan khusus; fungsi *Triage* serupa identik secara dengan *Forensic Imaging*.

### Q2
**Type:** True/False
**Question:** Di ekosistem *Incident Response*, penetapan *Scope (Ruang Lingkup)* sejak awal insiden merupakan hal fundamental dikarenakan parameter ini mendefinisikan batasan jumlah sistem yang terekspos. Dengan demikian, tim keamanan tak perlu memutuskan akses internet di seluruh struktur jaringan instalasi bisnis, melainkan eksklusif pada segmen IP perangkat yang berstatus termuat dalam *Scope*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Mengacu pada kerangka penanggulangan, fase apakah (Berawalan huruf I) dalam struktur *PICERL* yang bertugas memvalidasi *Incident Briefing* (Laporan awal) dan memulai *Triage*?
**Answer:** Fase Identification (Tahap Identifikasi).

### Q4
**Type:** Short Answer
**Question:** Saat analis keamanan menerima laporan eskalasi darurat (Contoh : "Server data utama instansi tak responsif"), mengapa instruksi isolasi mutlak pencabutan kabel tenaga dilarang dilakukan sebelum validasi?
**Answer:** Karena prosedur penanganan insiden mewajibkan eksekusi validasi fungsi *Identification (Validasi Insiden/Scope)* dan *Triage* secara untuk memvalidasi konfirmasi insiden (*True Positive*) ataukah itu hanya malfungsi jaringan standar (Indikasi fungsi *False Positive*).

### Q5
**Type:** Short Answer
**Question:** Dalam laporan investigasi kerentanan keamanan siber, terminologi teknis apa (Berawalan huruf E) yang mendefinisikan vektor akses sistem atau rute spesifik tempat aktor peretas pertama kali berhasil meretas perlindungan korporat?
**Answer:** Entry Point (Atau Titik Masuk infiltrasi fungsi).
