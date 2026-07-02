# 📡 Week 9 · Day 4: Cron Jobs (Penjadwalan)

> **Rank**: PACKET | **Minggu ke-9**, Hari 4/5 | **Durasi**: ~35 menit

📊 **Progress**: Week 9 · Day 4/5 | PACKET Rank (Minggu 5 dari 5) | Overall: 44/120 hari (36%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep tugas latar belakang berjadwal (Cron Jobs) di sistem UNIX/Linux
2. **Membaca** dan merancang waktu penjadwalan menggunakan format 5 Bintang Cron (`* * * * *`)
3. **Mengakses** tabel penjadwalan komputermu menggunakan `crontab`

---

## 📖 Materi Inti

### Mesin Waktu Linux: Cron

Bayangkan kamu seorang System Administrator. Kamu punya sebuah *script* (`backup.sh`) yang tugasnya meng-copy database kampus dan menyimpannya di harddisk cadangan agar data tidak hilang.

Tentu saja, kamu tidak mau bangun setiap jam 3 subuh, nyalain laptop, buka terminal, dan mengetik `./backup.sh` setiap hari secara manual. Kamu akan mati muda.

Solusinya adalah **Cron**. 
Cron adalah *daemon* (layanan latar belakang) yang berjalan terus menerus 24 jam sehari, bertugas mengecek jam komputer, lalu menjalankan perintah/script secara otomatis pada waktu yang sudah kamu tentukan.

### Bahasa Bintang (Cron Expression)

Untuk menyuruh Cron bekerja, kamu harus menulis jadwal di sebuah file bernama **Crontab**.
Penu jadwal ini sangat unik, terdiri dari **5 Bintang (Asterisk)** diikuti dengan perintah yang ingin dijalankan.

Formatnya:
```bash
* * * * * /lokasi/script.sh
| | | | |
| | | | +---- Hari dalam seminggu (0-7, di mana 0 dan 7 = Minggu)
| | | +------ Bulan (1-12)
| | +-------- Tanggal dalam bulan (1-31)
| +---------- Jam (0-23)
+------------ Menit (0-59)
```

**Aturan Emas:**
- Tanda bintang `*` artinya: **"Setiap"** (Every).
- Jika ada bintang di posisi menit, artinya: *Setiap menit*.
- Jika ada angka di posisi jam, misal `3`, artinya: *Tepat jam 3*.

### Latihan Membaca Bintang (Super Penting!)

Mari berlatih! Apa arti dari baris crontab di bawah ini?

1. `30 2 * * * /backup.sh`
 *(Artinya: Jalankan backup.sh pada menit ke-30, jam ke-02 subuh, setiap tanggal, setiap bulan, setiap hari. Singkatnya: **Setiap hari jam 02:30 subuh**).*

2. `0 0 1 1 * /ucapan_selamat.sh`
 *(Artinya: Menit 0, Jam 0, Tanggal 1, Bulan 1, Setiap hari. Singkatnya: **Tepat tengah malam pergantian Tahun Baru!**).*

3. `* * * * * /bot_spam.sh`
 *(Artinya: **Berjalan SETIAP MENIT tanpa henti!**).*

**Opsi Lanjut (Garis Miring):**
- Tanda `*/5 * * * *` artinya berjalan setiap interval 5 menit.
- Tanda `0 12 * * 1-5` artinya berjalan jam 12 siang hanya dari hari Senin sampai Jumat (Hari kerja).

### Cara Mengakses Crontab

Untuk mulai membuat jadwal, buka terminal dan ketik:
```bash
$ crontab -e
```
*(Huruf 'e' berarti Edit).*
Pemanggilan pertama kali mungkin akan memintamu memilih teks editor (pilih angka yang sesuai dengan `nano` karena paling mudah). Setelah terbuka, kamu bisa menambahkan jadwal 5 bintangmu di baris paling bawah.

---

## 🧪 Mini Lab (Simulasi Otak)

**Durasi**: ~10 menit

Tantangan Logika!

Bos perusahaan Cloud Computing menyuruhmu membuat penjadwalan Cron untuk script pembersihan sampah sementara server (`/opt/cleaner.sh`).
Bos minta script itu berjalan **Setiap hari Minggu tepat pada jam 04:00 subuh**.

**Tugas:**
Rangkailah format 5 Bintang yang tepat (Menit, Jam, Tanggal, Bulan, Hari) untuk perintah tersebut!
Tulis di buku catatanmu sebelum melihat kunci jawaban.

<details>
<summary>🔑 Kunci Jawaban Simulasi</summary>

Jawabannya adalah:
`0 4 * * 0 /opt/cleaner.sh`

**Penjelasan:**
- Menit ke: **0**
- Jam ke: **4** (subuh)
- Tanggal ke: **\*** (tanggal berapapun tidak peduli, asal...)
- Bulan ke: **\*** (bulan apa pun)
- Hari ke: **0** (0 melambangkan hari Minggu / Sunday).

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Kamu menemukan malware di dalam server yang berjalan otomatis. Saat kamu mengecek daftar crontab hacker (`crontab -l`), tertulis `*/10 * * * * /tmp/virus.sh`. Kapan virus ini dieksekusi oleh sistem?</summary>

**Jawaban:** Virus tersebut dieksekusi secara otomatis setiap interval **10 menit** selama server tersebut hidup. (Simbol `*/10` pada kolom pertama/menit).

</details>

<details>
<summary>❓ Mengapa kita harus menuliskan path lengkap (lokasi absolut) dari script yang ingin dijalankan di crontab, seperti `/home/budi/script.sh` dan bukan sekadar `./script.sh`?</summary>

**Jawaban:** Karena *Cron daemon* berjalan di latar belakang/background sistem, ia "tidak punya lokasi berdiri saat ini" (Current Working Directory). Jika kamu hanya menulis `./script.sh`, Cron akan kebingungan mencarinya di mana. Selalu gunakan lokasi/Absolute Path agar Cron tidak nyasar.

</details>

<details>
<summary>❓ Jika kamu hanya ingin melihat isi jadwal tanpa mengeditnya (agar tidak tidak sengaja terhapus), perintah apa yang digunakan?</summary>

**Jawaban:** Gunakan perintah **`crontab -l`** (huruf L kecil yang berarti *List*).

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami urutan ajaib dari 5 Bintang Cron (Menit, Jam, Tanggal, Bulan, Hari)
- [ ] Saya tahu bahwa bintang tunggal `*` berarti "Setiap"
- [ ] Saya bisa menerjemahkan maksud waktu di sebuah baris Cron
- [ ] Saya mengerti cara membuka tabel penjadwalan dengan `crontab -e`
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Crontab Guru](https://crontab.guru/) — Website wajib yang digunakan oleh *semua* SysAdmin dunia. Ini adalah kalkulator Cron, tinggal masukkan bintang-bintangnya dan web ini akan menerjemahkannya ke bahasa manusia. Sangat membantu agar kamu tidak salah menjadwal!

---

## ➡️ Besok

**Day 5: Lab & Mission: Buat Ping Sweeper & Ujian Kenaikan Rank** — Kita sudah di penghujung jalan RANK PACKET! Kamu akan diuji membuat senjata (script) nyata menggunakan perulangan For Loop, dan memadukan semua ilmu sistem yang sudah kita pelajari bulan ini. Bersiaplah untuk promosi pangkat!

---

*📅 TISS Null Teaming · Week 9 · Day 4 · PACKET Rank*
