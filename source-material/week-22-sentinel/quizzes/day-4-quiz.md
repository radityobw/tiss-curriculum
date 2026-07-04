---
type: quiz
week: 22
day: 4
title: "Quiz: IDS/IPS (Suricata & Snort)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan mendasar antara *IDS (Intrusion Detection System)* dan *IPS (Intrusion Prevention System)* dalam memproses muatan lalu lintas data berbahaya?
- [x] A. *IDS* beroperasi sebagai alat pemantau pasif; jika menemukan ancaman, sistem hanya membuat peringatan (*Alert*) tetapi tetap membiarkan data lolos. Sebaliknya, *IPS* beroperasi secara proaktif; jika menemukan ancaman, ia langsung mengeksekusi pemblokiran koneksi (*Drop/Reject*) sehingga serangan gagal masuk ke jaringan internal.
- [ ] B. *IDS* dikhususkan untuk sistem operasi Linux, sementara *IPS* hanya bisa dipasang di *Windows*.
- [ ] C. *IDS* adalah fitur dari SIEM Splunk, sedangkan *IPS* adalah nama lain dari aplikasi *Wireshark*.
- [ ] D. Tidak ada perbedaan, keduanya secara otomatis akan langsung menghapus seluruh jaringan korporat jika diretas.

### Q2
**Type:** True/False
**Question:** Pada konfigurasi aturan (*Rule*) di Suricata/Snort, parameter `content:"<script>";` berfungsi memerintahkan sensor keamanan untuk membongkar dan memeriksa isi muatan data (*Payload*), lalu mencari kecocokan *string* persis berupa `<script>` untuk mendeteksi eksploitasi XSS.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Apa nama *platform* sensor jaringan (*open-source*) modern yang memiliki keunggulan pemrosesan *Multi-threading* dan dianggap sebagai generasi penerus mesin Snort?
**Answer:** Suricata.

### Q4
**Type:** Short Answer
**Question:** Saat membuat satu baris sintaks deteksi (*Rule*) di Snort/Suricata, di posisi manakah parameter tindakan atau *Rule Action* (seperti `alert` atau `drop`) harus diletakkan?
**Answer:** Di posisi terdepan (paling awal dari keseluruhan sintaks).

### Q5
**Type:** Short Answer
**Question:** Pada akhir konfigurasi sintaks aturan pendeteksian di Snort/Suricata, apa kepanjangan dan fungsi dari elemen wajib bernama `sid` (misalnya: `sid:100001;`)?
**Answer:** Signature ID (Sebagai Nomor Identifikasi Unik untuk setiap Aturan yang dibuat).
