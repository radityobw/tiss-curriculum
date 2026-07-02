---
type: quiz
week: 21
day: 2
title: "Quiz: Windows Event Logs"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Menakar arsitektur infrastruktur rekam jejak di lingkungan korporasi , kategori log utama manakah di dalam aplikasi *Windows Event Viewer* yang senantiasa dipantau oleh Analis SOC lantaran log tersebut merekam pergerakan masuk (Login) dan penggunaan hak akses sistem?
- [ ] A. *Application* Logs.
- [ ] B. *System* Logs.
- [x] C. *Security* Logs.
- [ ] D. *Setup* Logs.

### Q2
**Type:** True/False
**Question:** Pada pemantauan *Windows Event ID*, kemunculan beruntun rentetan sandi insiden angka *ID 4625* yang terjadi dalam hitungan milidetik secara berulang mengindikasikan terjadinya serangan *Brute Force* (Penebakan Sandi), lantaran ID tersebut mencatat status <i>Logon Failed</i>.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat Analis keamanan menelaah rentetan *Security Logs* Windows, sandi <i>Event ID</i> nomor berapakah yang senantiasa memberikan pertanda bahwa proses <i>Logon Success</i> (Tamu atau Peretas sukses membobol sandi dan masuk) baru saja terjadi?
**Answer:** Event ID 4624.

### Q4
**Type:** Short Answer
**Question:** Saat penganalisis menganalisis *Event Viewer* dan mendapati kode <i>Event ID 7045</i>, instalasi komponen parasit jenis apakah yang disiarkan sandi insiden ini (biasanya digunakan peretas menancapkan *Backdoor* permanen)?
**Answer:** New Service Installed (Instalasi Layanan Baru / Service).

### Q5
**Type:** Short Answer
**Question:** Di ranah pengujian investigasi sistem operasi Windows, apa akronim nama aplikasi grafis (*GUI*) bawaan Windows yang menjadi ruang kendali sentral bagi *Blue Team* untuk mengekstrak dan menatap ribuan log (berformat `.evtx`)?
**Answer:** Event Viewer.
