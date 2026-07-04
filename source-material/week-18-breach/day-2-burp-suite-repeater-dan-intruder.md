# 💀 Week 18 · Day 2: Burp Suite Repeater & Intruder

> **Rank**: BREACH | **Minggu ke-18**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 18 · Day 2/5 | BREACH Rank (Minggu 4 dari 5) | Overall: 87/120 hari (72%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengeksploitasi** celah keamanan secara manual dan berulang tanpa perlu me-render halaman di *Browser* menggunakan *Repeater*.
2. **Mengotomatisasi** pengujian *payload* secara massal menggunakan *Intruder*.
3. **Mendemonstrasikan** cara menentukan titik serangan (*Payload Positions*) pada sebuah paket *HTTP*.

---

## 📖 Materi Inti

### Repeater: Eksekutor Manual

Ketika kamu mencegat (*Intercept*) kueri formulir *Login* dan ingin menguji 10 variasi *payload SQL Injection*, apakah kamu harus mencegat -> *forward* -> me-reload *browser* -> mengetik ulang form -> dan mencegatnya lagi?
Tentu siklus tersebut sangat membuang waktu!

Di dalam *Burp Suite*, kamu cukup mencegat kueri SATU KALI, lalu klik kanan pada data paket tersebut dan pilih **"Send to Repeater (Ctrl+R)"** .
Di dalam tab **Repeater**, kamu bebas mengubah-ubah kueri (seperti mengganti parameter *username* atau *password*) sesuka hati, lalu mengeklik tombol *Send*. Seketika itu juga, Server akan membalas dan responnya langsung tampil di panel sebelah kanan (*Response*) tanpa kamu perlu membuka antarmuka *Browser* sama sekali!

*Repeater* adalah fitur esensial bagi pentester yang ingin mencoba eksperimen serangan seperti *XSS*, *IDOR*, atau *SQLi* secara bertahap, sambil mengamati respons *server* secara mendetail.

### Intruder: Otomasi Eksploitasi

Jika *Repeater* digunakan untuk pengujian manual, maka **Burp Intruder** (Ctrl+I) adalah alat otomatisasi untuk mengirimkan ribuan modifikasi *payload* dalam waktu singkat!

Intruder sering digunakan untuk: *Brute Force Login, enumerasi parameter (seperti IDOR dari rentang ID 1 sampai 100), dan Fuzzing direktori/URL*.

**Anatomi Penggunaan Intruder:**
1. **Positions (Titik Sasaran):** Setelah mengirim *Request* ke Intruder, kamu akan melihat parameter yang ditandai. Misalnya kueri `password=admin`. Kamu bisa memblok kata "admin", lalu mengeklik tombol *Add §*. Hasilnya menjadi `password=§admin§`. Tanda `§` adalah penanda (marker) posisi di mana *Burp* akan menyuntikkan daftar *payload*-mu!
2. **Payloads (Daftar Input):** Di tab inilah kamu memuat daftar kata/kamus (*Wordlists*) seperti `rockyou.txt` atau kumpulan *payload XSS*. 
3. **Mulai Eksekusi:** Tekan tombol **Start Attack!** Burp akan mengirimkan permintaan dengan *payload* pertama, mencatat responnya, mengirimkan *payload* kedua, dan seterusnya. Pentester tinggal memilah hasil mana yang menunjukkan status *302 Redirect* atau memiliki ukuran balasan (*Length*) yang berbeda secara signifikan dari hasil lainnya.

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Ayo menyimulasikan serangan menggunakan *Burp Intruder*!

1. Aktifkan *Proxy Intercept*, lalu tangkap paket pengiriman dari sebuah formulir *Login* di mesin uji (misalnya di DVWA atau TryHackMe).
2. Temukan baris parameter, contoh: `username=hacker&password=123`.
3. Klik kanan pada paket tersebut -> **Send to Intruder**. Buka tab *Intruder*.
4. Di tab *Positions*, bersihkan semua penanda otomatis (dengan tombol *Clear §*). Kemudian, blok hanya pada angka `123`, dan klik **Add §**. Target seranganmu sekarang terpusat pada kata sandi!
5. Beralih ke tab *Payloads*. Masukkan 5 kata sandi secara manual pada daftar: `rahasia`, `qwerty`, `password`, `123`, `admin`.
6. Klik tombol **Start Attack**. Sebuah jendela baru akan terbuka dan menampilkan pengiriman 5 *request* tersebut secara otomatis.
7. Perhatikan kolom *Length* (Ukuran Respons). Amati apakah ada 1 *payload* yang ukuran responsnya berbeda jauh dari yang lain, atau apakah kolom *Status* berubah menjadi `302`? Jika iya, itu menandakan *payload* tersebut valid dan berhasil *login*!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Tab manakah di Burp Suite yang memungkinkan pentester memodifikasi dan mengirimkan sebuah paket <i>Request</i> berulang kali secara manual tanpa menggunakan browser?</summary>

**Jawaban:** Tab *Repeater*.
</details>

<details>
<summary>❓ Saat menggunakan <i>Burp Intruder</i>, simbol apa yang digunakan untuk menentukan posisi titik suntikan payload di dalam sebuah paket <i>Request</i>?</summary>

**Jawaban:** Simbol penanda seksi atau *Section Sign* (`§`), contohnya `password=§target§`.
</details>

<details>
<summary>❓ Setelah Burp Intruder selesai mengirimkan ribuan serangan, indikator utama apa pada tabel hasil yang digunakan pentester untuk mengidentifikasi keberhasilan serangan?</summary>

**Jawaban:** Kolom *Length* (ukuran *Response*) atau kolom *Status* (misalnya perbedaan status HTTP 200 vs 302/301). *Payload* yang berhasil dieksekusi biasanya menghasilkan angka *Length* atau *Status* yang berbeda dari tebakan yang gagal.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami cara kerja pengujian manual pada *Repeater*.
- [ ] Saya bisa menentukan posisi *payload* menggunakan simbol `§` di tab *Intruder* -> *Positions*.
- [ ] Saya dapat memuat daftar tebakan di tab *Intruder* -> *Payloads*.
- [ ] Saya tahu cara mengidentifikasi serangan yang berhasil dari tabel hasil *Intruder*.
- [ ] Saya telah menjawab seluruh *Quiz Kilat* dengan benar.

---

## 🔗 Resources

- [PortSwigger Burp Intruder Docs](https://portswigger.net/burp/documentation/desktop/tools/intruder) — Dokumentasi resmi panduan lengkap penggunaan *Burp Intruder*.

---

## ➡️ Besok

**Day 3: Burp Suite Scanner & Extensions** — Lelah mencoba *payload* satu per satu? Besok, kita akan membahas alat pelacak otomatis, **Burp Scanner**, yang mampu mendeteksi kerentanan situs secara otomatis (Tersedia di versi Pro). Serta pelajari cara memasang plugin pihak ketiga melalui *BApp Store / Extensions* untuk menambah kesaktian *Burp Suite*-mu!

---

*📅 TISS Null Teaming · Week 18 · Day 2 · BREACH Rank*
