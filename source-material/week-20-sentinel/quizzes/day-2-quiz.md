---
type: quiz
week: 20
day: 2
title: "Quiz: Security Events vs Incidents"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di ranah analisis keamanan siber, apa batasan operasional yang paling membedakan antara *Security Event* dengan *Security Incident*?
- [ ] A. *Event* adalah serangan, sedangkan *Incident* adalah peringatan alarm.
- [ ] B. *Security Event* selalu menyebabkan kerugian finansial, sedangkan *Security Incident* hanya sebatas pencatatan log *Apache*.
- [x] C. *Security Event* adalah setiap kejadian (normal maupun abnormal) yang tercatat pada sistem (contoh: *login* sukses). Sedangkan *Security Incident* adalah peristiwa keamanan yang terkonfirmasi berdampak negatif terhadap elemen keamanan *CIA Triad* sistem (contoh: kebocoran data) atau melanggar kebijakan keamanan secara nyata.
- [ ] D. *Security Incident* memerlukan lisensi perangkat lunak khusus.

### Q2
**Type:** True/False
**Question:** Ketika sensor keamanan membunyikan peringatan (*High Severity Alert*), namun setelah diinvestigasi (Triase) ternyata pemicunya adalah aktivitas wajar dari tim IT yang sedang melakukan pemindaian kerentanan terjadwal, maka peringatan tersebut diklasifikasikan sebagai *False Positive*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Dalam klasifikasi *Triage*, apa sebutan untuk skenario terburuk di mana sebuah serangan peretasan benar-benar berhasil menyusup, tetapi sistem pertahanan/sensor gagal mendeteksinya dan tidak memicu peringatan (*alert*) sama sekali?
**Answer:** False Negative.

### Q4
**Type:** Short Answer
**Question:** Ketika seorang Analis SOC meninjau peringatan (*Alert*) baru dari sistem, memvalidasinya, dan menentukan prioritas untuk memastikan apakah itu *False Positive* atau *True Positive*, apa istilah teknis dari proses penyaringan awal ini?
**Answer:** Triase (Triage).

### Q5
**Type:** Short Answer
**Question:** Ketika sistem *DLP (Data Loss Prevention)* mendeteksi dan memperingatkan bahwa seorang staf mengunduh 100GB *Database* nasabah ke penyimpanan awan pribadinya pada pukul 2 pagi, dan analis SOC mengonfirmasi hal tersebut sebagai pencurian data aktual, klasifikasi apakah yang disematkan pada peringatan tersebut?
**Answer:** True Positive.
