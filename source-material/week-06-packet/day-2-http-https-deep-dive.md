# 📡 Week 6 · Day 2: HTTP/HTTPS Deep-Dive

> **Rank**: PACKET | **Minggu ke-6**, Hari 2/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 6 · Day 2/5 | PACKET Rank (Minggu 2 dari 5) | Overall: 27/120 hari (22%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** siklus *Request/Response* pada protokol HTTP
2. **Membedakan** metode HTTP yang paling umum (GET vs POST)
3. **Mengklasifikasikan** kategori HTTP Status Code (200s, 300s, 400s, 500s)
4. **Menjelaskan** pentingnya "S" pada HTTPS

---

## 📖 Materi Inti

### Protokol Web: HTTP (Layer 7)

**HTTP** (*Hypertext Transfer Protocol*) adalah bahasa resmi *World Wide Web*. Setiap kali kamu membuka website, browsermu sedang berbicara menggunakan HTTP kepada web server. 

HTTP beroperasi menggunakan TCP (Port 80 secara default), yang berarti datanya dijamin sampai dengan utuh.

Siklus kerjanya sangat sederhana seperti tanya-jawab (*Request & Response*):
1. **Client (Browser-mu)** mengirim *HTTP Request* ("Tolong berikan saya halaman Beranda").
2. **Server** memprosesnya lalu membalas dengan *HTTP Response* ("Oke, ini kode HTML-nya").

### HTTP Methods (Kata Kerja)

Saat browser mengirim *Request*, ia harus memberi tahu server **apa yang ingin dia lakukan**. Ini disebut HTTP Methods. Dua yang paling utama:

| Method | Fungsi | Contoh Penggunaan | Sifat |
|--------|--------|-------------------|-------|
| **GET** | "Beri saya data!" (Membaca/Mengambil) | Membuka artikel, melihat profil, memutar video. | Semua data (URL) terlihat jelas di address bar. |
| **POST** | "Ini saya beri data baru!" (Mengirim) | Login, mengirim form, mengunggah foto. | Data dibungkus dalam "Body", tidak terlihat di URL. Lebih aman. |

> ⚠️ **Catatan Penting**: Jangan pernah membuat form Login menggunakan metode `GET`! (Bayangkan URL-nya jadi: `google.com/login?user=admin&password=rahasia123`). Passwordmu akan tersimpan di history browser selamanya!

### HTTP Status Codes (Kode Balasan)

Saat server merespons, server akan memberi kode angka 3 digit yang memberitahu nasib request-mu.

| Awalan Angka | Arti Utama | Kode Paling Terkenal |
|--------------|------------|-----------------------|
| **1xx** (Informational) | "Tunggu sebentar, sedang diproses." | 100 Continue |
| **2xx** (Success) | "Oke, berhasil!" | **200 OK** (Sukses memuat web) |
| **3xx** (Redirection) | "Bukan di sini, pindah ke URL lain ya."| **301 Moved Permanently**, **302 Found** |
| **4xx** (Client Error) | "Kamu (client) yang salah / dilarang!" | **403 Forbidden** (Tidak ada akses), **404 Not Found** (Web tidak ada) |
| **5xx** (Server Error) | "Kami (server) yang rusak/down." | **500 Internal Server Error** (Kodenya nge-bug), **502 Bad Gateway** |

*(Cara mudah menghafal 4xx vs 5xx: Jika 404, artinya URL yang kamu ketik salah. Jika 500, berarti teknisi webnya yang harus dimarahi karena servernya error).*

### Mengapa HTTPS Wajib?

HTTP standar adalah protokol *plaintext* (teks telanjang). Artinya, semua yang kamu kirim—termasuk password—bergerak dari kabel LAN-mu, melewati router kosan, lalu lewat tiang telkom, semuanya dalam bentuk teks yang **bisa dibaca siapa saja** di jalan.

**HTTPS** (Hypertext Transfer Protocol **Secure**) memecahkan masalah ini dengan menempelkan teknologi **TLS/SSL**.
Sebelum data dikirim, TLS akan **mengenkripsinya** (menyandikannya) menjadi teks acak. 
Bahkan jika ada *hacker* menyadap WiFi kampus, mereka hanya akan melihat teks acak (`#$!*ASDf28@%`) alih-alih passwordmu. HTTPS menggunakan Port **443**.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari kita lihat rahasia di balik browser-mu menggunakan **Developer Tools**!

1. Buka Google Chrome (atau Firefox).
2. Pergi ke halaman apa saja, misalnya `https://wikipedia.org`.
3. Tekan **F12** (atau klik kanan -> *Inspect Element*).
4. Klik tab **Network**. (Jika kosong, tekan F5 untuk me-refresh halaman).
5. Kamu akan melihat daftar panjang muncul. Klik file yang paling atas (biasanya bernama `wikipedia.org`).
6. Di kotak sebelah kanan yang muncul, klik tab **Headers**.
 - Cari baris **Request Method** (Apakah GET atau POST?).
 - Cari baris **Status Code** (Apakah 200 OK?).

Kamu baru saja membaca percakapan mentah HTTP yang terjadi di balik layar!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa form login bank tidak boleh menggunakan metode HTTP GET?</summary>

**Jawaban:** Karena pada metode GET, semua data yang dikirim akan terlihat di dalam URL (Address Bar) browser. Itu berarti *username* dan *password* akan tertulis jelas di URL, tersimpan di *history* browser, dan dicatat di *log* server secara telanjang. Form login harus selalu menggunakan metode **POST** agar data disembunyikan di dalam *Body Request*.

</details>

<details>
<summary>❓ Kamu mencoba mengakses halaman Admin sebuah website (`/admin-dashboard`), namun layarmu memunculkan tu 403 Forbidden. Apa artinya?</summary>

**Jawaban:** Kode **4xx** berarti *Client Error* (Kesalahan dari sisimu). Lebih spesifik, **403 Forbidden** berarti server tahu siapa kamu, halamannya benar ada, TAPI kamu **tidak memiliki izin (hak akses/otorisasi)** untuk masuk ke halaman tersebut.

</details>

<details>
<summary>❓ Apa bedanya port 80 dan port 443 dalam konteks web?</summary>

**Jawaban:** 
- **Port 80** digunakan oleh **HTTP** (Koneksi biasa, tidak aman/tidak terenkripsi).
- **Port 443** digunakan oleh **HTTPS** (Koneksi aman, terenkripsi oleh TLS/SSL, ditandai dengan ikon gembok di browser).

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami siklus Request dan Response HTTP
- [ ] Saya bisa membedakan kapan menggunakan GET dan POST
- [ ] Saya hafal arti awalan kode status (2xx Sukses, 4xx Kamu yang salah, 5xx Server yang salah)
- [ ] Saya mengerti perbedaan HTTP (Port 80) dan HTTPS (Port 443)
- [ ] Saya sudah melakukan Mini Lab Inspect Element
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [MDN Web Docs: HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) — Daftar resmi dan penjelasan semua kode HTTP. (Sangat berguna kalau kamu nanti masuk ke rank Forge / Web Dev!).
- [HTTP Status Dogs](https://httpstatusdogs.com/) — (Hiburan) Menghafal kode HTTP dengan gambar anjing lucu.

---

## ➡️ Besok

**Day 3: DNS, ARP, DHCP, ICMP** — Di balik layar internet, ada protokol-protokol diam yang bekerja bak kurir dan operator tanpa kamu sadari. Kita akan membedah keempat "unsung heroes" (pahlawan tanpa tanda jasa) dalam jaringan!

---

*📅 TISS Null Teaming · Week 6 · Day 2 · PACKET Rank*
