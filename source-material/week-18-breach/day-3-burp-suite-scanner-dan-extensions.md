# 💀 Week 18 · Day 3: Burp Suite Scanner & Extensions

> **Rank**: BREACH | **Minggu ke-18**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 18 · Day 3/5 | BREACH Rank (Minggu 4 dari 5) | Overall: 88/120 hari (73%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** fitur pemindaian kerentanan web otomatis (Burp Scanner).
2. **Membedakan** batasan fitur antara lisensi versi *Community* dan *Professional*.
3. **Menerapkan** instalasi *plugin* tambahan melalui *BApp Store* untuk memperluas kapabilitas Burp Suite.

---

## 📖 Materi Inti

### Kemudahan Otomatisasi: Burp Scanner (Professional Edition)

Jika *Repeater* dan *Intruder* ditujukan untuk pengujian semi-manual, *PortSwigger* menyediakan senjata pamungkas untuk otomatisasi penuh: **Burp Scanner**.
*Scanner* ini mampu memindai (*Crawl & Audit*) situs web secara keseluruhan dari ujung ke ujung, dan secara otomatis menghasilkan laporan seperti: *"Terdapat SQLi di URL A, XSS di URL B, dan CSRF di URL C"*.

**Kendala Lisensi:** Sayangnya, fitur *Scanner* otomatis ini hanya tersedia di versi berbayar, yaitu *Burp Suite Professional* (dengan harga langganan [sekitar $449/tahun](https://portswigger.net/burp/pro/pricing)).
Pada versi *Community Edition* yang dapat diunduh gratis, fitur tab *Dashboard Scanner* dinonaktifkan (berwarna abu-abu/dikunci). 

Namun, jangan khawatir! Seorang *Bug Hunter* dan pentester yang hebat tidak selalu bergantung pada pemindai otomatis. Keterampilan pengujian manual menggunakan *Repeater* sering kali lebih akurat dan mampu menemukan celah logika (*Logic Flaws*) yang tidak bisa dideteksi oleh *Scanner*.

### Bursa Ekstensi: BApp Store (Extensions)

Sama seperti editor teks *VS Code* yang memiliki *Extensions*, *Burp Suite* juga dibekali dengan sarana modifikasi pihak ketiga bernama **BApp Store (Burp App Store)**.

Komunitas keamanan siber di seluruh dunia mengembangkan berbagai *plugin* (menggunakan Python atau Java) dan merilisnya secara gratis di BApp Store untuk menambah kekuatan Burp Suite. (Catatan: Kamu membutuhkan instalasi lingkungan *Jython* jika ingin mengunduh plugin berbasis Python).

**Ekstensi Andalan:**
1. **Autorize:** Sangat populer untuk pengujian kerentanan *IDOR* (Insecure Direct Object Reference) dan *Broken Access Control*. Ekstensi ini otomatis mengirimkan setiap permintaan HTTP ulang (*replay*) menggunakan token sesi berhak akses rendah di latar belakang, sangat memudahkan pencarian celah otorisasi secara massal.
2. **Logger++:** Papan catatan (Log) terperinci yang merekam seluruh riwayat aktivitas *HTTP* secara menyeluruh (jauh lebih detail dari fitur *HTTP History* bawaan).
3. **Turbo Intruder:** Skrip otomatisasi tingkat lanjut yang melontarkan ribuan kueri jauh lebih cepat daripada *Intruder* bawaan Burp Suite. Sangat berguna untuk *Brute Force* dengan performa tinggi.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Ayo mencoba memasang ekstensi dari *BApp Store*!

1. Buka aplikasi *Burp Suite Community Edition*.
2. Arahkan kursor ke tab **Extender -> BApp Store**. (Pada versi terbaru, mungkin bernama **Extensions -> BApp Store**).
3. Di layar tersebut, kamu akan disuguhi ratusan *plugin* yang tersedia secara gratis.
4. Cari ekstensi bernama **"Logger++"**. Klik ekstensi tersebut lalu tekan tombol **Install** di panel bawah.
5. Setelah terinstal, tab baru bernama *Logger++* akan muncul di deretan menu navigasi atas Burp. Buka tab tersebut.
6. Mulai saat ini, *Logger++* akan mencatat dan merekam setiap detail paket data HTTP yang keluar-masuk dari Burp-mu seperti mesin log abadi.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Fitur utama apa untuk pemindaian kerentanan otomatis (*Crawl & Audit*) yang dikunci pada lisensi <i>Burp Suite Community Edition</i>?</summary>

**Jawaban:** Fitur *Burp Scanner* (Vulnerability Scanner Otomatis).
</details>

<details>
<summary>❓ Tab manakah yang harus dituju jika seorang pentester ingin mengunduh dan memasang <i>plugin</i> tambahan (*Extensions*) buatan komunitas pada Burp Suite?</summary>

**Jawaban:** Tab *BApp Store* (biasanya di dalam tab *Extender* atau *Extensions*).
</details>

<details>
<summary>❓ Ekstensi populer manakah dari BApp Store yang sering digunakan untuk mendeteksi kerentanan <i>IDOR / Broken Access Control</i> secara otomatis di latar belakang?</summary>

**Jawaban:** Autorize.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami fungsi dari *Burp Scanner* pada versi *Professional*.
- [ ] Saya mengerti perbedaan fitur utama antara lisensi *Community* dan *Professional*.
- [ ] Saya berhasil menemukan dan melakukan instalasi ekstensi dari *BApp Store*.
- [ ] Saya mengetahui kegunaan ekstensi *Autorize* dan *Logger++*.
- [ ] Saya telah menjawab seluruh *Quiz Kilat* dengan benar.

---

## 🔗 Resources

- [PortSwigger BApp Store Directory](https://portswigger.net/bappstore) — Galeri resmi direktori ekstensi *plugin* Burp Suite.

---

## ➡️ Besok

**Day 4: Other Tools (ZAP, ffuf, nikto)** — Karena *Burp Scanner* versi *Community* dikunci, apakah kita tidak bisa menggunakan pemindai otomatis sama sekali? Tentu saja bisa! Besok, kita akan beralih ke alat pengujian alternatif *Open Source* yang 100% gratis. Kita akan berkenalan dengan **OWASP ZAP** (Pemindai Web Otomatis Gratis!), pemindai kerentanan web legendaris **Nikto**, dan aplikasi *Fuzzing* andalan masa kini: **ffuf**!

---

*📅 TISS Null Teaming · Week 18 · Day 3 · BREACH Rank*
