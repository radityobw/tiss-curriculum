---
type: quiz
week: 9
day: 4
title: "Quiz: Menjadwalkan Tugas (Cron Jobs)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Jika sebuah server menampung aturan penjadwalan *cron job* dengan format `* * * * * /tmp/script.sh`, bagaimanakah frekuensi eksekusi dari skrip tersebut?
- [x] A. Skrip tersebut akan dieksekusi secara otomatis dan berulang kali setiap satu menit secara terus-menerus.
- [ ] B. Skrip hanya akan dieksekusi 5 kali seumur hidup di server tersebut.
- [ ] C. Komputer bakal menghentikan eksekusi skrip selama 5 tahun lamanya demi keamanan.
- [ ] D. Skrip dijadwalkan secara kondisional ketika beban server rendah.

### Q2
**Type:** True/False
**Question:** Saat mendefinisikan letak tugas di file `crontab`, disarankan untuk menggunakan lintasan rute relatif (*relative path*) seperti `./script.sh` saja, karena program jadwal *Cron* selalu mengetahui posisi *current directory* dari profil pengguna aktif.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Tuliskan format sandi penjadwalan *Cron* (*Cron Expression* 5 bintang) jika sebuah rutin pengelolaan harus dieksekusi secara otomatis setiap hari Minggu tepat pada pukul 04:00 dini hari!
**Answer:** `0 4 * * 0`

### Q4
**Type:** Short Answer
**Question:** Opsi atau parameter khusus (*flag*) apakah yang diselipkan pada perintah `crontab` jika administrator hanya ingin sekadar melihat (me-list) daftar jadwal *cron jobs* saat ini tanpa membuka mode editor?
**Answer:** `crontab -l` (Huruf l untuk *List*).

### Q5
**Type:** Short Answer
**Question:** Jika diurutkan secara sekuensial pada kerangka konfigurasi pola *Cron* (Bintang ke-1 mewakili Menit, ke-2 mewakili Jam), parameter waktu apakah yang diwakili oleh lambang bintang urutan ketiga dan keempat?
**Answer:** Tanggal (*Day of the month*) dan Bulan (*Month*).
