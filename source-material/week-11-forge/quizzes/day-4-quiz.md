---
type: quiz
week: 11
day: 4
title: "Quiz: Event Handling & Form Validation"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa fungsi utama dari pemanggilan `e.preventDefault()` saat menangani *event submit* pada formulir?
- [ ] A. Memutus koneksi *browser* ke DNS server.
- [ ] B. Mencegah pengiriman *password* ke URL *query string*.
- [x] C. Mencegah sifat bawaan *browser* yang otomatis memuat ulang (*refresh*) halaman, sehingga JavaScript memiliki waktu untuk memproses data formulir di latar belakang.
- [ ] D. Mematikan semua *Event Listener* pada tombol lain di halaman.

### Q2
**Type:** True/False
**Question:** Properti `.value` (misalnya pada `inputSandi.value`) digunakan untuk mengambil teks atau data yang telah diketikkan pengguna ke dalam elemen *input* formulir HTML.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Objek bawaan apa (sering disingkat sebagai parameter `e`) yang secara otomatis diberikan kepada fungsi *Event Listener* dan berisi detail informasi mengenai kejadian yang baru saja terjadi (seperti koordinat klik atau tombol yang ditekan)?
**Answer:** Event.

### Q4
**Type:** Short Answer
**Question:** Fungsi bawaan JavaScript apa yang digunakan untuk mendaftarkan pendengar kejadian (*Event Listener*) pada sebuah elemen, agar dapat mendeteksi interaksi pengguna (seperti klik atau ketikan)?
**Answer:** addEventListener.

### Q5
**Type:** Short Answer
**Question:** Apa nama *event* (kejadian) yang secara spesifik dipicu ketika sebuah elemen `<form>` mencoba mengirimkan datanya (misal karena pengguna menekan Enter atau klik tombol Submit)?
**Answer:** submit.
