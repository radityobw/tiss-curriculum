# 💀 Week 18 · Day 1: Burp Suite Proxy & Intercept

> **Rank**: BREACH | **Minggu ke-18**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 18 · Day 1/5 | BREACH Rank (Minggu 4 dari 5) | Overall: 86/120 hari (71%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep dan fungsi alat penengah lalu lintas web (*Proxy*).
2. **Mengonfigurasi** *Burp Suite* agar terhubung dengan *Browser*.
3. **Mencegat** dan memanipulasi *request HTTP* (*Intercept & Modify Requests*).

---

## 📖 Materi Inti

### Mengenal Burp Suite

Selama beberapa minggu terakhir, kamu telah belajar mencari kerentanan web secara manual, menebak *URL*, dan mengandalkan aplikasi terminal (Nmap, SQLMap). Mulai hari ini, kita akan meningkatkan efisiensi pengujian ke tahap selanjutnya!

Sambutlah **Burp Suite** (dikembangkan oleh *PortSwigger*). Aplikasi ini adalah standar industri dan *senjata utama* nomor satu bagi para profesional keamanan siber dan *Bug Hunter* dalam melakukan pengujian penetrasi web (*Web Penetration Testing*). Tanpa menguasai Burp Suite, seorang pentester akan sangat kesulitan dalam menganalisis dan membongkar kerentanan modern.

### Inti dari Burp Suite: Proxy

Dalam kondisi normal, *Browser* (Chrome/Firefox) mengirimkan permintaan (*Request HTTP*) secara langsung ke server, lalu server akan langsung merespons dengan menampilkan halaman web (*Response*). Semua proses pertukaran data itu terjadi dalam hitungan milidetik di belakang layar.

**Burp Suite Proxy** akan mengubah alur tersebut. 

*Burp* berfungsi sebagai penengah (*Man-in-the-Middle*) yang berdiri tepat di tengah-tengah jalur komunikasi antara *Browser* komputermu dan Server target.
1. Browser mengirimkan kueri `Request`.
2. Paket `Request` itu **dicegat dan ditahan (*Intercept*)** oleh *Burp Proxy*. (Browser akan terus *loading* berputar-putar menantikan balasan).
3. Di dalam antarmuka *Burp*, kamu dapat **melihat, membongkar, dan mengubah** isi dari `Request` tersebut secara bebas!
4. Setelah selesai mengubah data, kamu mengeklik tombol **Forward** untuk melepaskan paket yang sudah dimodifikasi tersebut menuju server target.

### Mengapa Manipulasi Ini Fatal?

Karena kamu bisa mencegat dan mengedit data *Request* di tengah jalan, semua perlindungan keamanan yang dipasang pengembang web di sisi antarmuka (*Frontend*)—seperti filter *JavaScript* atau pembatasan `maxlength` pada form *HTML*—menjadi **SAMA SEKALI TIDAK BERGUNA**.

**Contoh Skenario:**
Pengembang web merancang form *Transfer Uang* dengan menu *dropdown* di *HTML* yang membatasi nominal transfer maksimal sebesar "Rp 1 Juta". Secara visual di *browser*, kamu hanya bisa memilih nominal 1 Juta. 

Namun, saat tombol submit ditekan, kamu mencegat paket data tersebut di *Burp Suite*. Di dalam *Burp*, kamu menghapus angka "1 Juta" dan mengubahnya menjadi "1 Miliar", lalu menekan tombol **Forward**. *Server* akan menerima permintaan transfer 1 Miliar dan mengizinkannya (jika *server* lalai melakukan validasi ulang di sisi *Backend*). Ini adalah inti dari *Bypass Frontend Validation*!

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari menyimulasikan penggunaan fitur *Intercept* pada *Burp Proxy*!

1. Buka aplikasi **Burp Suite Community Edition** (Biasanya sudah terpasang bawaan di Kali Linux atau dapat diunduh gratis).
2. Pergi ke tab **Proxy** > **Intercept** dan pastikan tombol **Intercept is on** menyala.
3. Buka *Browser* khusus bawaan Burp dengan mengeklik tombol **Open Browser** di tab yang sama.
4. Di *Browser* tersebut, kunjungi halaman web sembarang, misalnya `example.com` atau web kampusmu.
5. Saat kamu menekan Enter, halaman web akan macet (*loading* terus-menerus).
6. Kembali ke jendela *Burp Suite*. Kamu akan melihat kode data HTTP *Request* mentah tertahan di layar!
7. Cobalah mencari baris *Header* `User-Agent: Mozilla/5.0...`. Hapus teks "Mozilla..." tersebut dan ganti dengan namamu sendiri, contoh: `User-Agent: Mesin-Peretas-Dewa`.
8. Klik tombol **Forward** hingga *loading browser* selesai.
9. Selamat! Kamu baru saja berhasil memodifikasi paket *HTTP* secara langsung dan menipu *server* dengan identitas *browser* palsu buatanmu sendiri!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam arsitektur peretasan Web, apa fungsi utama dari fitur <i>Proxy</i> pada Burp Suite?</summary>

**Jawaban:** Bertindak sebagai perantara (*Man-in-the-Middle*) untuk mencegat (*Intercept*), menahan, dan memungkinkan peretas untuk memodifikasi paket *Request* HTTP sebelum diteruskan ke *server* target.
</details>

<details>
<summary>❓ Mengapa perlindungan validasi <i>Frontend</i> (seperti JavaScript atau batasan input HTML) menjadi tidak berguna saat penyerang menggunakan Burp Suite?</summary>

**Jawaban:** Karena penyerang menggunakan *Burp Suite* untuk mengubah data paket HTTP secara mentah *setelah* paket tersebut lolos dari validasi *browser/Frontend*, tepat sebelum paket tersebut mencapai *server Backend*.
</details>

<details>
<summary>❓ Ketika kamu selesai mengedit sebuah paket HTTP yang ditahan oleh Burp Proxy, tombol apa yang harus kamu tekan agar paket tersebut dilepaskan dan meluncur ke Server target?</summary>

**Jawaban:** Tombol **Forward**.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami fungsi dan posisi *Web Proxy* (*Man-in-the-Middle*).
- [ ] Saya dapat menggunakan fitur *Open Browser* pada Burp Suite.
- [ ] Saya menguasai cara mengaktifkan dan menggunakan fitur *Intercept*.
- [ ] Saya berhasil mengubah nilai *User-Agent* pada *Mini Lab*.
- [ ] Saya telah menjawab seluruh *Quiz Kilat* dengan benar.

---

## 🔗 Resources

- [PortSwigger Burp Proxy Docs](https://portswigger.net/burp/documentation/desktop/tools/proxy) — Dokumentasi resmi dan panduan lengkap penggunaan *Burp Proxy* dari pembuatnya.

---

## ➡️ Besok

**Day 2: Burp Suite Repeater & Intruder** — Mencegat paket satu per satu dan memencet tombol *Forward* tentu melelahkan jika kamu harus mencoba puluhan injeksi *SQLi* atau *XSS*. Besok hari, kita akan mempelajari dua fitur ajaib *Burp* lainnya: **Repeater** (untuk mengirim *Request* modifikasi secara berulang tanpa perlu menggunakan *Browser*) dan **Intruder** (fitur otomatisasi untuk menembakkan ribuan *payload brute force* dalam hitungan detik)!

---

*📅 TISS Null Teaming · Week 18 · Day 1 · BREACH Rank*
