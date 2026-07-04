# 💀 Week 17 · Day 2: CSRF & SSRF (State-Changing Attacks)

> **Rank**: BREACH | **Minggu ke-17**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 17 · Day 2/5 | BREACH Rank (Minggu 3 dari 5) | Overall: 82/120 hari (69%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** konsep serangan antara *Cross-Site Request Forgery (CSRF)* dan *Server-Side Request Forgery (SSRF)*.
2. **Mensimulasikan** eksploitasi pemalsuan permintaan dari sisi pengguna (*CSRF*).
3. **Mengeksekusi** pengintaian infrastruktur internal dengan memanipulasi *server backend* (*SSRF*).

---

## 📖 Materi Inti

### CSRF: Menyetir Browser Korban Jarak Jauh

Bayangkan kamu menemukan celah keamanan pada sebuah situs, tetapi *server* situs tersebut telah melindungi *Session Cookie* menggunakan *flag HttpOnly*. Akibatnya, skrip pencurian *Cookie* menggunakan *XSS* tidak akan berfungsi. Jangan khawatir, serangan tidak berhenti di sini! Kamu tidak perlu mencuri *Cookie* korban untuk meretas akunnya; kamu cukup **memaksa browser korban untuk mengeksekusi perintah (seperti transfer uang atau ganti password)** selagi korban masih *login* di situs tersebut.

Taktik ini dikenal sebagai **CSRF (Cross-Site Request Forgery)**. Celah ini terjadi karena *server* hanya mengecek *"Apakah pengguna ini sudah login?"*, tetapi lupa memastikan *"Apakah permintaan ini BENAR-BENAR dilakukan secara sadar oleh pengguna tersebut?"*.

**Skenario Serangan CSRF:**
1. Korban sedang aktif *login* di situs `bank.com`.
2. Melalui rekayasa sosial, penyerang membujuk korban untuk mengeklik tautan miliknya: `http://hacker.com/kucing-lucu.html`.
3. Di dalam *file HTML* "kucing lucu" tersebut, penyerang telah menyisipkan skrip tersembunyi:
   ```html
   <form action="http://bank.com/transfer" method="POST">
    <input type="hidden" name="tujuan" value="rekening-hacker">
    <input type="hidden" name="jumlah" value="1000000">
   </form>
   <script> document.forms[0].submit(); </script>
   ```
4. Karena *browser* korban secara otomatis mengirimkan permintaan formulir tersebut sambil melampirkan *Cookie Login* yang masih aktif, *server* `bank.com` mengira permintaan itu sah. Uang berhasil ditransfer tanpa izin hanya dengan satu klik!

*Mitigasi*: Pengembang web wajib mengimplementasikan **CSRF Token** (kode acak sekali-pakai) di setiap formulir web yang mengubah data.

### SSRF: Menipu Server Menyerang Dirinya Sendiri

Bila *CSRF* berfokus menipu *Browser* pengguna (*Client-Side*)...
Maka **SSRF (Server-Side Request Forgery)** berfokus menipu *Server Backend* aplikasi agar *server* tersebut menyerang *server* lain di dalam jaringan internalnya sendiri (yang biasanya tertutup dari internet publik)!

Seringkali, *server* aplikasi memiliki fitur untuk mengunduh gambar atau data dari *URL* luar, contohnya:
`http://target.com/unduh?url=https://github.com/logo.png`

Penyerang dapat memodifikasi *parameter URL* tersebut dan menggantinya dengan alamat IP *server internal* (seperti `localhost`):
`http://target.com/unduh?url=http://127.0.0.1/admin-panel`

Hasilnya? *Server* aplikasi `target.com` akan mengeksekusi kueri ke panel admin internalnya sendiri, lalu memberikan isi halaman rahasia tersebut kepada penyerang! Celah SSRF sangat populer digunakan untuk mencuri kredensial *AWS Metadata* dengan menyuruh *server* mengakses IP khusus `169.254.169.254`.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merakit skrip eksploitasi CSRF (*CSRF Payload*)!

1. Kunjungi lab ekosistem *PortSwigger: CSRF vulnerability with no defenses*.
2. Temukan fitur "Ganti Email" (*Change Email*) yang ternyata tidak dilindungi oleh *CSRF Token*.
3. Fitur tersebut bekerja dengan mengirimkan *request HTTP POST* ke `/my-account/change-email`.
4. Rakitlah *file HTML* palsu di komputermu:
   ```html
   <form id="bajak" action="https://vulnerable-lab.net/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="hacker@tiss.or.id">
   </form>
   <script> document.getElementById('bajak').submit(); </script>
   ```
5. Saat korban (yang masih *login*) mengeklik *file HTML* buatanmu, email miliknya di *server* target akan otomatis diganti menjadi `hacker@tiss.or.id`. Kamu berhasil mengambil alih akun korban!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar antara serangan CSRF dan SSRF?</summary>

**Jawaban:** *CSRF* menyerang *Browser Korban / Client-Side* (memaksa *browser* korban melakukan aksi menggunakan *cookie* yang masih aktif tanpa disadari). Sebaliknya, *SSRF* menyerang *Server Backend* (memaksa *server* target untuk mengakses layanan di dalam jaringan internalnya sendiri).
</details>

<details>
<summary>❓ Ketika penyerang berhasil melakukan eksploitasi CSRF (seperti mengganti email korban secara diam-diam), fitur keamanan apa yang luput ditambahkan oleh pengembang web?</summary>

**Jawaban:** Tidak adanya perlindungan *CSRF Token* (token acak khusus untuk memvalidasi formulir) atau atribut *Cookie SameSite*.
</details>

<details>
<summary>❓ Dalam serangan SSRF pada infrastruktur Cloud seperti AWS, alamat IP spesifik apa yang sering dibidik oleh penyerang untuk mencuri kunci Metadata server?</summary>

**Jawaban:** Alamat IP internal Cloud `169.254.169.254`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan konsep antara *CSRF* dan *SSRF*.
- [ ] Saya memahami pentingnya penggunaan *CSRF Token* pada formulir web.
- [ ] Saya paham bahaya eksploitasi *SSRF* yang menargetkan akses internal (`127.0.0.1`).
- [ ] Saya mengerti cara merakit *Payload CSRF* menggunakan tag `<form>` tersembunyi.
- [ ] Saya telah menuntaskan evaluasi *Quiz Kilat*.

---

## 🔗 Resources

- [PortSwigger CSRF](https://portswigger.net/web-security/csrf) — Laboratorium praktik mengenai kerentanan dan mitigasi serangan *CSRF*.
- [PayloadsAllTheThings - SSRF](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery) — Kumpulan referensi *payload SSRF* untuk berbagai layanan infrastruktur *Cloud*.

---

## ➡️ Besok

**Day 3: File Upload & IDOR** — Pengetahuanmu sudah cukup solid untuk memahami serangan *SQLi*, *XSS*, hingga *CSRF/SSRF*. Besok hari, kita akan membahas celah keamanan yang sangat fatal namun sering disepelekan: Kerentanan Unggah Berkas (*File Upload Vulnerability*). Kita akan menyimulasikan cara mengunggah file foto palsu yang ternyata berisi skrip peretas (*Webshell Backdoor*) ke dalam *server* target!

---

*📅 TISS Null Teaming · Week 17 · Day 2 · BREACH Rank*
