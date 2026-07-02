---
type: quiz
week: 23
day: 5
title: "Quiz: Lab Threat Hunting Exercise"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam perumusan dokumen pedoman analisis ancaman *(Threat Hunting Playbook)* korporat, mengapa eksistensi skenario perancangan dugaan, yakni formulasi parameter *Hipotesis (Hypothesis)*, dipandang krusial?
- [x] A. Penyusunan Hipotesis memberikan gambaran skenario taktis (misalnya "Mendeteksi kemungkinan peretas menggunakan eksploitasi persistensi manipulasi *Scheduled Tasks* Windows"). Tanpa penyusunan parameter awal ini, rutinitas tim SOC sekadar mencari indikasi data tanpa kerangka yang terarah secara, menyebabkan efisiensi analisis berkurang secara dramatis.
- [ ] B. Karena struktur Hipotesis adalah modul integrasi algoritma wajib untuk menyalakan mesin data terpusat *Splunk*.
- [ ] C. Lantaran Hipotesis spesifik ditujukan sebagai format instalasi *file backup* ekosistem sistem berekstensi `.E01`.
- [ ] D. Komponen Hipotesis sebatas difokuskan sebagai instruksi simulasi peretasan arsitektur ofensif (*Red Team Operations*).

### Q2
**Type:** True/False
**Question:** Dalam mendayagunakan platform referensi analisis keamanan intelijen *Playbook*, filter kueri inspeksi perburuan sistem peladen Windows *EventCode 4698* diintegrasikan sebagai fungsi algoritma pendeteksi (Indikasi manipulasi tugas *Scheduled Task*) yang penataannya berkesesuaian pengujian skenario parameter arsitektur *MITRE ATT&CK* pada ID Taktik operasi T1053.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat mengeksekusi kueri SIEM Splunk, perintah `table _time, ComputerName, Task_Name` disisipkan pada kueri tersebut untuk menampilkan keluaran log dari format mentah menjadi format visual apa?
**Answer:** Menampilkannya sebagai tabel terstruktur (dengan kolom: Waktu, Komputer, dan Nama Tugas).

### Q4
**Type:** Short Answer
**Question:** Ketika staf *SOC* memformulasikan pedoman *Threat Hunting Playbook* untuk skenario *Scheduled Task*, standar referensi intelijen ancaman global apakah yang dirujuk guna memetakan klasifikasi taktik tersebut (Berawalan kata "MITRE")?
**Answer:** MITRE ATT&CK Framework.

### Q5
**Type:** Short Answer
**Question:** Di modul dokumen *Playbook*, apabila tim keamanan merekomendasikan instruksi: "Jika indikasi insiden terkonfirmasi positif (*True Positive*), segera lakukan isolasi dengan mencabut kabel jaringan *Ethernet*", arahan teknis mitigasi ini merujuk pada fase apa dalam kerangka respons insiden PICERL?
**Answer:** Fase Containment (Penahanan/Isolasi Jaringan).
