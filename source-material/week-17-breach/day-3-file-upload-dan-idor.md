# 💀 Week 17 · Day 3: File Upload & IDOR

> **Rank**: BREACH | **Minggu ke-17**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 17 · Day 3/5 | BREACH Rank (Minggu 3 dari 5) | Overall: 83/120 hari (70%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengeksploitasi** kelalaian validasi pada fitur unggah berkas (File Upload).
2. **Mensimulasikan** penyusupan cangkang belakang ke web server (*Web Shell* PHP).
3. **Mendemonstrasikan** eksploitasi celah kontrol akses (*IDOR / Broken Access Control*) untuk mengakses data rahasia pengguna lain.

---

## 📖 Materi Inti

### Membajak Infrastruktur via Pintu Belakang (File Upload)

Tak banyak fitur aplikasi web yang berpotensi menghasilkan kerentanan fatal selain fitur **Unggah Dokumen (File Upload)** (misalnya fitur unggah Foto Profil atau PDF). 
Jika pengembang sekadar memvalidasi keamanan unggahan ala kadarnya (semisal hanya mengecek ekstensi dari sisi *frontend*), pentester tidak akan mengunggah gambar *JPEG* sungguhan, melainkan akan memaksakan file berisi skrip berbahaya untuk masuk ke server!

Jika backend target menggunakan bahasa pemrograman **PHP**, pentester cukup merakit file berekstensi `.php` (misal `shell.php`). Skrip ini nantinya akan memberikan fungsi untuk menjalankan perintah terminal OS server secara langsung dari browser.

**Contoh isi skrip file `shell.php` sederhana:**
```php
<?php system($_GET['cmd']); ?>
```

Ketika file `shell.php` berhasil melewati penyaring dan tersimpan di direktori server (contoh: `target.com/uploads/shell.php`), pentester tinggal membuka URL file tersebut dan mengeksekusi perintah terminal lewat parameter URL:
`target.com/uploads/shell.php?cmd=cat /etc/passwd`

*Seketika!* Server target akan merespons dengan menampilkan isi dari file sistem rahasia `/etc/passwd`. Berbekal jalan pintas ini (*Backdoor Web Shell*), pentester dapat mengeksploitasi dan mengambil alih kendali penuh atas server target!

### Menelikung Tameng Penyaring Ekstensi 

Ketika pengembang memasang perlindungan *filter* di server yang mengharuskan "Hanya boleh mengunggah file JPG/PNG", pentester membalasnya dengan beberapa taktik *bypass*:

- **Bypass Ekstensi Ganda:** Mengganti nama file menjadi `shell.php.jpg` atau menggunakan taktik injeksi Null Byte `shell.php%00.jpg`.
- **Manipulasi MIME Type:** Menggunakan Burp Suite, pentester mencegat *Request* dan memodifikasi *header* `Content-Type: application/x-php` menjadi `Content-Type: image/jpeg` agar WAF atau filter server mengira file tersebut benar-benar adalah gambar.

### Mahaguru Penyamaran : IDOR 

*(Kita meninjau ulang kerentanan IDOR sebagaimana dibahas di materi sebelumnya, tapi kini dengan kacamata eksploitasi ofensif)*

**IDOR (Insecure Direct Object Reference)** adalah kerentanan *Broken Access Control* yang terjadi ketika server menggunakan angka atau ID untuk mengakses objek/dokumen, namun sama sekali tidak memvalidasi *"Apakah pengguna yang sedang login berhak melihat objek dengan ID ini?"*.

Pengguna awam mengakses nota belanja miliknya melalui tautan:
`target.com/struk?nota_id=505`

Namun, pentester dengan insting berburu kerentanan (*Bug Bounty*) hanya perlu mengubah angka pada URL tersebut menjadi angka lain:
`target.com/struk?nota_id=506`

Karena server tidak melakukan pengecekan otorisasi, ia dengan patuh akan menampilkan nota belanja, nomor kartu kredit, atau data pribadi utuh milik **pengguna lain** yang seharusnya dijaga kerahasiaannya!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari meracik ekskavasi cangkang (*Web Shell*) PHP untuk menembus target!

1. Kunjungi pelataran lingkungan uji *TryHackMe* atau *PortSwigger* yang dikhususkan untuk simulasi *File Upload*.
2. Web target menuntut pengguna mengunggah file gambar (*Avatar*).
3. Buat file teks berekstensi `.php` (misal: `avatar.php`) dan isi dengan skrip:
   ```php
   <?php echo system('whoami'); ?>
   ```
4. Coba unggah file tersebut. *Web merespons Gagal karena sistem memvalidasi dan menuntut format JPG!*
5. Nyalakan Burp Suite, lalu cegat (*Intercept*) paket pengiriman file tersebut.
6. Edit bagian `filename="avatar.php"` menjadi `filename="avatar.php.jpg"`. Sebagai alternatif, Anda bisa mengganti baris header `Content-Type` ke `image/jpeg`.
7. Lepaskan cegatan (*Forward*)! Bila berhasil lolos, buka URL pemuatan foto tersebut.
8. Laman foto tersebut seketika akan mencetak output dari sistem, misal: *www-data* (nama user apache/terminal peladen). Anda telah sukses mendapatkan eksekusi kueri langsung *RCE (Remote Code Execution)*!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Skrip atau program berbahaya (sering berekstensi PHP) yang diunggah ke dalam server web untuk menjalankan perintah sistem operasi (RCE) secara jarak jauh dikenal dengan istilah apa?</summary>

**Jawaban:** Web Shell (atau Backdoor Shell).
</details>

<details>
<summary>❓ Ketika meluncurkan serangan bypass upload, taktik merubah nilai header `Content-Type: application/php` menjadi `Content-Type: image/jpeg` agar server mengira file tersebut sebagai gambar disebut dengan teknik apa?</summary>

**Jawaban:** MIME Type Bypass (atau Content-Type Spoofing).
</details>

<details>
<summary>❓ Pada kerentanan IDOR, server melakukan kelalaian fatal karena mempercayai akses dokumen hanya berdasarkan parameter URL (seperti ID), tanpa pernah mencocokkannya dengan apa?</summary>

**Jawaban:** Tanpa mencocokkannya dengan *Session Cookie* (atau otorisasi Token pengguna yang sedang login) untuk memverifikasi apakah pemilik Cookie tersebut memang berhak melihat dokumen ID tersebut.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami logika kendali *Web Shell PHP* (`system($_GET['cmd'])`).
- [ ] Saya fasih menjabarkan siasat bypass validasi *File Upload* (MIME spoofing, Null Byte).
- [ ] Saya paham cara memanipulasi rentetan ID untuk menemukan celah *IDOR*.
- [ ] Saya telah menuntaskan validasi menjawab semua *quiz kilat*.

---

## 🔗 Resources

- [PortSwigger File Upload](https://portswigger.net/web-security/file-upload) — Laboratorium eksplorasi kerentanan bypass fitur unggahan.
- [PayloadsAllTheThings - Upload Insecure Files](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files) — Kompilasi payload dan teknik manipulasi *File Upload*.

---

## ➡️ Besok

**Day 4: Chaining Vulnerabilities** — Anda mengira bahwa menemukan kerentanan *IDOR* skala kecil atau celah peramban *Open Redirect* itu tidak berbahaya? Esok hari, kita akan meresapi seni pamungkas dari eksploitasi mahaguru: Merantai Kerentanan (*Chaining Vulns*). Anda akan belajar merajut celah kecil *XSS*, disilangkan dengan kerentanan *SSRF*, dan dipadukan dengan kelalaian *File Upload* untuk meledakkan server menjadi insiden *Remote Code Execution* berskala *Bug Bounty* jutaan rupiah!

---

*📅 TISS Null Teaming · Week 17 · Day 3 · BREACH Rank*
