---
type: quiz
week: 20
day: 2
title: "Quiz: Security Events vs Incidents"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di arsitektur analisis keamanan siber, apa batasan definisi yang paling mencerai <i>Security Event</i> dengan <i>Security Incident</i>?
- [ ] A. *Event* adalah serangan, sedangkan *Incident* adalah peringatan alarm.
- [ ] B. *Security Event* pasti menyebabkan kerugian finansial, sedangkan *Security Incident* hanya sebatas log *Apache*.
- [x] C. *Security Event* merupakan setiap kejadian atau observasi aktivitas normal maupun abnormal yang tercatat pada sistem (contoh : *login* sukses). Sedangkan *Security Incident* adalah peristiwa keamanan yang terbukti secara negatif memengaruhi <i>CIA Triad</i> sistem (contoh : kebocoran data) atau melanggar kebijakan keamanan secara nyata.
- [ ] D. *Security Incident* butuh lisensi *Burp Suite Professional*.

### Q2
**Type:** True/False
**Question:** Ketika peranti keamanan siber membunyikan peringatan (peringatan <i>High Severity</i>) namun setelah dilakukan proses Triase (Triage) ternyata penyebabnya adalah rutinitas wajar tim IT korporasi yang sedang memindai kerentanan menggunakan *Nmap*, maka insiden tersebut diklasifikasikan sebagai <i>False Positive</i>.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Di klasifikasi <i>Triage</i>, apa sebutan skenario insiden terburuk bagi Analis SOC ketika sebuah serangan nyata sukses melumpuhkan jaringan namun sistem pertahanan <i>IDS</i> tak mendeteksinya sama sekali dan bungkam tanpa alarm (tidak ada <i>alert</i>)?
**Answer:** False Negative.

### Q4
**Type:** Short Answer
**Question:** Ketika seorang Analis keamanan memilah dan menimbang tingkat prioritas sebuah peringatan (<i>Alert</i>) guna menentukan apakah ia berhadapan dengan <i>False Positive</i> atau <i>True Positive</i>, apa istilah baku dari proses pemilahan tersebut?
**Answer:** Triase (Triage).

### Q5
**Type:** Short Answer
**Question:** Ketika sistem <i>DLP (Data Loss Prevention)</i> membunyikan alarm karena seorang mantan admin diam-diam mengunduh 100GB <i>Database</i> nasabah ke penyimpanan awan miliknya pada jam 2 pagi, dan analis SOC mengonfirmasi bahwa itu adalah pencurian data, klasifikasi triase apakah yang disematkan?
**Answer:** True Positive.
