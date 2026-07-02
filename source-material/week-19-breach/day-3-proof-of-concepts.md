# 💀 Week 19 · Day 3: Writing Good Proof of Concepts (PoCs)

> **Rank**: BREACH | **Minggu ke-19**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 19 · Day 3/5 | BREACH Rank (Minggu 5 dari 5) | Overall: 93/120 hari (78%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** esensi pembuktian telak dokumen *Proof of Concept* (PoC).
2. **Merakit** langkah-langkah reproduksi eksploitasi (*Steps to Reproduce*).
3. **Menerapkan** pajangan barang bukti (<i>HTTP Request/Response</i> & <i>Screenshots</i>).

---

## 📖 Materi Inti

### Membantah Alibi dengan Bukti Otentik (Proof of Concept)

Dalam industri *Bug Bounty*, seringkali peretas pemula meratapi laporannya DITOLAK (Status *Not Applicable* atau *Can't Reproduce*). Bukan karena mereka tak menemukan celah, tapi karena mereka gagal memandu *Developer* menirukan serangan tersebut!

**Proof of Concept (PoC)** adalah jantung dari laporan. Ia adalah resep eksploitasi. Kalau kamu menulis PoC dengan cemerlang, *Developer* yang membacanya bakal sukses menduplikasi celah yang sama persis dalam hitungan detik.

### 3 Pilar PoC yang Komprehensif

**1. Steps to Reproduce (Langkah Reproduksi):**
Tulislah instruksi layaknya panduan teknis. Jangan melompati satu langkah pun.
- *BURUK :* "Eksekusi SQLi ke parameter ID."
- *SEMPURNA :* 
 - "Langkah 1: Kunjungi URL `http://target.com/produk` "
 - "Langkah 2: Tangkap lalu lintas (*Intercept*) di *Burp Suite*."
 - "Langkah 3: Ubah payload `id=1` menjadi `id=1' AND SLEEP(10)--`."
 - "Langkah 4: Tekan tombol <i>Forward</i> dan amati <i>Browser</i> memutar (loading) selama 10 detik."

**2. HTTP Request & Response (Barang Bukti Teknis):**
Sisipkan teks mentahan lalu-lintas (Salin dari Burp *Repeater*). Soroti di baris mana serangan (Payload) disuntikkan, dan di baris <i>Response</i> mana serangan SQL galat memuntahkan indikasi kerentanan.

**3. Visual Evidence (Tangkapan Layar & Video):**
Otak manusia mencintai gambar.
- Untuk serangan *RCE* atau *SQLi*, sebiji tangkapan layar *Burp Repeater* sudah cukup.
- Untuk retasan rumit *Chaining Vulnerabilities* atau manipulasi berantai *CSRF+ATO*, **Video Rekaman Layar (Screencast)** berdurasi 1 menit adalah absolut yang tak terbantahkan!

### Pantangan Menulis PoC
- JANGAN menyuruh mengeksploitasi pakai *SQLMap otomatis*. (Developer tak paham instalasi SQLMap). Berikan Payload *Manual* (Misal payload UNION) agar mereka bisa mengetiknya sendiri di <i>Browser</i>.
- JANGAN mendemonstrasikan kerentanan di server produksi *(Production)* sampai merusak data perusahaan. Gunakan *Safe Payload* (sebatas memanggil `sleep` atau `whoami`).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Ayo rakit pembuktian (PoC) di atas kertas teks editor!

1. Buka *Notepad / VS Code*.
2. Bayangkan kamu baru menemukan celah *Stored XSS* di kolom "Ubah Alamat Pengiriman" milik e-commerce.
3. Rangkai <i>Steps to Reproduce</i> (Minimal 4 langkah).
4. Contoh :
 `### Steps to Reproduce :`
 `1. Login ke http://target.com pakai akun Test.`
 `2. Pergi ke tab "Pengaturan Profil" -> "Alamat Pengiriman".`
 `3. Pada kolom "Alamat Lengkap", isikan payload : <img src=x onerror=alert('PoC_Berhasil')>`
 `4. Klik Simpan.`
 `5. Pergi ke Halaman Utama (Home), lalu kembali lagi ke Profil.`
 `6. Pop-up peringatan bertuliskan 'PoC_Berhasil' akan muncul di layar.`
5. Selamat, kamu baru saja meracik resep serangan (PoC) yang takkan pernah bisa dibantah oleh tim IT mana pun!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membuka anatomi dokumen laporan peretasan, apa sebutan untuk seksi bagian di mana penganalisis mendiktekan panduan langkah demi langkah resep agar penerima laporan (*Developer*) mampu menduplikasi serangan?</summary>

**Jawaban:** Proof of Concept (PoC) atau <i>Steps to Reproduce</i>.
</details>

<details>
<summary>❓ Ketika meluncurkan pembuktian celah <i>Blind SQLi Time-Based</i> (di mana tak ada tabel yang bocor maupun <i>Error</i> yang muncul), tangkapan layar visual apakah yang paling krusial disertakan di PoC sebagai barang bukti?</summary>

**Jawaban:** Tangkapan visual layar alat <i>Burp Suite Repeater</i> yang menyorot bagian selisih waktu respons (misal menyorot indikator balasan <i>Response time : 10,045 millis</i>) membuktikan peladen dipaksa tertidur.
</details>

<details>
<summary>❓ Di ranah pengujian penyusunan PoC, mengapa penganalisis sangat diharamkan menyuruh tim IT Developer perusahaan agar mengeksploitasi ulang mereproduksi celah menggunakan alat otomatis (contoh : "Silakan jalankan SQLMap ")?</summary>

**Jawaban:** Karena <i>Developer</i> bukan pakar <i>Cybersecurity</i> (mereka belum tentu terampil memasang/menjalankan SQLMap), dan otomatis bisa membuahkan ketidakstabilan di <i>Server</i> produksi. PoC haruslah manual, sederhana, dan bisa direproduksi langsung via <i>Browser</i> biasa atau <i>cURL</i>.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap dominasi pembuktian resep *PoC* - [ ] Saya fasih merangkai hirarki eksekusi *Steps to Reproduce* yang tak terbantahkan - [ ] Saya cakap menerjemahkan tangkapan <i>HTTP Request/Response</i> - [ ] Saya paham bahaya laten menggunakan SQLMap dalam penyusunan *PoC* - [ ] Saya telah menjawab seluruh ulasan *quiz kilat* 
---

## 🔗 Resources

- [Bugcrowd Vulnerability Rating Taxonomy (VRT)](https://bugcrowd.com/vulnerability-rating-taxonomy) — Kumpulan referensi taktik panduan standar industri laporan Bug Bounty dunia.

---

## ➡️ Besok

**Day 4: Remediation & Mitigation Advice** — Kau sukses menemukan kerentanan, memamerkan CVSS 9.8 Critical, dan menulis PoC sempurna. Lantas Direktur IT membalas laporanmu dengan kalimat : *"Lalu kami harus bagaimana agar tidak diretas lagi?!"* Esok harinya, dirimu bakal menjelma konsultan penyembuh . Kamu dituntut merajut panduan resep obat mujarab penawar kerentanan : **Remediation Advice**! Ajari <i>Programmer</i> cara merajut benteng pertahanan yang tak lekang oleh serangan!

---

*📅 TISS Null Teaming · Week 19 · Day 3 · BREACH Rank*
