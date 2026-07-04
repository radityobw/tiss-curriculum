---
type: quiz
week: 24
day: 1
title: "Quiz: Incident Briefing & Triage"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Terkait penanganan insiden, apa fungsi utama dari aktivitas *Triage (Pemilahan)* saat analis dihadapkan dengan ribuan peringatan (*Alerts*) dari Splunk?
- [x] A. Karena waktu investigasi terbatas, *Triage* berfungsi untuk memilah dan menentukan tingkat ancaman (*Severity*) agar analis memprioritaskan peringatan yang paling kritis (misal: pergerakan *Lateral Movement*) untuk diselidiki terlebih dahulu.
- [ ] B. *Triage* berfungsi untuk menghapus log secara otomatis agar kapasitas *SIEM* tidak penuh.
- [ ] C. *Triage* dikhususkan semata-mata untuk mengisolasi penyebaran *Ransomware*.
- [ ] D. Tidak ada; fungsi *Triage* sama persis dengan *Forensic Imaging*.

### Q2
**Type:** True/False
**Question:** Dalam *Incident Response*, penetapan *Scope (Ruang Lingkup)* sejak awal insiden sangat penting karena menentukan batas area infeksi. Dengan demikian, tim keamanan tidak perlu memutus internet di seluruh perusahaan, melainkan cukup mengisolasi jaringan server yang termasuk di dalam *Scope* tersebut saja.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Mengacu pada kerangka penanganan insiden PICERL, fase apakah yang bertugas menerima laporan awal (*Incident Briefing*) dan memvalidasi kebenaran sebuah anomali?
**Answer:** Fase Identification (Identifikasi).

### Q4
**Type:** Short Answer
**Question:** Saat analis keamanan menerima laporan darurat awal (contoh: "Server tiba-tiba mati"), mengapa analis dilarang untuk langsung mencabut kabel daya *server* sebelum melakukan validasi log?
**Answer:** Karena analis harus melakukan *Triage* dan *Identification* untuk memastikan apakah itu murni insiden serangan siber (*True Positive*) atau hanya kegagalan teknis perangkat keras/jaringan (*False Positive*). Mencabut daya secara acak dapat merusak barang bukti di memori (RAM).

### Q5
**Type:** Short Answer
**Question:** Dalam laporan investigasi, apa istilah teknis (berawalan huruf E) yang mendeskripsikan titik atau pintu masuk pertama kali peretas berhasil menyusup ke dalam jaringan?
**Answer:** Entry Point.
