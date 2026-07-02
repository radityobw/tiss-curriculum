# 💀 Week 17 · Day 2: CSRF & SSRF (State-Changing Attacks)

> **Rank**: BREACH | **Minggu ke-17**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 17 · Day 2/5 | BREACH Rank (Minggu 3 dari 5) | Overall: 82/120 hari (69%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** konsep serangan antara *Cross-Site Request Forgery (CSRF)* dan *Server-Side Request Forgery (SSRF)*.
2. **Mensimulasikan** eksploitasi pemalsuan permintaan dari sisi klien (*CSRF*).
3. **Mengeksekusi** pengintaian infrastruktur internal dengan memanipulasi peladen backend (*SSRF*).

---

## 📖 Materi Inti

### CSRF: Menyetir Peramban Pengguna Jarak Jauh

Bayangkan Anda menemukan kerentanan pada sebuah platform, tetapi peladen tersebut telah mengimplementasikan proteksi *HttpOnly* pada *Cookie* otentikasi. Akibatnya, eksploitasi *XSS* tidak lagi mampu mencuri *Cookie* pengguna. Kendala ini tidak menghentikan serangan! Seorang pentester tidak wajib mencuri sesi (cookie) untuk mengeksploitasi sistem; ia cukup memaksa **peramban korban untuk mengeksekusi perintah** tepat saat korban sedang masuk (*login*) di situs tersebut.

Taktik eksploitasi ini dikenal sebagai **CSRF (Cross-Site Request Forgery)**. Kerentanan ini terjadi ketika server hanya mengecek *"Apakah pengguna ini sudah login?"*, tetapi gagal memvalidasi *"Apakah permintaan (request) ini BENAR-BENAR dilakukan dengan sengaja oleh pengguna tersebut?"*.

**Skenario Eksploitasi CSRF:**
1. Korban sedang dalam kondisi otentikasi aktif (*Login*) di `bank.com`.
2. Melalui rekayasa sosial, korban dibujuk untuk mengeklik tautan dari pentester: `http://hacker.com/kucing-lucu.html`.
3. Di dalam dokumen *HTML* "kucing lucu" tersebut, pentester telah menyisipkan skrip tersembunyi:
   ```html
   <form action="http://bank.com/transfer" method="POST">
    <input type="hidden" name="tujuan" value="rekening-hacker">
    <input type="hidden" name="jumlah" value="1000000">
   </form>
   <script> document.forms[0].submit(); </script>
   ```
4. Karena peramban korban secara otomatis mengirimkan *Request* form tersebut sementara *Cookie* otentikasinya masih menempel (aktif), peladen `bank.com` mengira bahwa permintaan tersebut sah. Dana berhasil ditransfer tanpa izin hanya dengan satu klik pada tautan jebakan!

*Mitigasi (Blue Team)*: Pengembang web wajib mengimplementasikan proteksi **CSRF Token** (sandi acak sekali-pakai) di setiap formulir web yang mengubah data.

### SSRF: Menipu Peladen Menyerang Lingkungannya Sendiri

Bila *CSRF* berfokus menipu *Browser* pengguna untuk menyerang peladen...
Maka **SSRF (Server-Side Request Forgery)** berfokus menipu *Server Backend* target agar server tersebut secara otomatis menyerang server lain di jaringan internalnya sendiri (yang seharusnya tidak dapat diakses dari luar)!

Seringkali, server *Backend* memiliki fitur untuk mengunduh gambar atau data dari peladen luar, misal:
`http://target.com/unduh?url=https://github.com/logo.png`

Pentester dapat memodifikasi parameter URL tersebut untuk merujuk ke alamat IP internal peladen tertutup (seperti localhost):
`http://target.com/unduh?url=http://127.0.0.1/admin-rahasia`

*Seketika!* Server aplikasi `target.com` dengan polosnya akan mengeksekusi kueri pemanggilan ke antarmuka admin lokalnya sendiri (yang diblokir dari interaksi internet luar), lalu secara sukarela menyerahkan seluruh respons halaman rahasia itu kepada pentester! (Kerentanan SSRF sangat terkenal digunakan untuk merampas kredensial *AWS Metadata* dengan merujuk alamat IP `169.254.169.254`).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merakit skrip pemaksaan permintaan (*CSRF Payload*)!

1. Kunjungi fasilitas eksperimen web rentan (seperti lab *PortSwigger CSRF*).
2. Temukan fitur formulir ganti *email* yang teridentifikasi tidak dilindungi oleh *CSRF Token*.
3. Fitur web tersebut mengeksekusi perubahan email via rute: `/my-account/change-email` dengan metode HTTP *POST*.
4. Racik dokumen *HTML* fiktif di sisi Anda:
   ```html
   <form id="bajak" action="https://vulnerable.com/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="hacker@tiss.or.id">
   </form>
   <script> document.getElementById('bajak').submit(); </script>
   ```
5. Saat korban (yang sedang login) mengeklik file *HTML*-mu tersebut, data email miliknya di server web otomatis tertimpa menjadi alamat `hacker@tiss.or.id`. Anda sukses mengambil alih akunnya!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar antara eksploitasi CSRF dan SSRF?</summary>

**Jawaban:** Serangan *CSRF* menargetkan *Browser Pengguna/Klien* (memaksa peramban korban memicu aksi tanpa disadari menggunakan cookie otentikasi korban). Sebaliknya, *SSRF* menargetkan *Server Backend* aplikasi (memaksa server target untuk melakukan kueri ke server internalnya sendiri yang tertutup dari luar).
</details>

<details>
<summary>❓ Ketika pentester sukses meluncurkan serangan eksploitasi CSRF, perlindungan keamanan apa yang dipastikan tidak diimplementasikan oleh pembuat web?</summary>

**Jawaban:** Nihilnya implementasi validasi *CSRF Token* (token acak sekali-pakai) atau atribut Cookie *SameSite*.
</details>

<details>
<summary>❓ Dalam ranah pembajakan SSRF pada infrastruktur Cloud AWS, alamat IP spesifik apakah yang paling sering dibidik oleh hacker untuk merampas kunci Metadata AWS peladen tersebut?</summary>

**Jawaban:** Alamat IP keramat `169.254.169.254` (IP kredensial Metadata AWS/Cloud).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan taktis antara *CSRF* dan *SSRF*.
- [ ] Saya memahami fungsi pelindung mitigasi *CSRF Token*.
- [ ] Saya paham bahaya eksploitasi *SSRF* (membidik localhost `127.0.0.1`).
- [ ] Saya mengerti cara menyusun skrip pemaksaan CSRF menggunakan tag `<form>` tersembunyi.
- [ ] Saya telah menuntaskan menjawab kuis kilat.

---

## 🔗 Resources

- [PortSwigger CSRF](https://portswigger.net/web-security/csrf) — Laboratorium eksplorasi mengenai kerentanan dan mitigasi *CSRF*.
- [PayloadsAllTheThings - SSRF](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery) — Kumpulan taktik menyasar AWS dan ekstraksi *Metadata* via SSRF.

---

## ➡️ Besok

**Day 3: File Upload & IDOR** — Pengetahuan Anda sudah cukup solid untuk menangkis Injeksi *SQL*, *XSS*, hingga *CSRF/SSRF*. Esok hari, kita akan menyusup lewat celah keamanan yang paling sering dibiarkan terbuka: Kerentanan Unggah Berkas (*File Upload Vulnerability*). Kita akan menyimulasikan cara menginjeksi berkas foto palsu yang menyembunyikan skrip eksekutor jahat (*Webshell Backdoor*) PHP ke dalam server target!

---

*📅 TISS Null Teaming · Week 17 · Day 2 · BREACH Rank*
