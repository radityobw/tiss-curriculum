# 💀 Week 19 · Day 3: Writing Good Proof of Concepts (PoCs)

> **Rank**: BREACH | **Minggu ke-19**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 19 · Day 3/5 | BREACH Rank (Minggu 5 dari 5) | Overall: 93/120 hari (78%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** esensi dari dokumen *Proof of Concept* (PoC) yang solid dan tidak terbantahkan.
2. **Merakit** langkah-langkah reproduksi eksploitasi (*Steps to Reproduce*) dengan jelas dan sistematis.
3. **Menerapkan** penyertaan barang bukti teknis (<i>HTTP Request/Response</i> & <i>Screenshots/Video</i>).

---

## 📖 Materi Inti

### Membantah Alibi dengan Bukti Otentik (Proof of Concept)

Dalam industri *Bug Bounty* maupun *Pentesting* profesional, sering kali *Bug Hunter* pemula mendapati laporannya DITOLAK (dengan status *Not Applicable* atau *Can't Reproduce*). Hal ini biasanya bukan karena mereka tidak menemukan celah, tetapi karena mereka gagal memberikan instruksi yang jelas bagi *Developer* untuk meniru (merekreasi) serangan tersebut!

**Proof of Concept (PoC)** adalah inti dari sebuah laporan keamanan. Ini adalah resep eksploitasi. Jika kamu menulis PoC dengan cemerlang, *Developer* yang membacanya akan berhasil menduplikasi celah yang sama persis dalam hitungan detik.

### 3 Pilar PoC yang Komprehensif

**1. Steps to Reproduce (Langkah Reproduksi):**
Tulislah instruksi secara berurutan layaknya panduan teknis. Jangan melewatkan satu langkah pun.
- *BURUK:* "Eksekusi SQLi ke parameter ID."
- *SEMPURNA:* 
  - "Langkah 1: Kunjungi URL `http://target.com/produk`."
  - "Langkah 2: Tangkap lalu lintas (*Intercept*) menggunakan *Burp Suite*."
  - "Langkah 3: Ubah payload parameter `id=1` menjadi `id=1' AND SLEEP(10)--`."
  - "Langkah 4: Teruskan paket (*Forward*) dan amati bahwa *Browser* terus memuat (*loading*) tertunda selama tepat 10 detik."

**2. HTTP Request & Response (Barang Bukti Teknis):**
Sisipkan teks mentah dari lalu lintas HTTP (Salin dari *Burp Repeater*). Soroti pada baris mana injeksi (*Payload*) disuntikkan, dan tunjukkan *Response* dari server (seperti pesan *error* SQL atau perbedaan ukuran balasan) yang membuktikan kerentanan tersebut.

**3. Visual Evidence (Tangkapan Layar & Video):**
Otak manusia lebih mudah memproses bukti visual.
- Untuk serangan sederhana seperti *RCE* atau *SQLi*, satu atau dua tangkapan layar (*Screenshot*) *Burp Repeater* biasanya sudah cukup.
- Untuk serangan kompleks (*Chaining Vulnerabilities*) atau eksploitasi *CSRF / Account Takeover*, **Video Rekaman Layar (Screencast)** berdurasi 1-2 menit adalah bukti absolut yang paling disukai perusahaan.

### Pantangan Menulis PoC
- **JANGAN menyuruh menggunakan alat otomatis** (misalnya *SQLMap*). *Developer* mungkin tidak mengerti cara menggunakan alat tersebut atau tidak menginstalnya. Selalu berikan instruksi serangan manual (misalnya *payload UNION/Sleep*) yang bisa direproduksi via *Browser* atau perintah *cURL*.
- **JANGAN merusak data di server produksi (*Production*).** Saat membuat PoC, gunakan *Safe Payload* (sebatas menampilkan peringatan *alert()*, memanggil perintah *sleep*, atau mengeksekusi *whoami*) untuk membuktikan adanya celah tanpa menghapus atau membocorkan data asli klien.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Ayo berlatih merakit langkah-langkah PoC di *text editor*!

1. Buka *Notepad / VS Code*.
2. Bayangkan kamu baru saja menemukan celah *Stored XSS* di kolom "Ubah Alamat Pengiriman" pada situs web e-commerce klien.
3. Rangkai instruksi <i>Steps to Reproduce</i> (Minimal 4 langkah).
4. Contoh:
   `### Steps to Reproduce :`
   `1. Lakukan login ke http://target.com menggunakan akun Test.`
   `2. Navigasikan ke halaman "Pengaturan Profil" -> "Alamat Pengiriman".`
   `3. Pada kolom input "Alamat Lengkap", isikan payload XSS berikut: <img src=x onerror=alert('PoC_Berhasil')>`
   `4. Klik tombol "Simpan".`
   `5. Navigasikan ke Halaman Utama (Home), lalu kembali lagi ke halaman Profil.`
   `6. Pop-up peringatan alert bertuliskan 'PoC_Berhasil' akan langsung dieksekusi oleh browser.`
5. Selamat, kamu baru saja meracik langkah reproduksi (PoC) yang jelas dan mudah diikuti oleh tim pengembang mana pun!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa sebutan untuk bagian dalam laporan pentest yang berisi panduan teknis langkah demi langkah agar pembaca (Developer) dapat mereproduksi dan memvalidasi serangan kerentanan?</summary>

**Jawaban:** Proof of Concept (PoC) atau <i>Steps to Reproduce</i>.
</details>

<details>
<summary>❓ Saat membuktikan celah <i>Blind SQLi Time-Based</i> (di mana data tidak muncul di layar dan tidak ada pesan error), bukti tangkapan layar (*Screenshot*) apa yang paling penting untuk dilampirkan?</summary>

**Jawaban:** Tangkapan layar *Burp Suite Repeater* yang dengan jelas menyorot waktu penundaan respons (misal: menyoroti bagian <i>Response time: 10,045 millis</i>) untuk membuktikan bahwa server dipaksa tertidur/menunggu oleh payload SQL.
</details>

<details>
<summary>❓ Mengapa seorang pentester sangat tidak disarankan menyuruh <i>Developer</i> untuk mereproduksi celah menggunakan alat peretasan otomatis (contoh: "Silakan jalankan SQLMap ")?</summary>

**Jawaban:** Karena *Developer* bukan pakar *Cybersecurity* (mereka belum tentu terampil/memiliki instalasi alat tersebut), dan alat otomatis dapat menyebabkan ketidakstabilan pada server produksi. PoC harus manual, terkontrol, dan mudah direproduksi langsung via *Browser* atau alat standar (*cURL*).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami pentingnya menyertakan *Proof of Concept* (PoC) yang solid.
- [ ] Saya mampu merangkai instruksi *Steps to Reproduce* yang sistematis dan detail.
- [ ] Saya mengerti pentingnya menyertakan bukti pendukung seperti <i>HTTP Request/Response</i> dan *Screenshot/Video*.
- [ ] Saya mengetahui pantangan dalam menyusun PoC (menghindari *tools* otomatis dan menjaga integritas server produksi).
- [ ] Saya telah menjawab seluruh *Quiz Kilat* dengan benar.

---

## 🔗 Resources

- [Bugcrowd Vulnerability Rating Taxonomy (VRT)](https://bugcrowd.com/vulnerability-rating-taxonomy) — Standar industri untuk penulisan laporan dalam ekosistem Bug Bounty.

---

## ➡️ Besok

**Day 4: Remediation & Mitigation Advice** — Kamu telah berhasil menemukan celah, membuktikan CVSS 9.8 Critical, dan menulis PoC yang sempurna. Lalu Direktur IT membalas laporanmu: *"Lalu apa yang harus kami lakukan agar hal ini tidak terjadi lagi?!"* Besok, kamu akan belajar menjadi konsultan solusi! Kamu dituntut menyusun panduan perbaikan: **Remediation Advice**! Belajarlah mengajari *Programmer* cara membangun pertahanan (misal: implementasi parameterisasi query, sanitasi input) yang kebal terhadap serangan siber.

---

*📅 TISS Null Teaming · Week 19 · Day 3 · BREACH Rank*
