# 🔤 Week 3 · Day 4: Akronim & Singkatan Cybersecurity

> **Rank**: CIPHER | **Minggu ke-3**, Hari 4/5 | **Durasi**: ~35 menit

📊 **Progress**: Week 3 · Day 4/5 | CIPHER Rank (Minggu 2 dari 3) | Overall: 14/120 hari (12%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengenali** singkatan dan akronim (abbreviation) yang paling sering digunakan dalam dokumen cybersecurity
2. **Memahami** makna di balik singkatan tersebut, bukan hanya panjangannya
3. **Membaca** artikel teknis dengan lebih lancar tanpa harus *googling* setiap kata yang disingkat

---

## 📖 Materi Inti

### Budaya "Alphabet Soup"

Di dunia militer dan IT (khususnya *cybersecurity*), orang sangat suka menggunakan singkatan. Jika kamu tidak hafal singkatan dasar, sebuah laporan teknis akan terlihat seperti "Sup Alfabet" yang membingungkan.

Contoh kalimat asli di dunia nyata:
*"The SOC detected an APT using an RCE vulnerability to bypass the WAF. The IoCs suggest they are pivoting via RDP."*

Jika kamu tidak tahu singkatannya, kamu akan tersesat! Mari kita bedah singkatan-singkatan paling krusial.

### 📜 20 Singkatan Wajib Hafal (Materi Inti)

Pahami konteksnya, bukan sekadar kepanjangannya.

#### Kategori: Kerentanan & Serangan (Red Team Fokus)
| Akronim | Kepanjangan | Makna Singkat |
|---------|-------------|---------------|
| **XSS** | Cross-Site Scripting | Celah di mana hacker bisa menyisipkan *script* (biasanya JavaScript) ke website, yang nantinya akan dieksekusi di browser korban lain. |
| **SQLi** | SQL Injection | Memasukkan perintah database palsu (SQL) lewat form input (seperti login) agar database bocor. |
| **RCE** | Remote Code Execution | (Paling Bahaya). Hacker bisa menjalankan perintah dari jarak jauh di server korban. Kiamat. |
| **CSRF** | Cross-Site Request Forgery | Memaksa browser korban untuk melakukan aksi (seperti transfer uang) tanpa mereka sadari saat mereka sedang login. |
| **DDoS** | Distributed Denial of Service | Menyerang server dengan trafik sangat besar dari banyak komputer (botnet) sekaligus agar server mati. |
| **APT** | Advanced Persistent Threat | Kelompok hacker tingkat (biasanya dibiayai negara) yang diam-diam nongkrong di jaringanmu selama berbulan-bulan. |

#### Kategori: Pertahanan & Organisasi (Blue Team Fokus)
| Akronim | Kepanjangan | Makna Singkat |
|---------|-------------|---------------|
| **SOC** | Security Operations Center | Fasilitas atau ruang pusat di mana tim Blue Team memantau keamanan 24/7. |
| **SIEM**| Security Information and Event Management | Software *dashboard* tempat berkumpulnya semua *log* keamanan perusahaan untuk dianalisis. |
| **WAF** | Web Application Firewall | Satpam khusus (firewall) yang berdiri di depan aplikasi web untuk menangkis serangan seperti SQLi dan XSS. |
| **IDS/IPS**| Intrusion Detection/Prevention System | Sistem alarm (IDS) atau penangkal otomatis (IPS) jika ada lalu lintas jaringan mencurigakan. |
| **IoC** | Indicator of Compromise | Barang bukti (IP jahat, *hash* virus) yang menunjukkan sistem telah kebobolan. Jejak si penjahat. |
| **TTPs** | Tactics, Techniques, and Procedures | "Gaya bermain" atau pola khas dari sebuah kelompok hacker saat menyerang. |

#### Kategori: Konsep & Standar (Semua Pilar)
| Akronim | Kepanjangan | Makna Singkat |
|---------|-------------|---------------|
| **CIA** | Confidentiality, Integrity, Availability | Tiga pilar utama keamanan siber. (Sudah kita pelajari di W1D3!) |
| **CVE** | Common Vulnerabilities and Exposures | Daftar kerentanan publik beserta ID-nya. |
| **CVSS**| Common Vulnerability Scoring System | Kalkulator skor seberapa bahaya sebuah celah (0-10). |
| **PoC** | Proof of Concept | Bukti nyata (video/script/langkah) bahwa celah keamanan itu benar-benar bisa di-hack. |
| **MFA/2FA**| Multi-Factor Authentication | Login pakai lebih dari satu cara (contoh: Password + Kode OTP SMS). |
| **VPN** | Virtual Private Network | Terowongan aman terenkripsi untuk komunikasi jaringan. |
| **OSINT**| Open Source Intelligence | Mencari informasi intelijen dari sumber publik (sosmed, google, public record). |

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari terjemahkan "Alphabet Soup" di awal materi tadi ke bahasa manusia biasa!

**Kalimat Asli:**
*"The SOC detected an APT using an RCE vulnerability to bypass the WAF. The IoCs suggest they are pivoting via RDP."* (Catatan: RDP = Remote Desktop Protocol).

**Tugas:** Gunakan tabel di atas untuk menerjemahkan kalimat tersebut menjadi paragraf Bahasa Indonesia yang bisa dipahami oleh manajermu.

<details>
<summary>🔑 Klik untuk melihat Terjemahan yang Baik</summary>

*"Tim **Pusat Operasi Keamanan (SOC)** kita mendeteksi adanya **kelompok peretas tingkat tinggi (APT)** yang menggunakan celah **eksekusi perintah jarak jauh (RCE)** untuk melewati **Satpam Aplikasi Web (WAF)** kita. Dari **jejak barang bukti (IoC)** yang ditinggalkan, terlihat mereka mencoba menyebar ke komputer lain menggunakan fitur Remote Desktop (RDP)."*

Gila, kan? Kalimat aslinya hanya dua baris, tapi padat sekali informasinya! Itulah gunanya singkatan.

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa singkatan Cross-Site Scripting adalah "XSS" dan bukan "CSS"?</summary>

**Jawaban:** Karena **CSS** (*Cascading Style Sheets*) sudah lebih dulu dipakai sebagai nama bahasa untuk menghias tampilan website (desain web). Untuk menghindari kebingungan, dunia keamanan komputer sepakat menggunakan huruf **X** (sebagai simbol "Cross") sehingga menjadi **XSS**.

</details>

<details>
<summary>❓ Jika atasanmu meminta daftar "IoC" dari serangan kemarin, apa yang sebenarnya dia minta?</summary>

**Jawaban:** Atasanmu meminta **Indicator of Compromise**, yaitu jejak digital atau bukti-bukti spesifik peninggalan *hacker*. Ini bisa berupa: Alamat IP asal serangan, nama *file malware*, *hash malware*, atau URL mencurigakan. Daftar ini nanti dimasukkan ke *Firewall/SIEM* agar serangan dari sumber yang sama otomatis diblokir di masa depan.

</details>

<details>
<summary>❓ Antara IDS dan IPS, mana yang akan secara aktif memblokir serangan yang masuk?</summary>

**Jawaban:** **IPS** (*Intrusion Prevention System*).
- **IDS** (*Detection*) hanya mendeteksi dan memberi *alert* (seperti alarm kebakaran berbunyi).
- **IPS** (*Prevention*) mendeteksi lalu secara aktif memblokir trafik/mematikan koneksi (seperti alarm kebakaran yang langsung menyemprotkan air).

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya sudah menghafal kepanjangan dan konteks dari 20 akronim krusial di atas
- [ ] Saya mengerti perbedaan XSS dan SQLi
- [ ] Saya paham apa fungsi dari WAF dan SIEM
- [ ] Saya sudah menyelesaikan Mini Lab menerjemahkan "Alphabet Soup"
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Cybersecurity Acronyms and Abbreviations Cheat Sheet (SANS)](https://www.sans.org) — (Opsional) Jika kamu mau melihat daftar yang berisi *ratusan* akronim. Tapi pelajari 20 di atas dulu!

---

## ➡️ Besok

**Day 5: Lab & Mission: Tulis Bug Report** — Saatnya *Capstone* minggu ketiga! Kamu akan diberikan skenario penemuan kerentanan (*bug*), dan kamu harus menulis *Bug Report* lengkap layaknya profesional di program *Bug Bounty*. Hadiahnya? Pengakuan sebagai hacker yang tidak hanya jago, tapi juga komunikatif! 📝

---

*📅 TISS Null Teaming · Week 3 · Day 4 · CIPHER Rank*
