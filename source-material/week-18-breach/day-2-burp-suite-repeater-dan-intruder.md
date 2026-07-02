# 💀 Week 18 · Day 2: Burp Suite Repeater & Intruder

> **Rank**: BREACH | **Minggu ke-18**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 18 · Day 2/5 | BREACH Rank (Minggu 4 dari 5) | Overall: 87/120 hari (72%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengeksploitasi** secara manual berulang-ulang tanpa memuat rendering *Browser* (*Repeater*).
2. **Merakit** otomatis penembak tebakan sandi (*Intruder*).
3. **Mendemonstrasikan** pemasangan penetapan koordinat sasaran tebak (*Payload Positions*).

---

## 📖 Materi Inti

### Repeater: Eksekutor Manual

Ketika Anda mencegat (*Intercept*) kueri formulir *Login* dan ingin mengetes 10 variasi kutip injeksi *SQL Injection*, apakah Anda harus mencegat -> forward -> reload browser -> ketik ulang form -> cegat lagi?
Siklus tersebut membuang umur operasional!

Di arsitektur *Burp Suite*, Anda cukup mencegat kueri SATU KALI, lalu klik kanan lantas pilih **"Send to Repeater (Ctrl+R)"** .
Di dalam tab **Repeater**, Anda bebas mengubah-ubah kueri sesuka hati, lalu mengeklik tombol *Send*, dan seketika Server membalas di layar sebelah kanan (*Response*) tanpa kamu perlu menyentuh antarmuka *Browser* sama sekali!

Repeater adalah surga bagi penganalisis peretas yang ingin mendelegasikan bereksperimen mencoba eksploitasi *XSS, IDOR, SQLi* baris demi baris secara meraba, lantas mengamati ralat respons dengan ketelitian presisi.

### Intruder: Otomasi Eksploitasi

Bila *Repeater* adalah manual, maka **Burp Intruder** (Ctrl+I) adalah arsitektur alat otomatis *Brute Force* yang mendelegasikan pengiriman jutaan payload secara buta otomatis!

Digunakan untuk : *Brute Force Sandi, Meraba iteratif IDOR (dari rentang ID 1 sampai 10.000), Pencarian iterasi Fuzzing URL *.

**Anatomi Arsitektural Intruder:**
1. **Positions (Sasaran Koordinat Tembak):** Anda mencegat paket kueri `password=admin`. Anda memblok parameter kata "admin", lalu menandai *Add §*. Jadinya `password=§admin§`. Tanda `§` adalah penanda titik lokasi pengiriman kamus!
2. **Payloads (Payload ):** Di sinilah Anda menuangkan seember daftar kata sandi bocor (*Wordlists*) semacam arsip *rockyou.txt*. 
3. Tekan **Start Attack!** Burp akan mengirimkan kata pertama, mencatat respon, mengirimkan kata kedua, dst! pentester tinggal mendelegasikan pencarian serangan mana yang menghasilkan status *302 Redirect* atau memiliki ukuran panjang (*Length*) yang paling berbeda dari rincian lainnya .

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Ayo rakit target serangan *Burp Intruder* !

1. Nyalakan tab *Proxy*, lantas *Intercept* sembarang formulir laman *Login* di mesin uji . (Atau *Login* TryHackMe).
2. Temukan bodi `username=hacker&password=123`.
3. Klik kanan -> **Send to Intruder**. Buka tab *Intruder*.
4. Di tab *Positions*, bersihkan sasaran (tombol Clear §), lalu blok parameter angka `123`, dan klik **Add §**. targetmu terpusat di sandi!
5. Pindah ke tab *Payloads*. Ketikkan manual 5 sandi `rahasia`, `qwerty`, `password`, `123`, `admin`.
6. Klik tombol **Start Attack**. Layar jendela pengujian muncul mengirimkan 5 serangan beruntun.
7. Tatap kolom *Length* (Ukuran Balasan). Amati apakah ada 1 payload yang ukurannya membesar atau statusnya melesat menjadi `302`? Jika iya, itu sandi yang valid sukses masuk !

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membuka pemicu manual , apakah julukan tab di Burp Suite yang memampukan pentester memanipulasi seraya mengirimkan satu <i>Request</i> berulang-ulang tanpa henti (tanpa butuh pemanggilan <i>Browser</i>)?</summary>

**Jawaban:** Tab *Repeater* .
</details>

<details>
<summary>❓ Ketika meluncurkan serangan eksploitasi otomasi <i>Burp Intruder</i>, sepasang simbol apakah (`§...§`) yang digunakan sensor demi menandai menetapkan letak titik sasaran Payload?</summary>

**Jawaban:** Simbol penanda (Section Sign) `§` (digunakan membalut parameter `§target§`).
</details>

<details>
<summary>❓ Ketika penganalisis mengirimkan serangan ribuan kamus <i>Intruder</i> ke halaman *Login*, indikator visual parameter apakah (di tabel hasil *Intruder*) yang lumrah dilirik peretas demi meraba percobaan mana yang terbukti valid/berhasil masuk?</summary>

**Jawaban:** Memilah dan menatap perbedaan angka pada kolom *Length* (panjang response) atau kolom *Status* (misal serangan kode status HTTP dari 200 berubah menjadi 302). yang berhasil lumrahnya mencetak *Length* yang jauh berbeda wujudnya.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap dominasi serangan presisi manual *Repeater*
- [ ] Saya fasih merangkai letak target `§` di fitur *Intruder*
- [ ] Saya cakap menuangkan payload payload daftar *Payloads*
- [ ] Saya paham memilah rentetan serangan hasil *Brute Force*
- [ ] Saya telah menjawab seluruh ulasan *quiz kilat* 
---

## 🔗 Resources

- [PortSwigger Burp Intruder Docs](https://portswigger.net/burp/documentation/desktop/tools/intruder) — Kumpulan referensi taktik menyasar IP payload sandi *Intruder* .

---

## ➡️ Besok

**Day 3: Burp Suite Scanner & Extensions** — Lelah menatap layar *Repeater* menembak eksploitasi *XSS* manual? Esok harinya, rasakan kemewahan versi korporat! Kenalkan pelacak otomatis **Burp Scanner**, yang mampu membabat seluruh kerentanan situs sambil kamu tidur! Serta pelajari pemasangan *Extensions / BApp Store* (Plugin) untuk mengubah Burp-mu menjadi pisau Swiss Army insiden sejati !

---

*📅 TISS Null Teaming · Week 18 · Day 2 · BREACH Rank*
