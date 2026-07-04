---
type: quiz
week: 17
day: 1
title: "Quiz: XSS (Payload Crafting & Cookie Stealing)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa *Payload Crafting* dinilai jauh lebih berbahaya daripada sekadar memunculkan peringatan `alert(1)` pada celah XSS?
- [ ] A. *Payload Crafting* didesain khusus untuk mengekstrak isi *database* menggunakan SQL Injection.
- [x] B. Pada *Payload Crafting*, penyerang merakit *JavaScript* khusus yang bertujuan untuk tindakan eksploitatif yang nyata, seperti merampas *Session Cookie* Admin atau menyadap pengetikan papan ketik korban (*Keylogging*), bukan sekadar memunculkan *pop-up*.
- [ ] C. *Payload* tersebut mengizinkan penyerang untuk meledakkan serangan *DDoS*.
- [ ] D. Skrip *Payload* secara spesifik ditugaskan meretas *Wappalyzer*.

### Q2
**Type:** True/False
**Question:** Saat merangkai skrip penyadap tombol (*XSS Keylogger*), penyerang harus menggunakan fitur *Event Listener* pada JavaScript (misalnya mendeteksi aktivitas `keypress`) untuk mengawasi dan merekam ketikan korban.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada eksploitasi perampasan *Cookie*, properti JavaScript bawaan apa (yang berawalan `document.`) yang dieksploitasi oleh penyerang untuk menyedot nilai sesi otentikasi korban?
**Answer:** document.cookie

### Q4
**Type:** Short Answer
**Question:** Jika perlindungan sistem (*WAF*) memblokir dan melarang penggunaan tag `<script>`, elemen *HTML* apa yang sering digunakan penyerang sebagai inang penyamaran (biasanya dipadukan dengan *event handler* `onerror=`) untuk mengeksekusi XSS?
**Answer:** <img> (atau tag img).

### Q5
**Type:** Short Answer
**Question:** Pada eksploitasi pencurian *Cookie*, setelah *JavaScript* berhasil menyedot *Cookie* dari browser korban, ke mana skrip tersebut harus mengirimkan (mentransmisikan) *Cookie* itu agar bisa digunakan oleh penyerang?
**Answer:** Ke server penampung atau *Webhook* milik penyerang.
