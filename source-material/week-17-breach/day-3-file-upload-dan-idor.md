# 💀 Week 17 · Day 3: File Upload & IDOR

> **Rank**: BREACH | **Minggu ke-17**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 17 · Day 3/5 | BREACH Rank (Minggu 3 dari 5) | Overall: 83/120 hari (70%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengeksploitasi** celah keamanan pada fitur unggah berkas (*File Upload*).
2. **Mensimulasikan** penyusupan *Web Shell* ke *server* target untuk mendapatkan *Remote Code Execution*.
3. **Mendemonstrasikan** eksploitasi kontrol akses (*IDOR / Broken Access Control*) untuk mencuri data pengguna lain.

---

## 📖 Materi Inti

### Membajak Server Melalui File Upload

Salah satu fitur aplikasi web yang paling rawan dieksploitasi hingga menyebabkan *server* diambil alih sepenuhnya adalah fitur **Unggah Berkas (File Upload)** (seperti fitur *upload* Foto Profil atau PDF). 

Jika pengembang hanya mengecek jenis ekstensi (*jpg/png*) dari sisi *frontend* (browser) saja, penyerang bisa mengakali pengecekan tersebut dan mengunggah *file* berisi kode *backend* (seperti PHP/ASP) ke *server*!

Jika *backend* target menggunakan **PHP**, penyerang cukup merakit sebuah skrip berekstensi `.php` (misalnya `shell.php`). Skrip ini berfungsi untuk menjalankan perintah terminal (OS) secara langsung dari *browser*.

**Contoh isi skrip file `shell.php` sederhana:**
```php
<?php system($_GET['cmd']); ?>
```

Ketika *file* `shell.php` berhasil melewati filter dan tersimpan di direktori *server* (contoh: `target.com/uploads/shell.php`), penyerang tinggal membuka URL *file* tersebut dan mengeksekusi perintah terminal melalui *parameter URL*:
`target.com/uploads/shell.php?cmd=cat /etc/passwd`

Hasilnya? *Server* target akan merespons dengan menampilkan isi dari *file* sistem `/etc/passwd`. Menggunakan skrip *Web Shell* ini, penyerang mendapatkan kendali jarak jauh (RCE) atas *server*!

### Melewati Filter Ekstensi (Bypass Upload)

Ketika pengembang memasang perlindungan *filter* di *backend* yang mengharuskan "Hanya boleh mengunggah file JPG/PNG", penyerang dapat menggunakan beberapa taktik *bypass*:

- **Bypass Ekstensi Ganda:** Mengganti nama file menjadi `shell.php.jpg` atau menggunakan trik *Null Byte Injection* `shell.php%00.jpg`.
- **Manipulasi MIME Type:** Menggunakan Burp Suite, penyerang mencegat (*Intercept*) HTTP Request saat *upload*, lalu mengubah nilai `Content-Type: application/x-php` menjadi `Content-Type: image/jpeg` agar *Web Application Firewall (WAF)* mengira *file* tersebut adalah gambar.

### Eksploitasi IDOR (Insecure Direct Object Reference)

Kita pernah membahas sedikit konsep ini, namun mari lihat dari kacamata eksploitasi.
**IDOR** adalah jenis kerentanan *Broken Access Control* yang sangat umum. Ini terjadi ketika *server* menggunakan ID atau nomor urut untuk menampilkan dokumen, namun **tidak memeriksa apakah pengguna yang sedang login berhak melihat dokumen dengan ID tersebut**.

Pengguna biasa melihat nota belanjanya melalui *URL*:
`target.com/struk?nota_id=505`

Namun, seorang *Bug Hunter* atau penyerang hanya perlu mencoba mengubah angka ID tersebut:
`target.com/struk?nota_id=506`

Karena *server* tidak mengecek validasi kepemilikan, *server* akan mematuhi permintaan tersebut dan menampilkan nota belanja milik **pengguna lain** yang berisi data pribadi dan nomor kartu kredit!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan injeksi *Web Shell* PHP!

1. Kunjungi lingkungan lab *PortSwigger: Web Security Academy (File Upload vulnerabilities)*.
2. Temukan skenario di mana pengguna diminta mengunggah foto profil (*Avatar*).
3. Buatlah sebuah *file* berakhiran `.php` (misal: `avatar.php`) dan isi dengan skrip:
   ```php
   <?php echo system('whoami'); ?>
   ```
4. Coba unggah *file* tersebut secara normal. Web akan merespons *Error* karena *server* mengharuskan *file* berupa gambar (JPG/PNG).
5. Nyalakan **Burp Suite**, lalu aktifkan fitur *Intercept* dan unggah ulang *file* tersebut.
6. Pada *Burp Suite*, ubah baris *header* `Content-Type: application/x-php` menjadi `Content-Type: image/jpeg`.
7. Teruskan (*Forward*) permintaan tersebut! Jika berhasil lolos, buka *URL* di mana foto profilmu disimpan.
8. Halaman tersebut tidak akan menampilkan foto, melainkan mencetak teks hasil eksekusi terminal (misal: `www-data` atau `apache`). Kamu sukses mendapatkan eksekusi perintah jarak jauh (*Remote Code Execution*)!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Skrip atau program berbahaya (sering berekstensi PHP) yang diunggah ke dalam server web untuk memberikan penyerang akses menjalankan perintah sistem operasi (RCE) dari jarak jauh dikenal dengan istilah apa?</summary>

**Jawaban:** Web Shell (atau Backdoor Shell).
</details>

<details>
<summary>❓ Saat melakukan serangan unggah berkas, taktik mencegat request dan mengubah nilai header <code>Content-Type: application/php</code> menjadi <code>Content-Type: image/jpeg</code> agar server mengira file tersebut adalah gambar disebut dengan teknik apa?</summary>

**Jawaban:** MIME Type Bypass (atau Content-Type Spoofing).
</details>

<details>
<summary>❓ Pada kerentanan IDOR, server melakukan kesalahan karena hanya mengambil dokumen berdasarkan nomor ID di URL, tanpa mencocokkannya dengan apa?</summary>

**Jawaban:** Tanpa mencocokkannya dengan Sesi / *Cookie* pengguna (untuk memastikan apakah pengguna yang sedang *login* memang pemilik sah dari ID dokumen tersebut).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami bagaimana *Web Shell PHP* (`system($_GET['cmd'])`) bekerja.
- [ ] Saya mengetahui taktik melewati filter unggahan (*MIME spoofing, Null Byte, Double Extension*).
- [ ] Saya paham cara mengeksploitasi celah *IDOR* dengan mengubah ID pada URL.
- [ ] Saya telah menuntaskan evaluasi menjawab semua *Quiz Kilat*.

---

## 🔗 Resources

- [PortSwigger File Upload](https://portswigger.net/web-security/file-upload) — Laboratorium eksplorasi kerentanan bypass fitur unggahan.
- [PayloadsAllTheThings - Upload Insecure Files](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files) — Kompilasi *payload* dan trik bypass *File Upload*.

---

## ➡️ Besok

**Day 4: Chaining Vulnerabilities** — Kamu mungkin berpikir bahwa menemukan satu celah kecil (*Bug*) yang tidak terlalu berbahaya itu tidak bernilai. Namun besok, kita akan membahas seni eksploitasi tingkat tinggi: Merantai Kerentanan (*Chaining Vulnerabilities*). Kamu akan belajar bagaimana menggabungkan beberapa celah berisiko rendah (seperti *Open Redirect* dan celah logika bisnis) untuk menciptakan satu serangan berantai yang fatal dan menghasilkan *Remote Code Execution*!

---

*📅 TISS Null Teaming · Week 17 · Day 3 · BREACH Rank*
