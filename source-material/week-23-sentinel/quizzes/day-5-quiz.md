---
type: quiz
week: 23
day: 5
title: "Quiz: Lab Threat Hunting Exercise"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam pembuatan pedoman *Threat Hunting Playbook*, mengapa merumuskan dugaan atau *Hipotesis (Hypothesis)* di awal sangatlah krusial?
- [x] A. Hipotesis memberikan gambaran skenario ancaman yang jelas (misal: "Mendeteksi peretas yang mempertahankan akses menggunakan *Scheduled Tasks*"). Tanpa hipotesis yang terarah, analis SOC hanya akan membuang waktu mencari log secara acak tanpa tujuan yang jelas.
- [ ] B. Karena struktur Hipotesis diperlukan sebagai perintah wajib untuk menyalakan *server Splunk*.
- [ ] C. Karena Hipotesis adalah format penyimpanan *file backup* forensik yang berekstensi `.E01`.
- [ ] D. Komponen Hipotesis sebatas difokuskan sebagai instruksi simulasi peretasan sistem.

### Q2
**Type:** True/False
**Question:** Dalam penyusunan pedoman *Threat Hunting Playbook* untuk skenario "Pembuatan tugas otomatis oleh peretas", pencarian log Windows spesifik pada *Event ID 4698* memiliki korelasi langsung dengan pemetaan taktik *MITRE ATT&CK* pada ID T1053 (Scheduled Task/Job).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat merangkai kueri pencarian di Splunk, tambahan perintah `table _time, ComputerName, Task_Name` digunakan untuk mengubah format data mentah (*raw log*) menjadi tampilan visual berbentuk apa?
**Answer:** Menampilkannya dalam bentuk tabel terstruktur (yang berisi kolom: Waktu, Nama Komputer, dan Nama Tugas).

### Q4
**Type:** Short Answer
**Question:** Saat Analis SOC menyusun taktik mitigasi di dalam *Threat Hunting Playbook*, standar ensiklopedia ancaman siber global manakah yang sering digunakan sebagai rujukan untuk mengidentifikasi perilaku serangan peretas (Berawalan kata "MITRE")?
**Answer:** MITRE ATT&CK Framework.

### Q5
**Type:** Short Answer
**Question:** Jika di dalam dokumen *Playbook* direkomendasikan tindakan: "Jika ancaman terbukti valid, segera lakukan isolasi dengan mencabut kabel jaringan *Ethernet*", tindakan mengisolasi komputer dari jaringan ini masuk ke dalam fase apa dalam standar penanganan insiden (*Incident Response*)?
**Answer:** Fase Containment (Penahanan / Isolasi Jaringan).
