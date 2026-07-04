---
type: quiz
week: 17
day: 5
title: "Quiz: Lab PortSwigger XSS/CSRF"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Saat menyimulasikan eksploitasi pencurian *Cookie* melalui *XSS*, atribut JavaScript apa yang diakses dan dikirimkan oleh skrip penyerang untuk merampas nilai sesi autentikasi korban?
- [x] A. Atribut `document.cookie`.
- [ ] B. Fungsi `window.localStorage.clear()`.
- [ ] C. Fungsi `document.write()`.
- [ ] D. Fungsi `alert(1)`.

### Q2
**Type:** True/False
**Question:** Dalam serangan *CSRF*, penyerang menipu *browser* korban agar mengirimkan permintaan (contoh: transfer dana atau ganti email) ke *server* target tanpa disadari oleh korban, dengan memanfaatkan *Cookie* otorisasi korban yang masih aktif (*Login*).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada eksploitasi *File Upload*, ketika penyerang menyisipkan karakter `%00` pada akhiran file seperti `shell.php%00.jpg` untuk memotong pembacaan ekstensi oleh server, apa nama teknik bypass ini?
**Answer:** Null Byte Injection (atau Null Byte Bypass).

### Q4
**Type:** Short Answer
**Question:** Apa sebutan untuk dokumen atau catatan referensi ringkas yang berisi daftar *Payload XSS/CSRF* siap pakai yang biasa digunakan oleh *Bug Hunter* profesional agar tidak perlu mengetik ulang dari awal?
**Answer:** Cheat Sheet (atau Payload Cheatsheet).

### Q5
**Type:** Short Answer
**Question:** Pada serangan manipulasi *SSRF*, alamat IP `169.254.169.254` sering dibidik untuk mengekstrak kredensial *Metadata* dari *server* yang berjalan di lingkungan infrastruktur apa?
**Answer:** Cloud (Amazon Web Services / AWS, GCP, Azure, dsb).
