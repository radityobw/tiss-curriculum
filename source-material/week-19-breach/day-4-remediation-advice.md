# 💀 Week 19 · Day 4: Remediation & Mitigation Advice

> **Rank**: BREACH | **Minggu ke-19**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 19 · Day 4/5 | BREACH Rank (Minggu 5 dari 5) | Overall: 94/120 hari (79%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** peran penguji keamanan (*Red Team*) berhadapan dengan tanggung jawab penambal (*Blue Team*).
2. **Meracik** naskah saran perbaikan (<i>Remediation Advice</i>) yang <i>Actionable</i>.
3. **Mengeksploitasi** standar industri (OWASP) laksana referensi mitigasi.

---

## 📖 Materi Inti

### Menjelma Konsultan (Mitigation)

Seorang penguji keamanan (*Attacker/Pentester*) dihormati karena ketajamannya menemukan celah. Namun seorang Profesional Konsultan dihargai mahal karena kepiawaiannya memberikan solusi untuk menambal lubang yang dirobeknya itu.
Bagian terakhir laporan <i>Pentest</i> memuat **Remediation & Mitigation (Saran Perbaikan)**.

Tanpa saran perbaikan, korporat (Developer) bakal meraba dalam kegelapan tak tahu cara menambal celah <i>SQL Injection</i> yang kamu laporkan.

### Solusi Praktis (Make it Actionable!)

Banyak <i>Pentester</i> pemula menulis Remediasi seperti ini :
- ❌ *"Tolong amankan database-nya."* (Sangat tidak berguna!).
- ❌ *"Filter karakter kutip pada parameter ID."* (Buruk, <i>Attacker</i> masih bisa mengakali pakai <i>Double URL Encoding</i>).

Saran perbaikan (Remediasi) haruslah **Actionable** (Bisa langsung diprogram).
- ✅ **Remediasi SQLi :** *"Hentikan merangkai Kueri SQL secara dinamis. Gunakan arsitektur **Prepared Statements (Parameterized Queries)** bawaan PDO di PHP atau ORM."*
- ✅ **Remediasi XSS :** *"Terapkan arsitektur **Context-Aware Output Encoding** sebelum melempar data <i>Database</i> ke layar HTML Browser pengguna, serta aplikasikan tajuk pelindung **Content Security Policy (CSP)**."*
- ✅ **Remediasi CSRF :** *"Tanamkan token **Anti-CSRF Token** acak pada setiap sesi formulir POST, dan sematkan atribut `SameSite=Lax` pada <i>Cookie</i> Login."*

### Menyandar pada Standar Industri (OWASP Cheat Sheets)

Penganalisis tak perlu repot mengarang resep perbaikan sendiri. Di dunia keamanan siber telah tersedia referensi penyembuh segala kerentanan : **OWASP Cheat Sheet Series**.
Dalam laporan, cukup cantumkan tautan URL referensi (Reference Links) dari OWASP agar <i>Developer</i> korporat merujuk langsung ke panduan koding mitigasinya!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Ayo rakit nalar penyembuh resep Remediasi!

1. Siapkan lembar teks digital (Notepad).
2. Bayangkan kamu menemukan kelalaian unggah berkas **File Upload to RCE** (di mana kamu menyusupkan cangkang `shell.php`).
3. Tulis racikan resep <i>Remediation Advice</i> (Saran Perbaikan).
4. **Contoh Resep Mutlak :**
 - *"1. Jangan mengandalkan validasi di <i>Frontend</i> (JavaScript)."*
 - *"2. Validasi jenis berkas di <i>Backend</i> bukan berpatokan nama ekstensi, melainkan mengevaluasi **MIME-Type & Magic Bytes** (File Signature) berkas gambar."*
 - *"3. Simpan hasil unggahan di server (Storage) yang **TERPISAH** dari rute eksekusi kode <i>Web Server</i>, atau lumpuhkan wewenang hak eksekusi (Execute Permissions) skrip di folder direktori `/uploads/`."*
5. Resep perbaikan itu kelak menyelamatkan perusahaan dari insiden keamanan siber!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengurai tabir taktik perbaikan, mengapa saran Remediasi "Filter saja huruf kutip tunggal ('')" dinilai sebagai saran mitigasi untuk meredam celah <i>SQLi</i> yang amat buruk dan amatiran?</summary>

**Jawaban:** Lantaran penyerang (<i>Attacker</i>) masih leluasa menelikung (Bypass) pelindung penyaring dangkal tersebut membalut kueri bermodalkan taktik manipulasi enkripsi (<i>URL Encoding</i>, <i>Hex Encoding</i>, dsb). Solusi penangkal <i>SQLi</i> di era modern bukanlah mem-filter input, melainkan menggunakan <i>Parameterized Queries</i> (Prepared Statements).
</details>

<details>
<summary>❓ Ketika meluncurkan saran perbaikan <i>XSS (Cross-Site Scripting)</i> bagi tim <i>Developer</i>, fitur pertahanan arsitektur peramban (berupa tajuk <i>Header HTTP</i>) apakah yang lazim diwajibkan <i>Pentester</i> agar disisipkan guna meredam eksekusi racun skrip gelap?</summary>

**Jawaban:** <i>Content Security Policy</i> (CSP).
</details>

<details>
<summary>❓ Ketika penganalisis menenggak kehabisan akal merajut merumuskan solusi koding bahasa teknis mitigasi (Remediation) suatu kerentanan (misal IDOR), kitab dunia (diterbitkan OWASP) apakah yang selalu dikutip <i>hacker</i> laksana buku panduan obat pengembang perangkat lunak?</summary>

**Jawaban:** OWASP Cheat Sheet Series.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap dominasi pentingnya *Actionable Mitigation* - [ ] Saya fasih membelah siasat resep penyembuh *SQLi* (Prepared Statements)
- [ ] Saya menguasai titah peracikan obat penangkal *XSS (Encoding & CSP)* - [ ] Saya paham bahwasanya menyertakan *OWASP* sangatlah vital - [ ] Saya telah menjawab seluruh ulasan *quiz kilat* 
---

## 🔗 Resources

- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — kitab suci referensi membedah mitigasi pencegahan lubang.

---

## ➡️ Besok

**Day 5: Lab & Mission: Create a Full Pentest Report** — Dirimu telah meraba *Executive Summary*, merajut angka insiden *CVSS v3.1*, membungkus tangkapan layar *PoC*, lantas menuangkan resep penyembuh *Remediation*. Esok harinya, altar pengujian (Penilaian Akhir Breach) menantangmu! Satukan keempat elemen itu menjadi satu dokumen Laporan *Penetration Testing* yang otentik dan sempurna. Buktikan dirimu layak menyandang predikat penguji keamanan korporat elit!

---

*📅 TISS Null Teaming · Week 19 · Day 4 · BREACH Rank*
