---
type: quiz
week: 18
day: 5
title: "Quiz: Lab Full Pentest Machine"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam simulasi peretasan menggunakan *Burp Suite* secara menyeluruh, urutan langkah apa yang paling tepat digunakan untuk melakukan serangan *Brute Force Login* menggunakan kamus kata sandi?
- [x] A. Menyalakan *Intercept is on* di tab *Proxy*; mencegat *Request Login (POST)*; mengeklik kanan dan memilih *Send to Intruder*; menandai parameter kata sandi `§sandi§`; memuat daftar *Wordlist* di tab *Payloads*; lalu menekan tombol *Start Attack*.
- [ ] B. Menyuruh *Repeater* menebak 65ribu *Port* menggunakan *Nmap*.
- [ ] C. Mematikan *Proxy* lalu menggunakan *BApp Store* untuk mengirimkan *SQLMap*.
- [ ] D. Menggunakan ekstensi *Autorize* untuk mencari *XSS* di jendela *Wappalyzer*.

### Q2
**Type:** True/False
**Question:** Dengan menggunakan fitur pengujian manual di tab *Repeater* dalam *Burp Suite*, seorang pentester bisa menguji *payload* seperti injeksi `' OR 1=1 --` berkali-kali tanpa harus berinteraksi atau menekan tombol "Submit" di *Browser* web sama sekali.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada antarmuka *Burp Proxy*, fitur atau tab apakah yang merekam dan menyimpan riwayat seluruh pertukaran lalu-lintas komunikasi *HTTP* yang melewati *Burp*, sehingga pentester bisa melihat jejak pencariannya kembali?
**Answer:** HTTP History.

### Q4
**Type:** Short Answer
**Question:** Ketika seorang *Bug Hunter* menyusun laporan pengujian penetrasi untuk celah yang ditemukan melalui *Burp Suite*, tangkapan layar (*Screenshot*) fitur apa yang biasanya disertakan sebagai *Proof of Concept* (PoC) bukti serangan?
**Answer:** Tangkapan layar tab *Repeater* atau *Intruder* (yang memamerkan *Request injeksi* bersanding dengan *Response* dari server).

### Q5
**Type:** Short Answer
**Question:** Pada penggunaan ekstensi *Autorize*, jenis kerentanan kelalaian hak akses apa yang secara efektif dapat dilacak dan dideteksi secara otomatis di latar belakang oleh ekstensi tersebut?
**Answer:** IDOR (Insecure Direct Object Reference) atau Broken Access Control.
