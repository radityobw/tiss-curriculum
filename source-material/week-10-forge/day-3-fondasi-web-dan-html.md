# 🔨 Week 10 · Day 3: Fondasi Web & HTML Dasar

> **Rank**: FORGE | **Minggu ke-10**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 10 · Day 3/5 | FORGE Rank (Minggu 1 dari 5) | Overall: 48/120 hari (40%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** cara kerja internet (Client-Server Model dan HTTP)
2. **Menulis** struktur dasar dokumen HTML5 dengan Semantic Tags
3. **Membuat** formulir (Forms) sederhana dengan metode GET dan POST

---

## 📖 Materi Inti

### Bagaimana Web Bekerja?

Sebelum membuat web, kamu harus paham cara kerjanya. Internet pada dasarnya beroperasi dengan model **Client-Server**.
- **Client ()**: Laptop atau HP-mu yang menggunakan browser (Chrome, Firefox). bertugas *meminta* (Request).
- **Server (Peladen)**: Komputer super kuat di tempat lain yang selalu menyala. Server bertugas *menjawab* (Response).

Saat kamu mengetik `www.google.com`, browsermu mengirimkan surat bernama **HTTP Request** ke server Google. Server Google lalu merespons dengan **HTTP Response** yang berisi kode HTML, CSS, dan JavaScript agar browsermu bisa melukis halamannya.

### HTML: Kerangka Tulang Website

**HTML (HyperText Markup Language)** bukanlah bahasa pemrograman. Ia adalah bahasa *markup* (penanda) yang berfungsi sebagai tulang/kerangka dari sebuah website.

```html
<!DOCTYPE html>
<html>
<head>
 <title>Halaman Pertamaku</title>
</head>
<body>
 <header>
 <h1>Selamat Datang di TISS</h1>
 </header>
 <main>
 <p>Ini adalah paragraf pertama saya.</p>
 <img src="logo.png" alt="Logo TISS">
 </main>
</body>
</html>
```

Perhatikan tag seperti `<header>` dan `<main>`. Ini disebut **Semantic Tags**. Di era HTML5 modern, kita tidak lagi menggunakan `<div>` untuk semua hal. Semantic tags membuat struktur web lebih mudah dipahami oleh mesin pencari (SEO) dan pembaca layar tunanetra (Accessibility).

### Formulir (HTML Forms) & Pengiriman Data

Jika HTML biasa hanya menampilkan informasi, **Forms** memungkinkan *mengirimkan* informasi kembali ke Server (contoh: Login, Register, Cari Barang).

Ada 2 metode pengiriman data utama di internet:
1. **GET**: Mengirimkan data dengan menempelkannya langsung di URL (contoh: `google.com/search?q=kucing`). Sangat tidak aman untuk password karena terekspos di Address Bar.
2. **POST**: Mengirimkan data melalui "perut" (Body) surat HTTP. Data tersembunyi dari URL (contoh: mengirim formulir). 

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari membuat formulir sederhana!

1. Buka **VS Code** dan buat file bernama `index.html`.
2. Ketik `!` lalu tekan `Tab` atau `Enter` (ini adalah jalan pintas Emmet untuk memunculkan kerangka HTML otomatis).
3. Di dalam tag `<body>`, buat form sederhana ini:

```html
<form action="/login-sukses" method="POST">
 <h2>Formulir Pasukan Biru</h2>
 
 <label for="username">Username:</label>
 <input type="text" id="username" name="username" required>
 
 <br><br>
 
 <label for="password">Password rahasia:</label>
 <input type="password" id="password" name="password" required>
 
 <br><br>
 
 <button type="submit">Daftar Sekarang!</button>
</form>
```
4. Simpan, lalu buka file `index.html` tersebut dengan mengklik dua kali agar terbuka di browsermu. Coba isi dan klik daftar!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa tidak mengirimkan kata sandi (password) menggunakan metode GET?</summary>

**Jawaban:** Karena metode GET akan menempelkan semua data masukan langsung ke dalam URL di Address Bar (contoh: `login?user=admin&pass=123`). Hal ini membuat password sangat mudah terlihat oleh orang di sebelah kita, serta akan tercatat permanen di *history* (riwayat) peramban.

</details>

<details>
<summary>❓ Apa yang dimaksud dengan tag semantik (Semantic Tags) dalam HTML5?</summary>

**Jawaban:** Tag semantik adalah tag yang penamaannya secara jelas mendeskripsikan maknanya kepada *developer* dan *browser* (contoh: `<article>`, `<footer>`, `<nav>`), dibandingkan dengan tag non-semantik (seperti `<div>` atau `<span>`) yang tidak memberitahu apa pun tentang isi kontennya.

</details>

<details>
<summary>❓ Komponen komputer manakah yang bertugas menerjemahkan kode HTML menjadi tampilan visual berwarna yang bisa dilihat manusia?</summary>

**Jawaban:** atau Peramban Web (*Web Browser* seperti Google Chrome atau Firefox).

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami siklus Client-Server dan HTTP (Request/Response)
- [ ] Saya mengetahui struktur dasar kerangka dokumen HTML
- [ ] Saya bisa membedakan kapan harus menggunakan metode GET dan POST
- [ ] Saya berhasil merakit form sederhana di Mini Lab
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [MDN Web Docs: HTML Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) — Dokumentasi de-facto paling lengkap untuk HTML (dari Mozilla).

---

## ➡️ Besok

**Day 4: CSS Fundamentals & DevTools** — Kerangka HTML kita hari ini tampak sangat kuno dan kaku bak situs tahun 1990-an. Besok, kita akan menyuntikkan nyawa, warna, dan tata letak elegan dengan **CSS**, serta mengintip rahasia di balik layar menggunakan pisau lipat *hacker*: **Developer Tools**!

---

*📅 TISS Null Teaming · Week 10 · Day 3 · FORGE Rank*
