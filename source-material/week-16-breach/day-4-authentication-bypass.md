# 💀 Week 16 · Day 4: Authentication Bypass

> **Rank**: BREACH | **Minggu ke-16**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 16 · Day 4/5 | BREACH Rank (Minggu 2 dari 5) | Overall: 79/120 hari (66%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** serangan ekstraksi *SQLi* dengan serangan penelikungan autentikasi (*Authentication Bypass*).
2. **Mensimulasikan** taktik serangan tebakan *password* (*Brute Force* & *Credential Stuffing*).
3. **Mengeksploitasi** kelalaian logika pemrograman dalam manajemen *Session* pengguna.

---

## 📖 Materi Inti

### Mendobrak Gerbang Tanpa SQL Injection (Auth Bypass)

Meskipun kerentanan *SQL Injection* pada target telah diperbaiki (misalnya menggunakan *Parameterized Queries*), keamanan aplikasi belum terjamin seratus persen. Kelalaian logika dalam menyusun fitur keamanan **Otentikasi (Authentication)** sering kali menjadi celah eksploitasi yang sama fatalnya.

*Authentication Bypass* (Bypass Otentikasi) adalah kondisi di mana penyerang berhasil masuk ke akun pengguna (atau bahkan mengambil alih otoritas Administrator) tanpa mengetahui kredensial (seperti *password*) yang benar. Hal ini dilakukan dengan memanipulasi kelalaian logika pada kode target.

### 1. Serangan Penebakan Sandi (Brute Force & Credential Stuffing)

Jika fitur *Login* aplikasi target **TIDAK MEMILIKI PEMBATASAN KECEPATAN** (*Rate Limiting*) atau sistem *CAPTCHA*, penyerang dapat menggunakan alat otomatisasi (seperti *Hydra* atau *Burp Suite Intruder*) untuk membombardir halaman *Login* dengan ratusan hingga jutaan tebakan kata sandi per detik menggunakan daftar kata sandi umum (*Wordlists* seperti `rockyou.txt`).

- **Brute Force:** Penyerang mencoba meretas 1 nama pengguna (misal: `admin`) dengan mencoba jutaan variasi kata sandi umum secara membabi-buta (contoh: `'123456'`, `'password'`, atau `'admin123'`).
- **Credential Stuffing:** Penyerang menggunakan daftar kombinasi *Email* dan *Password* asli yang bocor dari peretasan situs web lain di masa lalu (misal: kebocoran data LinkedIn atau Yahoo). Penyerang menggunakan daftar tersebut untuk mencoba *login* ke situs target. Taktik ini sangat berbahaya dan efektif karena mayoritas pengguna sering kali menggunakan kata sandi yang sama persis di berbagai aplikasi yang berbeda!

### 2. Membajak Sesi Pengguna (Session Hijacking & Fixation)

Setelah pengguna berhasil *login*, *server* aplikasi web akan memberikan token sesi (berupa *Session Cookie* atau *JWT*). Selama *browser* pengguna melampirkan *Cookie* tersebut, *server* akan menganggap pengguna sudah *login* dan tidak perlu memasukkan *password* lagi.

Celah keamanan yang sering terjadi pada manajemen sesi:
- **Sesi yang Dapat Diprediksi:** Jika *server* membuat *Session ID* dengan format statis yang mudah ditebak (misal: `session_id=user_1`), penyerang cukup memodifikasi *Cookie* tersebut menjadi `session_id=user_2` untuk mengambil alih akun orang lain!
- **Session Fixation:** Penyerang memancing korban untuk mengklik tautan *login* yang sudah disuntikkan *Cookie Session* buatan penyerang. Ketika korban berhasil *login*, *server* akan mengikat akun korban pada *Cookie* tersebut. Akibatnya, penyerang yang memegang *Cookie* yang sama bisa langsung ikut mengakses akun korban tanpa perlu *login*!

### 3. Celah Logika Pengangkatan Hak (Parameter Tampering)

Terkadang, celah keamanan justru terletak setelah pengguna biasa berhasil *login*!
Penyerang masuk menggunakan akun *User Biasa*, lalu menyisipkan *proxy* (seperti Burp Suite) untuk mencegat (*intercept*) lalu lintas jaringan (*HTTP request*). Penyerang kemudian menemukan parameter peran (seperti `"role":"user"`) dan memodifikasinya secara manual menjadi `"role":"admin"`. 

Jika *server* (bagian *backend*) hanya mempercayai input dari pengguna tanpa melakukan validasi ulang, *server* akan langsung memberikan hak administrator kepada penyerang! Celah manipulasi parameter ini erat kaitannya dengan *Insecure Direct Object Reference (IDOR)* atau *Broken Access Control*.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan serangan *Brute Force* mekanikal di laboratorium!

1. Kunjungi ekosistem lab: [PortSwigger Academy: Authentication](https://portswigger.net/web-security/authentication).
2. Asumsikan kamu menargetkan form *Login* yang tidak memiliki perlindungan *Rate Limiting*.
3. Buka *Burp Suite* (kita akan belajar cara menggunakannya secara mendalam di Minggu 18). Cegat (*Intercept*) *Request Login*, lalu kirimkan ke modul **Burp Intruder**.
4. Tandai parameter kata sandi sebagai area yang akan ditebak: `password=§FUZZ§`
5. Muat daftar kata sandi (*wordlist*) dari *file* teks ke dalam *payload Intruder*. Klik **Start Attack**!
6. Amati hasilnya. Sebagian besar serangan akan menghasilkan kode `HTTP 200 OK` (yang menandakan peringatan "Login Gagal"). Namun, jika kamu melihat satu *request* yang mengembalikan kode `HTTP 302 Found` (Redirect), itu berarti tebakan *password* tersebut berhasil dan kamu berhasil masuk!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar antara taktik <i>Credential Stuffing</i> dibandingkan dengan serangan <i>Brute Force</i> biasa?</summary>

**Jawaban:** Pada *Brute Force*, penyerang menebak *password* secara acak atau menggunakan daftar *password* umum (secara membabi-buta). Sebaliknya, pada *Credential Stuffing*, penyerang menggunakan daftar kombinasi *Email* dan *Password* asli yang bocor dari situs lain, berharap korban menggunakan kata sandi yang sama di situs target.
</details>

<details>
<summary>❓ Apa nama kerentanan di mana penyerang mencegat (*intercept*) HTTP Request dan mengubah nilainya, misalnya dari <code>role=user</code> menjadi <code>role=admin</code>, untuk mendapatkan hak akses yang lebih tinggi?</summary>

**Jawaban:** Parameter Tampering (atau berkaitan dengan ekskalasi hak akses / *Privilege Escalation* / *Broken Access Control*).
</details>

<details>
<summary>❓ Fitur keamanan apa yang tidak diimplementasikan oleh pembuat aplikasi sehingga penyerang bisa mengirimkan ratusan tebakan <i>Brute Force</i> per detik tanpa diblokir?</summary>

**Jawaban:** *Rate Limiting* (Pembatasan kecepatan/jumlah percobaan *login*) atau *CAPTCHA*.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan antara *SQL Injection* dan *Authentication Bypass*.
- [ ] Saya bisa membedakan taktik *Brute Force* dan *Credential Stuffing*.
- [ ] Saya memahami cara kerja eksploitasi manajemen Sesi (*Session Hijacking* & *Session Fixation*).
- [ ] Saya memahami bahaya manipulasi parameter (*Parameter Tampering*).
- [ ] Saya telah membaca ulasan *Quiz Kilat* dengan baik.

---

## 🔗 Resources

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — Panduan penting dari OWASP tentang cara merancang fitur autentikasi (*login*) yang aman dan bebas celah.

---

## ➡️ Besok

**Day 5: Lab & Mission: PortSwigger SQLi Labs** — Kamu telah mempelajari teori ekploitasi *UNION-based SQLi*, *Blind SQLi*, alat otomatisasi *SQLMap*, hingga *Authentication Bypass*. Besok, kamu akan memasuki lab resmi PortSwigger untuk mempraktikkan secara langsung eksploitasi SQLi. Selesaikan lab secara manual tanpa *SQLMap*, dan buatlah dokumen laporan (*Write-up*) sebagai bukti keberhasilan eksploitasimu!

---

*📅 TISS Null Teaming · Week 16 · Day 4 · BREACH Rank*
